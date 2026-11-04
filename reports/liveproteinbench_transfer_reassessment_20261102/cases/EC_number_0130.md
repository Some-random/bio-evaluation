# EC_number_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0130.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 1.1.1.195

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAKSPEVEHPVKAFGWAARDPSGVLSPFNFSRRATGEHDVQFKVLYCGICHSDLHMIKNEWGFTKYPIVPGHEIVGVVTEVGSKVEKFKVGDKVGVGCLVGSCRKCDMCSDDLENYCPGQILTYSAAYTDGTTTYGGYSNLMVSDEHFVICWPENLPMDIGAPLLCAGITTYSPLRYFGLDKPGTHVGVVGLGGLGHVAVKFAKAFGAKVTVISTSESKKQEAIEKLGADAFLVSRDPEQMQGAAGSMDGIIDTVSAVHPVLPLVNLLKSQGKLIMVGAPEKPLELPVFPLLAGRRIIAGSAIGGLKETQEMIDFAAKNNILPDVELVPMDYVNTAMERLLKADVKYRFVIDIGNTLKSA

[Multiple Choices]
A. 1.1.1.122
B. 1.1.1.195
C. 3.2.1.20
D. 3.1.3.16
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

> The source record matches the supplied sequence and assigns EC 1.1.1.195. It also links that EC to the cinnamyl alcohol/cinnamaldehyde reaction with experimental evidence cited to a publication. The primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a zinc-dependent medium-chain dehydrogenase/reductase, including conserved metal-binding features and a cofactor-binding region. Transferable knowledge of plant cinnamyl-alcohol-dehydrogenase-like proteins supports EC 1.1.1.195 among these options; the two hydrolase choices are a poor fit, and the other oxidoreductase choice is less consistent with this family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully favor the cinnamyl-alcohol-dehydrogenase EC over the offered alternatives. Exact substrate preference is not guaranteed by family membership alone, so this is a defensible inference rather than proof of the specific reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option has comparably strong support from the sequence and transferable family-level knowledge.


### Important caveats

- The experimental support is represented in the supplied source annotation and its cited publication; that publication was not independently assessed.
- The reviewed source identifies the exact sequence, but that target-specific identity is not used as the basis for the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent medium-chain dehydrogenase/reductase, including conserved metal-binding features and a cofactor-binding region. Transferable knowledge of plant cinnamyl-alcohol-dehydrogenase-like proteins supports EC 1.1.1.195 among these options; the two hydrolase choices are a poor fit, and the other oxidoreductase choice is less consistent with this family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully favor the cinnamyl-alcohol-dehydrogenase EC over the offered alternatives. Exact substrate preference is not guaranteed by family membership alone, so this is a defensible inference rather than proof of the specific reaction."
  },
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and assigns EC 1.1.1.195. It also links that EC to the cinnamyl alcohol/cinnamaldehyde reaction with experimental evidence cited to a publication. The primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental support is represented in the supplied source annotation and its cited publication; that publication was not independently assessed.",
    "The reviewed source identifies the exact sequence, but that target-specific identity is not used as the basis for the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparably strong support from the sequence and transferable family-level knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The source record matches the supplied sequence and assigns EC 1.1.1.195. It also links that EC to the cinnamyl alcohol/cinnamaldehyde reaction with experimental evidence cited to a publication. The primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent medium-chain dehydrogenase/reductase, including conserved metal-binding features and a cofactor-binding region. Transferable knowledge of plant cinnamyl-alcohol-dehydrogenase-like proteins supports EC 1.1.1.195 among these options; the two hydrolase choices are a poor fit, and the other oxidoreductase choice is less consistent with this family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully favor the cinnamyl-alcohol-dehydrogenase EC over the offered alternatives. Exact substrate preference is not guaranteed by family membership alone, so this is a defensible inference rather than proof of the specific reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparably strong support from the sequence and transferable family-level knowledge."
  },
  "important_caveats": [
    "The experimental support is represented in the supplied source annotation and its cited publication; that publication was not independently assessed.",
    "The reviewed source identifies the exact sequence, but that target-specific identity is not used as the basis for the transferability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina) is annotated with EC 1.1.1.195 backed by experimental evidence (ECO:0000269, PubMed:26715562). The catalytic reaction (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+) is confirmed. The benchmark sequence (360 aa) matches the source entry exactly. The evidence code ECO:0000269 indicates inference from direct assay, confirming experimental validation of the EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits hallmark features of the medium-chain dehydrogenase/reductase (MDR) family: (1) a Rossmann-like NAD(P)+-binding region near the N-terminus, (2) a zinc-binding motif with multiple cysteines in a glycine-rich context ('GDKVGVGCLVGSCRKCDMC'), and (3) a C-terminal domain typical of MDR enzymes. These features immediately eliminate options C (β-glucosidase, EC 3.2.1.20, a glycosyl hydrolase with a (β/α)8 TIM-barrel fold and catalytic Glu/Asp residues) and D (phosphoprotein phosphatase, EC 3.1.3.16, a hydrolase with distinct metal-binding motifs like DXDxDx). Between A (EC 1.1.1.122, L-arabinose reductase) and B (EC 1.1.1.195, cinnamyl-alcohol dehydrogenase): EC 1.1.1.122 is predominantly a member of the aldo-keto reductase (AKR) superfamily, which uses a catalytic Tyr-Lys-Asp/His triad, has a β-sheet barrel fold, and lacks zinc-binding cysteines. The clear MDR zinc-binding architecture in this sequence is inconsistent with AKR family membership, favoring B. Additionally, the ~360-aa length, plant-type sequence context, and the specific Cys arrangement in the zinc-binding site are consistent with characterized plant CAD enzymes (a well-known MDR subfamily).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of protein families can distinguish the MDR/zinc-dependent ADH architecture (present here) from the AKR fold (typical of EC 1.1.1.122), and can rule out glycosidases and phosphatases by their entirely different structural and catalytic features. The zinc-binding cysteine motif in a glycine-rich context is a transferable family-level signature shared across MDR enzymes, and the absence of AKR catalytic triad residues disfavors option A. This constitutes a legitimate family-level inference from sequence features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are in entirely different EC classes (hydrolases) with incompatible sequence architectures. Option A (EC 1.1.1.122) is typically an AKR-family enzyme lacking the zinc-binding cysteine motif clearly present here. While distinguishing between different MDR subfamily members from sequence alone can be challenging, among the four offered choices the MDR zinc-binding architecture plus plant context provides a clear preference for B over A.


### Important caveats

- The reviewer-only evidence confirms experimental validation (ECO:0000269) of the EC assignment, but this evidence was not available to the evaluated model.
- Distinguishing EC 1.1.1.195 from other MDR-family alcohol dehydrogenases (not offered as options) would require more specific annotation; however, the question only asks to choose among the four given alternatives.
- Some rare L-arabinose reductases in certain organisms may belong to the MDR family, but the predominant and well-characterized assignment for EC 1.1.1.122 is AKR, making the family-level inference reasonable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits hallmark features of the medium-chain dehydrogenase/reductase (MDR) family: (1) a Rossmann-like NAD(P)+-binding region near the N-terminus, (2) a zinc-binding motif with multiple cysteines in a glycine-rich context ('GDKVGVGCLVGSCRKCDMC'), and (3) a C-terminal domain typical of MDR enzymes. These features immediately eliminate options C (β-glucosidase, EC 3.2.1.20, a glycosyl hydrolase with a (β/α)8 TIM-barrel fold and catalytic Glu/Asp residues) and D (phosphoprotein phosphatase, EC 3.1.3.16, a hydrolase with distinct metal-binding motifs like DXDxDx). Between A (EC 1.1.1.122, L-arabinose reductase) and B (EC 1.1.1.195, cinnamyl-alcohol dehydrogenase): EC 1.1.1.122 is predominantly a member of the aldo-keto reductase (AKR) superfamily, which uses a catalytic Tyr-Lys-Asp/His triad, has a β-sheet barrel fold, and lacks zinc-binding cysteines. The clear MDR zinc-binding architecture in this sequence is inconsistent with AKR family membership, favoring B. Additionally, the ~360-aa length, plant-type sequence context, and the specific Cys arrangement in the zinc-binding site are consistent with characterized plant CAD enzymes (a well-known MDR subfamily).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of protein families can distinguish the MDR/zinc-dependent ADH architecture (present here) from the AKR fold (typical of EC 1.1.1.122), and can rule out glycosidases and phosphatases by their entirely different structural and catalytic features. The zinc-binding cysteine motif in a glycine-rich context is a transferable family-level signature shared across MDR enzymes, and the absence of AKR catalytic triad residues disfavors option A. This constitutes a legitimate family-level inference from sequence features."
  },
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina) is annotated with EC 1.1.1.195 backed by experimental evidence (ECO:0000269, PubMed:26715562). The catalytic reaction (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+) is confirmed. The benchmark sequence (360 aa) matches the source entry exactly. The evidence code ECO:0000269 indicates inference from direct assay, confirming experimental validation of the EC assignment."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms experimental validation (ECO:0000269) of the EC assignment, but this evidence was not available to the evaluated model.",
    "Distinguishing EC 1.1.1.195 from other MDR-family alcohol dehydrogenases (not offered as options) would require more specific annotation; however, the question only asks to choose among the four given alternatives.",
    "Some rare L-arabinose reductases in certain organisms may belong to the MDR family, but the predominant and well-characterized assignment for EC 1.1.1.122 is AKR, making the family-level inference reasonable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are in entirely different EC classes (hydrolases) with incompatible sequence architectures. Option A (EC 1.1.1.122) is typically an AKR-family enzyme lacking the zinc-binding cysteine motif clearly present here. While distinguishing between different MDR subfamily members from sequence alone can be challenging, among the four offered choices the MDR zinc-binding architecture plus plant context provides a clear preference for B over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0U4AHM6 (CAD2_RAUSE, Cinnamyl alcohol dehydrogenase 2 from Rauvolfia serpentina) is annotated with EC 1.1.1.195 backed by experimental evidence (ECO:0000269, PubMed:26715562). The catalytic reaction (E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+) is confirmed. The benchmark sequence (360 aa) matches the source entry exactly. The evidence code ECO:0000269 indicates inference from direct assay, confirming experimental validation of the EC assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits hallmark features of the medium-chain dehydrogenase/reductase (MDR) family: (1) a Rossmann-like NAD(P)+-binding region near the N-terminus, (2) a zinc-binding motif with multiple cysteines in a glycine-rich context ('GDKVGVGCLVGSCRKCDMC'), and (3) a C-terminal domain typical of MDR enzymes. These features immediately eliminate options C (β-glucosidase, EC 3.2.1.20, a glycosyl hydrolase with a (β/α)8 TIM-barrel fold and catalytic Glu/Asp residues) and D (phosphoprotein phosphatase, EC 3.1.3.16, a hydrolase with distinct metal-binding motifs like DXDxDx). Between A (EC 1.1.1.122, L-arabinose reductase) and B (EC 1.1.1.195, cinnamyl-alcohol dehydrogenase): EC 1.1.1.122 is predominantly a member of the aldo-keto reductase (AKR) superfamily, which uses a catalytic Tyr-Lys-Asp/His triad, has a β-sheet barrel fold, and lacks zinc-binding cysteines. The clear MDR zinc-binding architecture in this sequence is inconsistent with AKR family membership, favoring B. Additionally, the ~360-aa length, plant-type sequence context, and the specific Cys arrangement in the zinc-binding site are consistent with characterized plant CAD enzymes (a well-known MDR subfamily).",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of protein families can distinguish the MDR/zinc-dependent ADH architecture (present here) from the AKR fold (typical of EC 1.1.1.122), and can rule out glycosidases and phosphatases by their entirely different structural and catalytic features. The zinc-binding cysteine motif in a glycine-rich context is a transferable family-level signature shared across MDR enzymes, and the absence of AKR catalytic triad residues disfavors option A. This constitutes a legitimate family-level inference from sequence features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are in entirely different EC classes (hydrolases) with incompatible sequence architectures. Option A (EC 1.1.1.122) is typically an AKR-family enzyme lacking the zinc-binding cysteine motif clearly present here. While distinguishing between different MDR subfamily members from sequence alone can be challenging, among the four offered choices the MDR zinc-binding architecture plus plant context provides a clear preference for B over A."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms experimental validation (ECO:0000269) of the EC assignment, but this evidence was not available to the evaluated model.",
    "Distinguishing EC 1.1.1.195 from other MDR-family alcohol dehydrogenases (not offered as options) would require more specific annotation; however, the question only asks to choose among the four given alternatives.",
    "Some rare L-arabinose reductases in certain organisms may belong to the MDR family, but the predominant and well-characterized assignment for EC 1.1.1.122 is AKR, making the family-level inference reasonable."
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
  "benchmark_sequence_length": 360,
  "benchmark_sequence_sha256": "7aad12ce1f502060a2c409f7c29cb9e2c0eeaa19ba50f8e4c2966e112d90861b",
  "current_entry_audit": {
    "entryVersion": 28,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 360,
  "current_source_sequence_sha256": "7aad12ce1f502060a2c409f7c29cb9e2c0eeaa19ba50f8e4c2966e112d90861b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 27,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U4AHM6",
  "selected_historical_entry_version": 27,
  "selected_historical_record_sha256": "e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458",
  "selected_historical_source_sequence_length": 360,
  "selected_historical_source_sequence_sha256": "7aad12ce1f502060a2c409f7c29cb9e2c0eeaa19ba50f8e4c2966e112d90861b",
  "selected_historical_version": {
    "accession": "A0A0U4AHM6",
    "database": "Swiss-Prot",
    "entryVersion": 27,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CAD2_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U4AHM6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":28,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR6\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsRR6\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.195\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Cinnamyl alcohol dehydrogenase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsCAD2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:10394\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.195\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"name\":\"(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:10392\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16731\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33227\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82980.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROTEIN SEQUENCE OF 43-53 AND 66-77\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:23.084054+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "729526cd490e7835c63bf23151cfac76f61e2eee15d3331fc705b3c325c26d70",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4AHM6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H1",
  "excerpt": "ID   CAD2_RAUSE              Reviewed;         360 AA.\nAC   A0A0U4AHM6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 27.\nDE   RecName: Full=Cinnamyl alcohol dehydrogenase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsCAD2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.1.1.195 {ECO:0000269|PubMed:26715562};\nDE   AltName: Full=Protein RR6 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR6 {ECO:0000303|PubMed:26715562};\nGN   Name=CAD2 {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR6 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:26.964793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458",
  "url": "https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Cinnamyl alcohol dehydrogenase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsCAD2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.1.1.195 {ECO:0000269|PubMed:26715562};\nDE   AltName: Full=Protein RR6 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR6 {ECO:0000303|PubMed:26715562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:26.964793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458",
  "url": "https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82980.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 43-53 AND 66-77, FUNCTION,\nRP   CATALYTIC ACTIVITY, AND TISSUE SPECIFICITY.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:26.964793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458",
  "url": "https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27)

```json
{
  "entry_version": 27,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(E)-cinnamyl alcohol + NADP(+) = (E)-cinnamaldehyde + NADPH +\nCC         H(+); Xref=Rhea:RHEA:10392, ChEBI:CHEBI:15378, ChEBI:CHEBI:16731,\nCC         ChEBI:CHEBI:33227, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;\nCC         EC=1.1.1.195; Evidence={ECO:0000269|PubMed:26715562};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:10394;\nCC         Evidence={ECO:0000269|PubMed:26715562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:26.964793+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e85fa680b6b0f4b7eb19749997dc2e80edd7537f4e965d90637174bac9c0e458",
  "url": "https://rest.uniprot.org/unisave/A0A0U4AHM6?format=txt&versions=27"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
