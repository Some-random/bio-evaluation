# EC_number_0026

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0026.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.6.5.2

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
A. 1.5.1.38
B. 2.7.1.52
C. 3.1.1.4
D. 1.6.5.2
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

> The supplied sequence matches the UniProt record annotated as EC 1.6.5.2, with catalytic reactions listed for quinone reduction by NADH and NADPH. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a mitochondrial-targeting-like N-terminus and a glycine-rich dinucleotide-binding region in an enzyme-sized globular protein, supporting a mitochondrial NAD(P)H-dependent oxidoreductase rather than the kinase or lipase choices. More specifically, transferable sequence-family recognition can distinguish an RTN4IP1-like quinone oxidoreductase (D) from the other redox option (A); the generic cofactor-binding motif alone would not make that finer distinction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices are distinct enzyme families, and sequence-family similarity provides a meaningful route to the quinone-oxidoreductase choice without needing the exact protein's database annotation. The inference is probabilistic, and the short motif by itself is not conclusive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although A and D are both oxidoreductase-class choices, the sequence-family inference favors D; the shared broad class does not make both choices equally defensible.


### Important caveats

- The source annotation for this exact sequence is similarity-based, and the reviewer-only evidence does not independently establish direct experimental characterization of the fly protein's reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a mitochondrial-targeting-like N-terminus and a glycine-rich dinucleotide-binding region in an enzyme-sized globular protein, supporting a mitochondrial NAD(P)H-dependent oxidoreductase rather than the kinase or lipase choices. More specifically, transferable sequence-family recognition can distinguish an RTN4IP1-like quinone oxidoreductase (D) from the other redox option (A); the generic cofactor-binding motif alone would not make that finer distinction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are distinct enzyme families, and sequence-family similarity provides a meaningful route to the quinone-oxidoreductase choice without needing the exact protein's database annotation. The inference is probabilistic, and the short motif by itself is not conclusive."
  },
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt record annotated as EC 1.6.5.2, with catalytic reactions listed for quinone reduction by NADH and NADPH. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The source annotation for this exact sequence is similarity-based, and the reviewer-only evidence does not independently establish direct experimental characterization of the fly protein's reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D are both oxidoreductase-class choices, the sequence-family inference favors D; the shared broad class does not make both choices equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the UniProt record annotated as EC 1.6.5.2, with catalytic reactions listed for quinone reduction by NADH and NADPH. The annotation is transferred by similarity (ECO:0000250), so it supports the key but is not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a mitochondrial-targeting-like N-terminus and a glycine-rich dinucleotide-binding region in an enzyme-sized globular protein, supporting a mitochondrial NAD(P)H-dependent oxidoreductase rather than the kinase or lipase choices. More specifically, transferable sequence-family recognition can distinguish an RTN4IP1-like quinone oxidoreductase (D) from the other redox option (A); the generic cofactor-binding motif alone would not make that finer distinction.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices are distinct enzyme families, and sequence-family similarity provides a meaningful route to the quinone-oxidoreductase choice without needing the exact protein's database annotation. The inference is probabilistic, and the short motif by itself is not conclusive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D are both oxidoreductase-class choices, the sequence-family inference favors D; the shared broad class does not make both choices equally defensible."
  },
  "important_caveats": [
    "The source annotation for this exact sequence is similarity-based, and the reviewer-only evidence does not independently establish direct experimental characterization of the fly protein's reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates Q8IPZ3 (RTN4IP1, Drosophila) with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), not direct experimental evidence on this exact protein. However, a 2024 Nat. Chem. Biol. paper (Park et al., PMID 37884807) experimentally demonstrated RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, providing functional support. The catalytic reactions listed (quinone + NADH/NADPH → quinol + NAD+/NADP+) are consistent with EC 1.6.5.2. The annotation is database-supported with indirect experimental backing.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence shows (1) an N-terminal mitochondrial targeting signal (MTAAGFNSILC...), (2) a Rossmann-fold-like glycine-rich motif (GGSGGVGTLAIQ) characteristic of NAD(P)H-binding oxidoreductases, and (3) overall length (~413 aa) consistent with a small mitochondrial flavoprotein/oxidoreductase. These features immediately eliminate class 2 (transferase, 2.7.1.52 thiamine kinase) and class 3 (hydrolase, 3.1.1.4 carboxylesterase), as no kinase catalytic motifs or serine-hydrolase GxSxG triad are present. Between the two class-1 options: 1.5.1.38 (dihydrofolate reductase-like, acting on CH-NH donors) and 1.6.5.2 (NAD(P)H:quinone oxidoreductase), the mitochondrial localization strongly favors quinone metabolism (coenzyme Q is a mitochondrial membrane quinone), and general knowledge of mitochondrial NAD(P)H:quinone oxidoreductases (e.g., NQO2, complex I subunits, FDXR) provides a family-level analogy. The combination of mitochondrial targeting + NAD(P)H-binding motif + quinone context distinguishes 1.6.5.2 from 1.5.1.38, which typically acts on folate-type substrates in cytosolic/nuclear contexts.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the visible mitochondrial targeting sequence, the Rossmann-fold glycine-rich motif, elimination of non-oxidoreductase classes, and general knowledge about mitochondrial quinone oxidoreductases to arrive at 1.6.5.2 without needing the specific UniProt annotation of Q8IPZ3. The inference relies on transferable sequence-feature recognition and family-level biology of mitochondrial oxidoreductases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (kinase) and C (hydrolase) are clearly inconsistent with the observed sequence features. Option A (1.5.1.38, dihydrofolate reductase-like) is less favored because it acts on CH-NH group donors (folate analogs) typically in cytosolic contexts, whereas the mitochondrial targeting and NAD(P)H-binding motif align with quinone oxidoreductase activity. No other option is equally defensible.


### Important caveats

- The UniProt EC annotation uses evidence code ECO:0000250 (similarity to human ortholog Q8WWV3), not direct experimental evidence on this exact Drosophila protein.
- The 2024 Nat. Chem. Biol. paper supports oxidoreductase function in coenzyme Q synthesis but the exact EC assignment (1.6.5.2) is still primarily transferred from the human ortholog annotation.
- Distinguishing 1.6.5.2 from 1.5.1.38 relies on mitochondrial context and general quinone-metabolism knowledge; without the mitochondrial targeting signal, the distinction would be less clear.
- The sequence was integrated into Swiss-Prot only in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence shows (1) an N-terminal mitochondrial targeting signal (MTAAGFNSILC...), (2) a Rossmann-fold-like glycine-rich motif (GGSGGVGTLAIQ) characteristic of NAD(P)H-binding oxidoreductases, and (3) overall length (~413 aa) consistent with a small mitochondrial flavoprotein/oxidoreductase. These features immediately eliminate class 2 (transferase, 2.7.1.52 thiamine kinase) and class 3 (hydrolase, 3.1.1.4 carboxylesterase), as no kinase catalytic motifs or serine-hydrolase GxSxG triad are present. Between the two class-1 options: 1.5.1.38 (dihydrofolate reductase-like, acting on CH-NH donors) and 1.6.5.2 (NAD(P)H:quinone oxidoreductase), the mitochondrial localization strongly favors quinone metabolism (coenzyme Q is a mitochondrial membrane quinone), and general knowledge of mitochondrial NAD(P)H:quinone oxidoreductases (e.g., NQO2, complex I subunits, FDXR) provides a family-level analogy. The combination of mitochondrial targeting + NAD(P)H-binding motif + quinone context distinguishes 1.6.5.2 from 1.5.1.38, which typically acts on folate-type substrates in cytosolic/nuclear contexts.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the visible mitochondrial targeting sequence, the Rossmann-fold glycine-rich motif, elimination of non-oxidoreductase classes, and general knowledge about mitochondrial quinone oxidoreductases to arrive at 1.6.5.2 without needing the specific UniProt annotation of Q8IPZ3. The inference relies on transferable sequence-feature recognition and family-level biology of mitochondrial oxidoreductases."
  },
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates Q8IPZ3 (RTN4IP1, Drosophila) with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), not direct experimental evidence on this exact protein. However, a 2024 Nat. Chem. Biol. paper (Park et al., PMID 37884807) experimentally demonstrated RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, providing functional support. The catalytic reactions listed (quinone + NADH/NADPH → quinol + NAD+/NADP+) are consistent with EC 1.6.5.2. The annotation is database-supported with indirect experimental backing."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000250 (similarity to human ortholog Q8WWV3), not direct experimental evidence on this exact Drosophila protein.",
    "The 2024 Nat. Chem. Biol. paper supports oxidoreductase function in coenzyme Q synthesis but the exact EC assignment (1.6.5.2) is still primarily transferred from the human ortholog annotation.",
    "Distinguishing 1.6.5.2 from 1.5.1.38 relies on mitochondrial context and general quinone-metabolism knowledge; without the mitochondrial targeting signal, the distinction would be less clear.",
    "The sequence was integrated into Swiss-Prot only in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (kinase) and C (hydrolase) are clearly inconsistent with the observed sequence features. Option A (1.5.1.38, dihydrofolate reductase-like) is less favored because it acts on CH-NH group donors (folate analogs) typically in cytosolic contexts, whereas the mitochondrial targeting and NAD(P)H-binding motif align with quinone oxidoreductase activity. No other option is equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates Q8IPZ3 (RTN4IP1, Drosophila) with EC 1.6.5.2 (NAD(P)H:quinone oxidoreductase). The evidence code is ECO:0000250 (inferred by similarity to human Q8WWV3), not direct experimental evidence on this exact protein. However, a 2024 Nat. Chem. Biol. paper (Park et al., PMID 37884807) experimentally demonstrated RTN4IP1/OPA10 as an oxidoreductase in coenzyme Q synthesis, providing functional support. The catalytic reactions listed (quinone + NADH/NADPH → quinol + NAD+/NADP+) are consistent with EC 1.6.5.2. The annotation is database-supported with indirect experimental backing.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence shows (1) an N-terminal mitochondrial targeting signal (MTAAGFNSILC...), (2) a Rossmann-fold-like glycine-rich motif (GGSGGVGTLAIQ) characteristic of NAD(P)H-binding oxidoreductases, and (3) overall length (~413 aa) consistent with a small mitochondrial flavoprotein/oxidoreductase. These features immediately eliminate class 2 (transferase, 2.7.1.52 thiamine kinase) and class 3 (hydrolase, 3.1.1.4 carboxylesterase), as no kinase catalytic motifs or serine-hydrolase GxSxG triad are present. Between the two class-1 options: 1.5.1.38 (dihydrofolate reductase-like, acting on CH-NH donors) and 1.6.5.2 (NAD(P)H:quinone oxidoreductase), the mitochondrial localization strongly favors quinone metabolism (coenzyme Q is a mitochondrial membrane quinone), and general knowledge of mitochondrial NAD(P)H:quinone oxidoreductases (e.g., NQO2, complex I subunits, FDXR) provides a family-level analogy. The combination of mitochondrial targeting + NAD(P)H-binding motif + quinone context distinguishes 1.6.5.2 from 1.5.1.38, which typically acts on folate-type substrates in cytosolic/nuclear contexts.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the visible mitochondrial targeting sequence, the Rossmann-fold glycine-rich motif, elimination of non-oxidoreductase classes, and general knowledge about mitochondrial quinone oxidoreductases to arrive at 1.6.5.2 without needing the specific UniProt annotation of Q8IPZ3. The inference relies on transferable sequence-feature recognition and family-level biology of mitochondrial oxidoreductases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (kinase) and C (hydrolase) are clearly inconsistent with the observed sequence features. Option A (1.5.1.38, dihydrofolate reductase-like) is less favored because it acts on CH-NH group donors (folate analogs) typically in cytosolic contexts, whereas the mitochondrial targeting and NAD(P)H-binding motif align with quinone oxidoreductase activity. No other option is equally defensible."
  },
  "important_caveats": [
    "The UniProt EC annotation uses evidence code ECO:0000250 (similarity to human ortholog Q8WWV3), not direct experimental evidence on this exact Drosophila protein.",
    "The 2024 Nat. Chem. Biol. paper supports oxidoreductase function in coenzyme Q synthesis but the exact EC assignment (1.6.5.2) is still primarily transferred from the human ortholog annotation.",
    "Distinguishing 1.6.5.2 from 1.5.1.38 relies on mitochondrial context and general quinone-metabolism knowledge; without the mitochondrial targeting signal, the distinction would be less clear.",
    "The sequence was integrated into Swiss-Prot only in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
