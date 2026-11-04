# catalytic_activity_0164

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0164.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNKVKVGDAQVSYCIDGKGPGLVLVHGTGGDSETNWGHLMPALTNDWTVVRPDYSGSGITSDEGKQLEVKEIAAQVVAAAEAARVVPFDLVGFSLGSAVVIAIAADYPHLVRRIVLLGAFLSSRDIRQKTQFELWRDLIRTDRAALSRLILLTGFSPDFISKQGHDGVSVIINSFVSEINWEGMARQVELDLSIDVSEAARRIEKPTLVIGCSHDHIVPSSQAKSVVRIIRGAQYTELHTGHLAHIENPEEFILLLRSFLLSEDVP

[Multiple Choices]
A. L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)
B. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
C. L-methionine + H2O = methanethiol + 2-oxobutanoate + NH4(+)
D. Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.
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

> The sequence matches the annotated protein, and the matched UniProt record reports this catalytic reaction with ECO:0000269 evidence linked to a publication. This supports choice B, although the supplied excerpt does not include the underlying assay details.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GxSxG-like motif (GFSLG), a transferable hallmark of many serine hydrolases. That makes an acyl-hydrolysis reaction such as the deacetylation in B plausible. The alternatives describe protein phosphorylation, PLP-dependent methionine cleavage, or a viral polyprotein processing event; the sequence offers no comparable kinase or viral-polyprotein context, and C is a different reaction class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The motif supports a hydrolase-class inference that meaningfully distinguishes B among these choices, without establishing the exact unusual substrate solely from sequence. The alternatives are sufficiently distinct that this limitation does not make the choice lookup-dependent.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction is comparably supported by the sequence-level hydrolase inference.


### Important caveats

- A GxSxG-like motif supports a hydrolase inference but does not by itself establish the enzyme's exact substrate or products.
- The annotation cites experimental evidence, but the primary study and assay details were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GxSxG-like motif (GFSLG), a transferable hallmark of many serine hydrolases. That makes an acyl-hydrolysis reaction such as the deacetylation in B plausible. The alternatives describe protein phosphorylation, PLP-dependent methionine cleavage, or a viral polyprotein processing event; the sequence offers no comparable kinase or viral-polyprotein context, and C is a different reaction class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The motif supports a hydrolase-class inference that meaningfully distinguishes B among these choices, without establishing the exact unusual substrate solely from sequence. The alternatives are sufficiently distinct that this limitation does not make the choice lookup-dependent."
  },
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the matched UniProt record reports this catalytic reaction with ECO:0000269 evidence linked to a publication. This supports choice B, although the supplied excerpt does not include the underlying assay details."
  },
  "important_caveats": [
    "A GxSxG-like motif supports a hydrolase inference but does not by itself establish the enzyme's exact substrate or products.",
    "The annotation cites experimental evidence, but the primary study and assay details were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence-level hydrolase inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the matched UniProt record reports this catalytic reaction with ECO:0000269 evidence linked to a publication. This supports choice B, although the supplied excerpt does not include the underlying assay details.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GxSxG-like motif (GFSLG), a transferable hallmark of many serine hydrolases. That makes an acyl-hydrolysis reaction such as the deacetylation in B plausible. The alternatives describe protein phosphorylation, PLP-dependent methionine cleavage, or a viral polyprotein processing event; the sequence offers no comparable kinase or viral-polyprotein context, and C is a different reaction class.",
    "missing_item_specific_fact": "",
    "reason": "The motif supports a hydrolase-class inference that meaningfully distinguishes B among these choices, without establishing the exact unusual substrate solely from sequence. The alternatives are sufficiently distinct that this limitation does not make the choice lookup-dependent."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably supported by the sequence-level hydrolase inference."
  },
  "important_caveats": [
    "A GxSxG-like motif supports a hydrolase inference but does not by itself establish the enzyme's exact substrate or products.",
    "The annotation cites experimental evidence, but the primary study and assay details were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C4, C5, H2, H4) confirms UniProt entry A0A2G0QDP0 is annotated as 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-) with the exact catalytic reaction: pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+). The evidence code is ECO:0000269 (experimental, PubMed:39428351) and is corroborated by a 1.18 Å X-ray crystal structure (PDB 8QZU) with acetate in the active site. The sequence in the benchmark matches the source entry exactly (SHA-256 match, 266 aa).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two hallmark motifs of the Ntn (N-terminal nucleophile) hydrolase superfamily: a 'GTGGDS' motif near position 17-22 (the autocatalytic Ser nucleophile) and a 'GCSHDH' motif near the C-terminus. This superfamily (penicillin G acylase, glutamine amidotransferases, cephalosporin C acylase, various deacylases) is defined by catalyzing hydrolysis of amide bonds via the N-terminal nucleophile. Among the four options: (A) is a protein kinase requiring ATP and a kinase fold (Gly-rich loop, HRD, DFG motifs absent here); (C) is a PLP-dependent γ-lyase with a fold-type I aminotransferase architecture (no PLP-binding Lys motif present); (D) is a ~120-residue chymotrypsin-like alphavirus capsid protease with a His-Asp-Ser triad in a trypsin fold, incompatible with a 266-aa Ntn-hydrolase. Option B describes hydrolysis of an amide (acetamide) bond releasing acetate — exactly the reaction class performed by Ntn-hydrolase deacylases. The model need not recognize the exotic substrate name; it only needs to match the fold to the reaction type (amide hydrolysis), which uniquely selects B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Ntn-hydrolase fold is a well-characterized superfamily with a conserved catalytic mechanism (N-terminal Ser nucleophile after autocatalytic processing). Recognizing GTGGDS and GCSHDH motifs allows family assignment, and the known family function (amide-bond hydrolysis) eliminates A (kinase), C (PLP-lyase), and D (chymotrypsin-like protease), leaving B as the only hydrolysis-of-amide option consistent with the fold. This is a legitimate family-level inference from conserved sequence features and superfamily-level functional knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four entirely distinct enzyme classes/folds (kinase, deacetylase/hydrolase, PLP-lyase, chymotrypsin-like protease). The Ntn-hydrolase motifs unambiguously point to a hydrolysis enzyme, and only B fits both the reaction type and the fold. No two options are defensible.


### Important caveats

- The specific substrate 'pyrrolizixenacetamide' is a recently characterized bacterial alkaloid intermediate (2024 paper); a model would not know this compound by name but can still identify the reaction type (amide hydrolysis) from the fold.
- The Ntn-hydrolase annotation is supported by experimental evidence (ECO:0000269) and a high-resolution crystal structure, not merely computational prediction.
- The benchmark sequence matches the UniProt entry exactly (266 aa, SHA-256 confirmed), so no isoform or construct ambiguity exists.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two hallmark motifs of the Ntn (N-terminal nucleophile) hydrolase superfamily: a 'GTGGDS' motif near position 17-22 (the autocatalytic Ser nucleophile) and a 'GCSHDH' motif near the C-terminus. This superfamily (penicillin G acylase, glutamine amidotransferases, cephalosporin C acylase, various deacylases) is defined by catalyzing hydrolysis of amide bonds via the N-terminal nucleophile. Among the four options: (A) is a protein kinase requiring ATP and a kinase fold (Gly-rich loop, HRD, DFG motifs absent here); (C) is a PLP-dependent γ-lyase with a fold-type I aminotransferase architecture (no PLP-binding Lys motif present); (D) is a ~120-residue chymotrypsin-like alphavirus capsid protease with a His-Asp-Ser triad in a trypsin fold, incompatible with a 266-aa Ntn-hydrolase. Option B describes hydrolysis of an amide (acetamide) bond releasing acetate — exactly the reaction class performed by Ntn-hydrolase deacylases. The model need not recognize the exotic substrate name; it only needs to match the fold to the reaction type (amide hydrolysis), which uniquely selects B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Ntn-hydrolase fold is a well-characterized superfamily with a conserved catalytic mechanism (N-terminal Ser nucleophile after autocatalytic processing). Recognizing GTGGDS and GCSHDH motifs allows family assignment, and the known family function (amide-bond hydrolysis) eliminates A (kinase), C (PLP-lyase), and D (chymotrypsin-like protease), leaving B as the only hydrolysis-of-amide option consistent with the fold. This is a legitimate family-level inference from conserved sequence features and superfamily-level functional knowledge."
  },
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms UniProt entry A0A2G0QDP0 is annotated as 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-) with the exact catalytic reaction: pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+). The evidence code is ECO:0000269 (experimental, PubMed:39428351) and is corroborated by a 1.18 Å X-ray crystal structure (PDB 8QZU) with acetate in the active site. The sequence in the benchmark matches the source entry exactly (SHA-256 match, 266 aa)."
  },
  "important_caveats": [
    "The specific substrate 'pyrrolizixenacetamide' is a recently characterized bacterial alkaloid intermediate (2024 paper); a model would not know this compound by name but can still identify the reaction type (amide hydrolysis) from the fold.",
    "The Ntn-hydrolase annotation is supported by experimental evidence (ECO:0000269) and a high-resolution crystal structure, not merely computational prediction.",
    "The benchmark sequence matches the UniProt entry exactly (266 aa, SHA-256 confirmed), so no isoform or construct ambiguity exists."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four entirely distinct enzyme classes/folds (kinase, deacetylase/hydrolase, PLP-lyase, chymotrypsin-like protease). The Ntn-hydrolase motifs unambiguously point to a hydrolysis enzyme, and only B fits both the reaction type and the fold. No two options are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms UniProt entry A0A2G0QDP0 is annotated as 'Pyrrolizixenacetamide deacetylase' (EC 3.5.1.-) with the exact catalytic reaction: pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+). The evidence code is ECO:0000269 (experimental, PubMed:39428351) and is corroborated by a 1.18 Å X-ray crystal structure (PDB 8QZU) with acetate in the active site. The sequence in the benchmark matches the source entry exactly (SHA-256 match, 266 aa).",
    "evidence_ids": ["C4", "C5", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two hallmark motifs of the Ntn (N-terminal nucleophile) hydrolase superfamily: a 'GTGGDS' motif near position 17-22 (the autocatalytic Ser nucleophile) and a 'GCSHDH' motif near the C-terminus. This superfamily (penicillin G acylase, glutamine amidotransferases, cephalosporin C acylase, various deacylases) is defined by catalyzing hydrolysis of amide bonds via the N-terminal nucleophile. Among the four options: (A) is a protein kinase requiring ATP and a kinase fold (Gly-rich loop, HRD, DFG motifs absent here); (C) is a PLP-dependent γ-lyase with a fold-type I aminotransferase architecture (no PLP-binding Lys motif present); (D) is a ~120-residue chymotrypsin-like alphavirus capsid protease with a His-Asp-Ser triad in a trypsin fold, incompatible with a 266-aa Ntn-hydrolase. Option B describes hydrolysis of an amide (acetamide) bond releasing acetate — exactly the reaction class performed by Ntn-hydrolase deacylases. The model need not recognize the exotic substrate name; it only needs to match the fold to the reaction type (amide hydrolysis), which uniquely selects B.",
    "missing_item_specific_fact": "",
    "reason": "The Ntn-hydrolase fold is a well-characterized superfamily with a conserved catalytic mechanism (N-terminal Ser nucleophile after autocatalytic processing). Recognizing GTGGDS and GCSHDH motifs allows family assignment, and the known family function (amide-bond hydrolysis) eliminates A (kinase), C (PLP-lyase), and D (chymotrypsin-like protease), leaving B as the only hydrolysis-of-amide option consistent with the fold. This is a legitimate family-level inference from conserved sequence features and superfamily-level functional knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four entirely distinct enzyme classes/folds (kinase, deacetylase/hydrolase, PLP-lyase, chymotrypsin-like protease). The Ntn-hydrolase motifs unambiguously point to a hydrolysis enzyme, and only B fits both the reaction type and the fold. No two options are defensible."
  },
  "important_caveats": [
    "The specific substrate 'pyrrolizixenacetamide' is a recently characterized bacterial alkaloid intermediate (2024 paper); a model would not know this compound by name but can still identify the reaction type (amide hydrolysis) from the fold.",
    "The Ntn-hydrolase annotation is supported by experimental evidence (ECO:0000269) and a high-resolution crystal structure, not merely computational prediction.",
    "The benchmark sequence matches the UniProt entry exactly (266 aa, SHA-256 confirmed), so no isoform or construct ambiguity exists."
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
  "benchmark_sequence_length": 266,
  "benchmark_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 266,
  "current_source_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2G0QDP0",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "selected_historical_source_sequence_length": 266,
  "selected_historical_source_sequence_sha256": "db237f760869551b09464ba4867169aafc47d9b85d114228f62281edb6b9c76d",
  "selected_historical_version": {
    "accession": "A0A2G0QDP0",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XHPG_XENHO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2G0QDP0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Morganellaceae\",\"Xenorhabdus\"],\"scientificName\":\"Xenorhabdus hominickii\",\"taxonId\":351679}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolizixenamide hydrolase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"3.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolizixenacetamide deacetylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83308\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"name\":\"pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83307\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232461\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:232462\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Effert J.\",\"Westphalen M.\",\"Calderari A.\",\"Shi Y.M.\",\"Elamri I.\",\"Najah S.\",\"Gruen P.\",\"Li Y.\",\"Gruez A.\",\"Weissman K.J.\",\"Bode H.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39428351\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.202411258\"}],\"citationType\":\"journal article\",\"firstPage\":\"e202411258\",\"id\":\"39428351\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"e202411258\",\"publicationDate\":\"2024\",\"title\":\"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.\",\"volume\":\"63\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QZU\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 17903 / CIP 109072 / KE01\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH ACETATE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF ASN-35 AND SER-94\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:47.833416+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ae3334cfc3b11f2536437c9d5e79945575a56544d5415a430b401730b6c628d9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDP0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   XHPG_XENHO              Reviewed;         266 AA.\nAC   A0A2G0QDP0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Pyrrolizixenacetamide deacetylase {ECO:0000305|PubMed:39428351};\nDE            EC=3.5.1.- {ECO:0000269|PubMed:39428351};\nDE   AltName: Full=Pyrrolizixenamide hydrolase {ECO:0000303|PubMed:39428351};\nGN   Name=xhpG {ECO:0000303|PubMed:39428351};\nGN   ORFNames=Xhom_00310 {ECO:0000312|EMBL:PHM57344.1};\nOS   Xenorhabdus hominickii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Morganellaceae; Xenorhabdus.\nOX   NCBI_TaxID=351679;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Pyrrolizixenacetamide deacetylase {ECO:0000305|PubMed:39428351};\nDE            EC=3.5.1.- {ECO:0000269|PubMed:39428351};\nDE   AltName: Full=Pyrrolizixenamide hydrolase {ECO:0000303|PubMed:39428351};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8QZU}\nRP   X-RAY CRYSTALLOGRAPHY (1.18 ANGSTROMS) OF MUTANT ALA-94 IN COMPLEX WITH\nRP   ACETATE, FUNCTION, CATALYTIC ACTIVITY, DISRUPTION PHENOTYPE, SUBUNIT,\nRP   ACTIVE SITE, AND MUTAGENESIS OF ASN-35 AND SER-94.\nRC   STRAIN=DSM 17903 / CIP 109072 / KE01;\nRX   PubMed=39428351; DOI=10.1002/anie.202411258;\nRA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,\nRA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;\nRT   \"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal\nRT   peptide synthetase and non-enzymatic dimerization.\";\nRL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-\nCC         pyrrolizin-1-one + acetate + H(+); Xref=Rhea:RHEA:83307,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30089,\nCC         ChEBI:CHEBI:232461, ChEBI:CHEBI:232462;\nCC         Evidence={ECO:0000269|PubMed:39428351};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83308;\nCC         Evidence={ECO:0000269|PubMed:39428351};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:49.959052+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d0bca0810bb663b04edc4dd649d45e97b5536f59d4132847e0dc79e272689d14",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDP0?format=txt&versions=28"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
