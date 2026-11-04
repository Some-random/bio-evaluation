# pathway_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0028.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEELTRSLVNDVEVLNNHFVSTGHPLPSFDRHTPTVVLPNDASPDAHAARERILDNALRLFQLAAGPSAYLLNLQTGYQYASCVRWLCHFQIFHLVPLEGSIAYADLAVLAKAPEPQLISVVRMAMTNGLFLESPPQHLAHSATSALLRNDADFHDWAVTMSDLSFPTAFAMVEAHERWPNSVEGNQTAYNIAVGSELPFFSHLAEQSDRKRQFAGFMRSMARSQGTDVEKLAEGWDWAALGQACVVDVGGSTGHTSVALARKYPDLNFVVEDLPEVVAEGPGYLSYLDDAQDLKSRIGYRAHSFFDPQPVQDADVYMLRMILHNWSFDDCVRILSRLVQTLKPGARIIIVDIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA

[Multiple Choices]
A. Polyketide biosynthesis. .
B. Antibiotic biosynthesis. .
C. Secondary metabolite biosynthesis. .
D. One-carbon metabolism
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation assigns the protein to secondary metabolite biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it does not establish that this is the only useful level of pathway description.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a methyltransferase, and methyltransferases can act as tailoring enzymes in secondary metabolism. That provides a plausible broad hypothesis and makes one-carbon metabolism less compelling, but methyltransferase family recognition alone does not identify the substrate or distinguish a general secondary-metabolite role from a specific polyketide or antibiotic pathway.


**Missing item-specific fact**

> The protein's substrate or experimentally established pathway association is needed to resolve its particular role among the offered, overlapping pathway labels.


**Reason**

> Transferable enzyme-family knowledge suggests possible secondary-metabolite involvement but does not meaningfully select C over the more specific secondary-metabolism choices A or B. Resolving the particular pathway requires information specific to this protein that is absent from the sequence input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Polyketide biosynthesis is a form of secondary metabolite biosynthesis, so A and C can both describe the pathway at different levels of specificity. The choices do not state whether the broad category or a more specific pathway label is intended.


### Important caveats

- The source evidence supports the author's broad pathway annotation but does not make the choices mutually exclusive.
- The reviewer-only protein identity and pathway annotation are not treated as information available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a methyltransferase, and methyltransferases can act as tailoring enzymes in secondary metabolism. That provides a plausible broad hypothesis and makes one-carbon metabolism less compelling, but methyltransferase family recognition alone does not identify the substrate or distinguish a general secondary-metabolite role from a specific polyketide or antibiotic pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate or experimentally established pathway association is needed to resolve its particular role among the offered, overlapping pathway labels.",
    "reason": "Transferable enzyme-family knowledge suggests possible secondary-metabolite involvement but does not meaningfully select C over the more specific secondary-metabolism choices A or B. Resolving the particular pathway requires information specific to this protein that is absent from the sequence input."
  },
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns the protein to secondary metabolite biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it does not establish that this is the only useful level of pathway description."
  },
  "important_caveats": [
    "The source evidence supports the author's broad pathway annotation but does not make the choices mutually exclusive.",
    "The reviewer-only protein identity and pathway annotation are not treated as information available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Polyketide biosynthesis is a form of secondary metabolite biosynthesis, so A and C can both describe the pathway at different levels of specificity. The choices do not state whether the broad category or a more specific pathway label is intended."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns the protein to secondary metabolite biosynthesis and cites experimental evidence (ECO:0000269). This supports choice C, though it does not establish that this is the only useful level of pathway description.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a methyltransferase, and methyltransferases can act as tailoring enzymes in secondary metabolism. That provides a plausible broad hypothesis and makes one-carbon metabolism less compelling, but methyltransferase family recognition alone does not identify the substrate or distinguish a general secondary-metabolite role from a specific polyketide or antibiotic pathway.",
    "missing_item_specific_fact": "The protein's substrate or experimentally established pathway association is needed to resolve its particular role among the offered, overlapping pathway labels.",
    "reason": "Transferable enzyme-family knowledge suggests possible secondary-metabolite involvement but does not meaningfully select C over the more specific secondary-metabolism choices A or B. Resolving the particular pathway requires information specific to this protein that is absent from the sequence input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Polyketide biosynthesis is a form of secondary metabolite biosynthesis, so A and C can both describe the pathway at different levels of specificity. The choices do not state whether the broad category or a more specific pathway label is intended."
  },
  "important_caveats": [
    "The source evidence supports the author's broad pathway annotation but does not make the choices mutually exclusive.",
    "The reviewer-only protein identity and pathway annotation are not treated as information available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2TXQ9 (AOIF_ASPOR) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:22447538). The protein is O-methyltransferase aoiF (EC 2.1.1.-) from Aspergillus oryzae, confirmed by a 2012 ChemBioChem paper showing it participates in a silent biosynthetic pathway producing a novel polyketide. The answer C matches the database annotation directly.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear SAM-dependent methyltransferase signature: the 'GGSTG' motif (residues ~245-249) is a hallmark of the Class I methyltransferase (Rossmann-fold) SAM-binding motif, and the overall domain architecture (N-terminal region + C-terminal catalytic core with 'DIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA') matches O-methyltransferases. This rules out D (one-carbon metabolism), whose methyltransferases (e.g., methionine synthase, MTHFR, glycine N-methyltransferase) have distinctly different domain architectures (cobalamin-binding, folate-binding, or different Rossmann arrangements). The protein lacks any polyketide synthase (PKS) domains (no KS, AT, ACP, KR, DH, ER modules) and lacks NRPS domains, so it is a tailoring enzyme rather than a core biosynthetic scaffold. For tailoring methyltransferases in fungal natural-product gene clusters, the well-established pattern (learned from many fungal O-methyltransferases in secondary metabolite clusters) is that they are annotated under the broad 'Secondary metabolite biosynthesis' pathway rather than the narrower 'Polyketide biosynthesis,' because the methyltransferase itself does not perform polyketide chain assembly. This distinguishes C from A. B (Antibiotic biosynthesis) is a further subset requiring evidence of antimicrobial activity, which is not inferable from a methyltransferase sequence alone. Thus, the methyltransferase domain identity plus the absence of PKS/NRPS core domains plus the general pattern of fungal tailoring methyltransferases in secondary metabolite clusters supports C as the most defensible choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the SAM-methyltransferase fold from the GGSTG motif and domain organization, rule out one-carbon metabolism by comparing to known folate/methionine-cycle methyltransferase architectures, and apply the general pattern that tailoring methyltransferases in fungal biosynthetic gene clusters are classified under secondary metabolite biosynthesis broadly. The absence of PKS core domains weakens A relative to C. This is a legitimate family-level and mechanistic inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The protein is in fact a tailoring O-methyltransferase in a polyketide biosynthetic pathway (the 2012 paper describes a novel polyketide). Thus 'Polyketide biosynthesis' (A) is factually accurate for this protein's pathway. 'Secondary metabolite biosynthesis' (C) is the broader UniProt annotation and is also accurate. Without the specific pathway context, a model could reasonably argue for A if it recognized the protein as a methyltransferase acting on a polyketide intermediate. The distinction between A and C depends on whether one treats the pathway as the specific polyketide route or the broader secondary metabolite category. The UniProt annotation resolves this in favor of C, but the question wording does not clearly exclude A.


### Important caveats

- The distinction between A (Polyketide biosynthesis) and C (Secondary metabolite biosynthesis) is a taxonomy-of-pathways issue: polyketide biosynthesis is a subset of secondary metabolite biosynthesis. The UniProt annotation uses the broader term, but the specific pathway IS polyketide biosynthesis.
- The methyltransferase identification from sequence is robust (GGSTG motif, domain architecture), but the specific pathway assignment (polyketide vs. other secondary metabolite) cannot be determined from the methyltransferase sequence alone without pathway context.
- The evidence for the pathway annotation is experimental (ECO:0000269) from a 2012 paper, not purely computational inference.
- The organism (Aspergillus oryzae) is not provided in the original input; the fungal secondary metabolite cluster context is inferred from general knowledge of fungal methyltransferases, which is permitted transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear SAM-dependent methyltransferase signature: the 'GGSTG' motif (residues ~245-249) is a hallmark of the Class I methyltransferase (Rossmann-fold) SAM-binding motif, and the overall domain architecture (N-terminal region + C-terminal catalytic core with 'DIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA') matches O-methyltransferases. This rules out D (one-carbon metabolism), whose methyltransferases (e.g., methionine synthase, MTHFR, glycine N-methyltransferase) have distinctly different domain architectures (cobalamin-binding, folate-binding, or different Rossmann arrangements). The protein lacks any polyketide synthase (PKS) domains (no KS, AT, ACP, KR, DH, ER modules) and lacks NRPS domains, so it is a tailoring enzyme rather than a core biosynthetic scaffold. For tailoring methyltransferases in fungal natural-product gene clusters, the well-established pattern (learned from many fungal O-methyltransferases in secondary metabolite clusters) is that they are annotated under the broad 'Secondary metabolite biosynthesis' pathway rather than the narrower 'Polyketide biosynthesis,' because the methyltransferase itself does not perform polyketide chain assembly. This distinguishes C from A. B (Antibiotic biosynthesis) is a further subset requiring evidence of antimicrobial activity, which is not inferable from a methyltransferase sequence alone. Thus, the methyltransferase domain identity plus the absence of PKS/NRPS core domains plus the general pattern of fungal tailoring methyltransferases in secondary metabolite clusters supports C as the most defensible choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the SAM-methyltransferase fold from the GGSTG motif and domain organization, rule out one-carbon metabolism by comparing to known folate/methionine-cycle methyltransferase architectures, and apply the general pattern that tailoring methyltransferases in fungal biosynthetic gene clusters are classified under secondary metabolite biosynthesis broadly. The absence of PKS core domains weakens A relative to C. This is a legitimate family-level and mechanistic inference."
  },
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2TXQ9 (AOIF_ASPOR) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:22447538). The protein is O-methyltransferase aoiF (EC 2.1.1.-) from Aspergillus oryzae, confirmed by a 2012 ChemBioChem paper showing it participates in a silent biosynthetic pathway producing a novel polyketide. The answer C matches the database annotation directly."
  },
  "important_caveats": [
    "The distinction between A (Polyketide biosynthesis) and C (Secondary metabolite biosynthesis) is a taxonomy-of-pathways issue: polyketide biosynthesis is a subset of secondary metabolite biosynthesis. The UniProt annotation uses the broader term, but the specific pathway IS polyketide biosynthesis.",
    "The methyltransferase identification from sequence is robust (GGSTG motif, domain architecture), but the specific pathway assignment (polyketide vs. other secondary metabolite) cannot be determined from the methyltransferase sequence alone without pathway context.",
    "The evidence for the pathway annotation is experimental (ECO:0000269) from a 2012 paper, not purely computational inference.",
    "The organism (Aspergillus oryzae) is not provided in the original input; the fungal secondary metabolite cluster context is inferred from general knowledge of fungal methyltransferases, which is permitted transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The protein is in fact a tailoring O-methyltransferase in a polyketide biosynthetic pathway (the 2012 paper describes a novel polyketide). Thus 'Polyketide biosynthesis' (A) is factually accurate for this protein's pathway. 'Secondary metabolite biosynthesis' (C) is the broader UniProt annotation and is also accurate. Without the specific pathway context, a model could reasonably argue for A if it recognized the protein as a methyltransferase acting on a polyketide intermediate. The distinction between A and C depends on whether one treats the pathway as the specific polyketide route or the broader secondary metabolite category. The UniProt annotation resolves this in favor of C, but the question wording does not clearly exclude A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2TXQ9 (AOIF_ASPOR) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:22447538). The protein is O-methyltransferase aoiF (EC 2.1.1.-) from Aspergillus oryzae, confirmed by a 2012 ChemBioChem paper showing it participates in a silent biosynthetic pathway producing a novel polyketide. The answer C matches the database annotation directly.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear SAM-dependent methyltransferase signature: the 'GGSTG' motif (residues ~245-249) is a hallmark of the Class I methyltransferase (Rossmann-fold) SAM-binding motif, and the overall domain architecture (N-terminal region + C-terminal catalytic core with 'DIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA') matches O-methyltransferases. This rules out D (one-carbon metabolism), whose methyltransferases (e.g., methionine synthase, MTHFR, glycine N-methyltransferase) have distinctly different domain architectures (cobalamin-binding, folate-binding, or different Rossmann arrangements). The protein lacks any polyketide synthase (PKS) domains (no KS, AT, ACP, KR, DH, ER modules) and lacks NRPS domains, so it is a tailoring enzyme rather than a core biosynthetic scaffold. For tailoring methyltransferases in fungal natural-product gene clusters, the well-established pattern (learned from many fungal O-methyltransferases in secondary metabolite clusters) is that they are annotated under the broad 'Secondary metabolite biosynthesis' pathway rather than the narrower 'Polyketide biosynthesis,' because the methyltransferase itself does not perform polyketide chain assembly. This distinguishes C from A. B (Antibiotic biosynthesis) is a further subset requiring evidence of antimicrobial activity, which is not inferable from a methyltransferase sequence alone. Thus, the methyltransferase domain identity plus the absence of PKS/NRPS core domains plus the general pattern of fungal tailoring methyltransferases in secondary metabolite clusters supports C as the most defensible choice.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the SAM-methyltransferase fold from the GGSTG motif and domain organization, rule out one-carbon metabolism by comparing to known folate/methionine-cycle methyltransferase architectures, and apply the general pattern that tailoring methyltransferases in fungal biosynthetic gene clusters are classified under secondary metabolite biosynthesis broadly. The absence of PKS core domains weakens A relative to C. This is a legitimate family-level and mechanistic inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The protein is in fact a tailoring O-methyltransferase in a polyketide biosynthetic pathway (the 2012 paper describes a novel polyketide). Thus 'Polyketide biosynthesis' (A) is factually accurate for this protein's pathway. 'Secondary metabolite biosynthesis' (C) is the broader UniProt annotation and is also accurate. Without the specific pathway context, a model could reasonably argue for A if it recognized the protein as a methyltransferase acting on a polyketide intermediate. The distinction between A and C depends on whether one treats the pathway as the specific polyketide route or the broader secondary metabolite category. The UniProt annotation resolves this in favor of C, but the question wording does not clearly exclude A."
  },
  "important_caveats": [
    "The distinction between A (Polyketide biosynthesis) and C (Secondary metabolite biosynthesis) is a taxonomy-of-pathways issue: polyketide biosynthesis is a subset of secondary metabolite biosynthesis. The UniProt annotation uses the broader term, but the specific pathway IS polyketide biosynthesis.",
    "The methyltransferase identification from sequence is robust (GGSTG motif, domain architecture), but the specific pathway assignment (polyketide vs. other secondary metabolite) cannot be determined from the methyltransferase sequence alone without pathway context.",
    "The evidence for the pathway annotation is experimental (ECO:0000269) from a 2012 paper, not purely computational inference.",
    "The organism (Aspergillus oryzae) is not provided in the original input; the fungal secondary metabolite cluster context is inferred from general knowledge of fungal methyltransferases, which is permitted transferable knowledge."
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
  "benchmark_sequence_length": 423,
  "benchmark_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 423,
  "current_source_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 88,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2TXQ9",
  "selected_historical_entry_version": 88,
  "selected_historical_record_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "selected_historical_source_sequence_length": 423,
  "selected_historical_source_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "selected_historical_version": {
    "accession": "Q2TXQ9",
    "database": "Swiss-Prot",
    "entryVersion": 88,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOIF_ASPOR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2TXQ9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yellow koji mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus oryzae (strain ATCC 42149 / RIB 40)\",\"taxonId\":510516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase aoiF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Nakazawa T.\",\"Ishiuchi K.\",\"Praseuth A.\",\"Noguchi H.\",\"Hotta K.\",\"Watanabe K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22447538\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201200107\"}],\"citationType\":\"journal article\",\"firstPage\":\"855\",\"id\":\"22447538\",\"journal\":\"ChemBioChem\",\"lastPage\":\"861\",\"publicationDate\":\"2012\",\"title\":\"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.\",\"volume\":\"13\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H1",
  "excerpt": "ID   AOIF_ASPOR              Reviewed;         423 AA.\nAC   Q2TXQ9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 88.\nDE   RecName: Full=O-methyltransferase aoiF {ECO:0000303|PubMed:22447538};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:22447538};\nGN   Name=aoiF {ECO:0000303|PubMed:22447538}; ORFNames=AO090010000047;\nOS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=510516;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND INDUCTION.\nRX   PubMed=22447538; DOI=10.1002/cbic.201200107;\nRA   Nakazawa T., Ishiuchi K., Praseuth A., Noguchi H., Hotta K., Watanabe K.;\nRT   \"Overexpressing transcriptional regulator in Aspergillus oryzae activates a\nRT   silent biosynthetic pathway to produce a novel polyketide.\";\nRL   ChemBioChem 13:855-861(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:22447538}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
