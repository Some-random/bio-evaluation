# catalytic_activity_0121

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0121.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — a quinone + NADH + H(+) = a quinol + NAD(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTAAGFNSILCLRQLVRLNRRQYSAPAKSVLSGSQTNDQATPPPTSKSADKMRGWQLHNYGDIDELQLSEMLKIPQIRCSNECLVRIRATAVNPIDLAMLRGYGATVLNKMRCQPGDGIEFPLILGREFCGELVQTGMGVSLPLGSRVWGVVPLQATIGSHAEYVAVPSYCLAPAPKELDDYEAASVLYAGLTAWSGLYITGGLGGPCGATTASGGGAHKRVLVLGGSGGVGTLAIQILKSQKVQVLATCSENAIEMVRNLGADLVVDYNNPQAMEELCKYAPYDIVLDCAGQGGQKAAESKYDFRQYITFSSPLLANIDKQGLGVGALKNVFDLFQTNVRSVTQRGGLVKWGFFSPAPQGIQFLQKLVEQRKLMPLIDSSYGFSELPKAFEKMKSGHLRGKIVVKLREETGD

[Multiple Choices]
A. a cytidine in tRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in tRNA + ADP + phosphate + CoA + H(+)
B. (19E)-geissoschizine + NADPH + H(+) = (16R,19Z)-isositsirikine + NADP(+)
C. a quinone + NADH + H(+) = a quinol + NAD(+)
D. L-dopa + H(+) = dopamine + CO2
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

> The sequence-matched UniProt record annotates the NADH-dependent quinone reduction in choice C. The annotation is supported by similarity to another protein (ECO:0000250), so it is not direct experimental evidence for this exact sequence.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long enzyme-like protein with glycine-rich regions consistent with a nucleotide-binding oxidoreductase, making quinone reduction with NADH a plausible choice. This transferable class-level inference distinguishes C from the tRNA acetylation, specialized alkaloid transformation, and PLP-dependent amino-acid decarboxylation alternatives. The sequence alone does not establish the precise substrate or cofactor with certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A meaningful choice is available from enzyme-class and sequence-pattern reasoning; the answer need not depend on recalling this exact protein's database entry, although that entry provides supporting confirmation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C matches the annotated NADH-dependent quinone-to-quinol reaction among the offered options.


### Important caveats

- The supporting catalytic-activity annotation is transferred by similarity rather than cited as a direct assay of the supplied protein.
- The record also annotates a related NADPH-dependent quinone reduction, but that reaction is not one of the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long enzyme-like protein with glycine-rich regions consistent with a nucleotide-binding oxidoreductase, making quinone reduction with NADH a plausible choice. This transferable class-level inference distinguishes C from the tRNA acetylation, specialized alkaloid transformation, and PLP-dependent amino-acid decarboxylation alternatives. The sequence alone does not establish the precise substrate or cofactor with certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A meaningful choice is available from enzyme-class and sequence-pattern reasoning; the answer need not depend on recalling this exact protein's database entry, although that entry provides supporting confirmation."
  },
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the NADH-dependent quinone reduction in choice C. The annotation is supported by similarity to another protein (ECO:0000250), so it is not direct experimental evidence for this exact sequence."
  },
  "important_caveats": [
    "The supporting catalytic-activity annotation is transferred by similarity rather than cited as a direct assay of the supplied protein.",
    "The record also annotates a related NADPH-dependent quinone reduction, but that reaction is not one of the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C matches the annotated NADH-dependent quinone-to-quinol reaction among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the NADH-dependent quinone reduction in choice C. The annotation is supported by similarity to another protein (ECO:0000250), so it is not direct experimental evidence for this exact sequence.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long enzyme-like protein with glycine-rich regions consistent with a nucleotide-binding oxidoreductase, making quinone reduction with NADH a plausible choice. This transferable class-level inference distinguishes C from the tRNA acetylation, specialized alkaloid transformation, and PLP-dependent amino-acid decarboxylation alternatives. The sequence alone does not establish the precise substrate or cofactor with certainty.",
    "missing_item_specific_fact": "",
    "reason": "A meaningful choice is available from enzyme-class and sequence-pattern reasoning; the answer need not depend on recalling this exact protein's database entry, although that entry provides supporting confirmation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C matches the annotated NADH-dependent quinone-to-quinol reaction among the offered options."
  },
  "important_caveats": [
    "The supporting catalytic-activity annotation is transferred by similarity rather than cited as a direct assay of the supplied protein.",
    "The record also annotates a related NADPH-dependent quinone reduction, but that reaction is not one of the offered choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8IPZ3 (RTN4IP1_DROME) annotates the catalytic activity as 'a quinone + NADH + H(+) = a quinol + NAD(+)' (EC 1.6.5.2), matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), and a 2024 experimental paper (Park et al., Nat. Chem. Biol. 20:221-233) confirms RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q synthesis. The annotation is supported by both similarity transfer and experimental validation.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits two key transferable features: (1) an N-terminal mitochondrial targeting presequence (MTAAGFNSILCLRQLVRLNRRQ...), indicating a mitochondrial enzyme, and (2) a Rossmann-fold NAD(P)H-binding motif 'GGSGGVGTLAIQ' (the canonical GxGxxG nucleotide-binding pattern). These features together point to a mitochondrial NAD(P)H-dependent oxidoreductase. Choice D (DOPA decarboxylase) requires a PLP-binding KxxK motif and cytosolic localization—neither is present. Choice A (tRNA acetyltransferase) requires an acetyl-CoA binding domain and tRNA interaction surface—absent here. Choice B (geissoschizine reductase) is a cytoplasmic SDR-family enzyme with a YxxxN catalytic motif and a different fold, inconsistent with the mitochondrial targeting and Rossmann architecture. Choice C (quinone→quinol, EC 1.6.5.2) is the canonical reaction of mitochondrial CoQ oxidoreductases, perfectly matching the Rossmann NADH-binding motif and mitochondrial localization. The combination of mitochondrial presequence + Rossmann NAD(P)H motif + absence of PLP/acetyltransferase/SDR features meaningfully distinguishes C from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the mitochondrial targeting sequence and the Rossmann-fold NAD(P)H-binding motif (GGSGGVG) to infer this is a mitochondrial nucleotide-dependent oxidoreductase. The absence of PLP-binding motifs rules out D, absence of acetyltransferase motifs rules out A, and the mitochondrial context plus Rossmann fold (rather than SDR YxxxN fold) rules out B. This leaves C as the most consistent option. The inference relies on general protein-family knowledge (Rossmann fold = NAD(P)H oxidoreductases; mitochondrial CoQ reductases use this architecture) rather than memorizing this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (acetyltransferase, SDR terpenoid reductase, quinone reductase, PLP-decarboxylase) with clearly different structural and cofactor requirements. The sequence features (mitochondrial targeting + Rossmann NAD(P)H motif) cleanly select C and exclude the others.


### Important caveats

- The UniProt annotation for this Drosophila entry uses ECO:0000250 (similarity to human Q8WWV3), not direct experimental evidence on the fly protein itself, though the 2024 Park et al. paper provides functional validation in Drosophila.
- The protein also catalyzes the NADPH-dependent reaction (EC 1.6.5.2 with NADPH), but only the NADH reaction is offered as a choice, so no ambiguity arises from the options.
- The Rossmann motif 'GGSGGVG' is a strong but not absolutely exclusive indicator; however, combined with mitochondrial targeting and the absence of features for the other three enzyme classes, the inference is robust.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits two key transferable features: (1) an N-terminal mitochondrial targeting presequence (MTAAGFNSILCLRQLVRLNRRQ...), indicating a mitochondrial enzyme, and (2) a Rossmann-fold NAD(P)H-binding motif 'GGSGGVGTLAIQ' (the canonical GxGxxG nucleotide-binding pattern). These features together point to a mitochondrial NAD(P)H-dependent oxidoreductase. Choice D (DOPA decarboxylase) requires a PLP-binding KxxK motif and cytosolic localization—neither is present. Choice A (tRNA acetyltransferase) requires an acetyl-CoA binding domain and tRNA interaction surface—absent here. Choice B (geissoschizine reductase) is a cytoplasmic SDR-family enzyme with a YxxxN catalytic motif and a different fold, inconsistent with the mitochondrial targeting and Rossmann architecture. Choice C (quinone→quinol, EC 1.6.5.2) is the canonical reaction of mitochondrial CoQ oxidoreductases, perfectly matching the Rossmann NADH-binding motif and mitochondrial localization. The combination of mitochondrial presequence + Rossmann NAD(P)H motif + absence of PLP/acetyltransferase/SDR features meaningfully distinguishes C from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the mitochondrial targeting sequence and the Rossmann-fold NAD(P)H-binding motif (GGSGGVG) to infer this is a mitochondrial nucleotide-dependent oxidoreductase. The absence of PLP-binding motifs rules out D, absence of acetyltransferase motifs rules out A, and the mitochondrial context plus Rossmann fold (rather than SDR YxxxN fold) rules out B. This leaves C as the most consistent option. The inference relies on general protein-family knowledge (Rossmann fold = NAD(P)H oxidoreductases; mitochondrial CoQ reductases use this architecture) rather than memorizing this specific protein's record."
  },
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8IPZ3 (RTN4IP1_DROME) annotates the catalytic activity as 'a quinone + NADH + H(+) = a quinol + NAD(+)' (EC 1.6.5.2), matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), and a 2024 experimental paper (Park et al., Nat. Chem. Biol. 20:221-233) confirms RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q synthesis. The annotation is supported by both similarity transfer and experimental validation."
  },
  "important_caveats": [
    "The UniProt annotation for this Drosophila entry uses ECO:0000250 (similarity to human Q8WWV3), not direct experimental evidence on the fly protein itself, though the 2024 Park et al. paper provides functional validation in Drosophila.",
    "The protein also catalyzes the NADPH-dependent reaction (EC 1.6.5.2 with NADPH), but only the NADH reaction is offered as a choice, so no ambiguity arises from the options.",
    "The Rossmann motif 'GGSGGVG' is a strong but not absolutely exclusive indicator; however, combined with mitochondrial targeting and the absence of features for the other three enzyme classes, the inference is robust."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acetyltransferase, SDR terpenoid reductase, quinone reductase, PLP-decarboxylase) with clearly different structural and cofactor requirements. The sequence features (mitochondrial targeting + Rossmann NAD(P)H motif) cleanly select C and exclude the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8IPZ3 (RTN4IP1_DROME) annotates the catalytic activity as 'a quinone + NADH + H(+) = a quinol + NAD(+)' (EC 1.6.5.2), matching choice C exactly. The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), and a 2024 experimental paper (Park et al., Nat. Chem. Biol. 20:221-233) confirms RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q synthesis. The annotation is supported by both similarity transfer and experimental validation.",
    "evidence_ids": ["C5", "C7", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits two key transferable features: (1) an N-terminal mitochondrial targeting presequence (MTAAGFNSILCLRQLVRLNRRQ...), indicating a mitochondrial enzyme, and (2) a Rossmann-fold NAD(P)H-binding motif 'GGSGGVGTLAIQ' (the canonical GxGxxG nucleotide-binding pattern). These features together point to a mitochondrial NAD(P)H-dependent oxidoreductase. Choice D (DOPA decarboxylase) requires a PLP-binding KxxK motif and cytosolic localization—neither is present. Choice A (tRNA acetyltransferase) requires an acetyl-CoA binding domain and tRNA interaction surface—absent here. Choice B (geissoschizine reductase) is a cytoplasmic SDR-family enzyme with a YxxxN catalytic motif and a different fold, inconsistent with the mitochondrial targeting and Rossmann architecture. Choice C (quinone→quinol, EC 1.6.5.2) is the canonical reaction of mitochondrial CoQ oxidoreductases, perfectly matching the Rossmann NADH-binding motif and mitochondrial localization. The combination of mitochondrial presequence + Rossmann NAD(P)H motif + absence of PLP/acetyltransferase/SDR features meaningfully distinguishes C from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the mitochondrial targeting sequence and the Rossmann-fold NAD(P)H-binding motif (GGSGGVG) to infer this is a mitochondrial nucleotide-dependent oxidoreductase. The absence of PLP-binding motifs rules out D, absence of acetyltransferase motifs rules out A, and the mitochondrial context plus Rossmann fold (rather than SDR YxxxN fold) rules out B. This leaves C as the most consistent option. The inference relies on general protein-family knowledge (Rossmann fold = NAD(P)H oxidoreductases; mitochondrial CoQ reductases use this architecture) rather than memorizing this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (acetyltransferase, SDR terpenoid reductase, quinone reductase, PLP-decarboxylase) with clearly different structural and cofactor requirements. The sequence features (mitochondrial targeting + Rossmann NAD(P)H motif) cleanly select C and exclude the others."
  },
  "important_caveats": [
    "The UniProt annotation for this Drosophila entry uses ECO:0000250 (similarity to human Q8WWV3), not direct experimental evidence on the fly protein itself, though the 2024 Park et al. paper provides functional validation in Drosophila.",
    "The protein also catalyzes the NADPH-dependent reaction (EC 1.6.5.2 with NADPH), but only the NADH reaction is offered as a choice, so no ambiguity arises from the options.",
    "The Rossmann motif 'GGSGGVG' is a strong but not absolutely exclusive indicator; however, combined with mitochondrial targeting and the absence of features for the other three enzyme classes, the inference is robust."
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
  "benchmark_sequence_length": 413,
  "benchmark_sequence_sha256": "99137aa525ccbf4bc6bd0d532928424a9bf9102dfb71fa5a05d92a378269611d",
  "current_entry_audit": {
    "entryVersion": 180,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 413,
  "current_source_sequence_sha256": "99137aa525ccbf4bc6bd0d532928424a9bf9102dfb71fa5a05d92a378269611d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 178,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IPZ3",
  "selected_historical_entry_version": 178,
  "selected_historical_record_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "selected_historical_source_sequence_length": 413,
  "selected_historical_source_sequence_sha256": "99137aa525ccbf4bc6bd0d532928424a9bf9102dfb71fa5a05d92a378269611d",
  "selected_historical_version": {
    "accession": "Q8IPZ3",
    "database": "Swiss-Prot",
    "entryVersion": 178,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RT4I1_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IPZ3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":180,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Reticulon-4-interacting protein 1 homolog\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37884807\",\"source\":\"PubMed\"}],\"value\":\"dRtn4ip1\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8WWV3\",\"source\":\"UniProtKB\"}],\"value\":\"1.6.5.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"NAD(P)H oxidoreductase RTN4IP1, mitochondrial\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.6.5.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8WWV3\",\"source\":\"UniProtKB\"}],\"name\":\"a quinone + NADH + H(+) = a quinol + NAD(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46160\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.6.5.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8WWV3\",\"source\":\"UniProtKB\"}],\"name\":\"a quinone + NADPH + H(+) = a quinol + NADP(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46164\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:24646\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132124\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IPZ3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Park I.\",\"Kim K.E.\",\"Kim J.\",\"Kim A.K.\",\"Bae S.\",\"Jung M.\",\"Choi J.\",\"Mishra P.K.\",\"Kim T.M.\",\"Kwak C.\",\"Kang M.G.\",\"Yoo C.M.\",\"Mun J.Y.\",\"Liu K.H.\",\"Lee K.S.\",\"Kim J.S.\",\"Suh J.M.\",\"Rhee H.W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37884807\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-023-01452-w\"}],\"citationType\":\"journal article\",\"firstPage\":\"221\",\"id\":\"37884807\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"233\",\"publicationDate\":\"2024\",\"title\":\"Mitochondrial matrix RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q synthesis.\",\"volume\":\"20\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:32:18.576763+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e86069a21d68baee355342320a6ffe2ad016abdc8d4f641d55cad548579f2ea3",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IPZ3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H1",
  "excerpt": "ID   RT4I1_DROME             Reviewed;         413 AA.\nAC   Q8IPZ3; Q8SZK7; Q9VQL4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 178.\nDE   RecName: Full=NAD(P)H oxidoreductase RTN4IP1, mitochondrial {ECO:0000305};\nDE            EC=1.6.5.2 {ECO:0000250|UniProtKB:Q8WWV3};\nDE   AltName: Full=Reticulon-4-interacting protein 1 homolog;\nDE            Short=dRtn4ip1 {ECO:0000303|PubMed:37884807};\nDE   Flags: Precursor;\nGN   Name=Rtn4ip1 {ECO:0000312|FlyBase:FBgn0031500};\nGN   ORFNames=CG17221 {ECO:0000312|FlyBase:FBgn0031500};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.972608+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "url": "https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=NAD(P)H oxidoreductase RTN4IP1, mitochondrial {ECO:0000305};\nDE            EC=1.6.5.2 {ECO:0000250|UniProtKB:Q8WWV3};\nDE   AltName: Full=Reticulon-4-interacting protein 1 homolog;\nDE            Short=dRtn4ip1 {ECO:0000303|PubMed:37884807};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.972608+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "url": "https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H3",
  "excerpt": "RN   [5]\nRP   FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=37884807; DOI=10.1038/s41589-023-01452-w;\nRA   Park I., Kim K.E., Kim J., Kim A.K., Bae S., Jung M., Choi J., Mishra P.K.,\nRA   Kim T.M., Kwak C., Kang M.G., Yoo C.M., Mun J.Y., Liu K.H., Lee K.S.,\nRA   Kim J.S., Suh J.M., Rhee H.W.;\nRT   \"Mitochondrial matrix RTN4IP1/OPA10 is an oxidoreductase for coenzyme Q\nRT   synthesis.\";\nRL   Nat. Chem. Biol. 20:221-233(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.972608+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "url": "https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a quinone + NADH + H(+) = a quinol + NAD(+);\nCC         Xref=Rhea:RHEA:46160, ChEBI:CHEBI:15378, ChEBI:CHEBI:24646,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57945, ChEBI:CHEBI:132124; EC=1.6.5.2;\nCC         Evidence={ECO:0000250|UniProtKB:Q8WWV3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.972608+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 97-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "url": "https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178)

```json
{
  "entry_version": 178,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a quinone + NADPH + H(+) = a quinol + NADP(+);\nCC         Xref=Rhea:RHEA:46164, ChEBI:CHEBI:15378, ChEBI:CHEBI:24646,\nCC         ChEBI:CHEBI:57783, ChEBI:CHEBI:58349, ChEBI:CHEBI:132124; EC=1.6.5.2;\nCC         Evidence={ECO:0000250|UniProtKB:Q8WWV3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:22.972608+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c2044f60ca3ef3b11b8d9eda94d95aa716930f1e71581317ce51caed3192aef1",
  "url": "https://rest.uniprot.org/unisave/Q8IPZ3?format=txt&versions=178"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
