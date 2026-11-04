# pathway_0074

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0074.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPSATPVIPSQQTAIVAEGAGQLSIYHDAPVPALQPDVALVKTAAVAINPVDAKMLDYSPVPGAIHGYDFAGTIVALGSDTPPHLKVGDRVAGFVHGMNPLLPDVGAFAEYVAASADLVLKLPDTMSFEEGASLGLGLFTAGLGLFQHLQIPLSLTREPSPEASSPTKADFVLVAGGSTATGTRALQLLKLAGLRPVATCSPAHFDLARRFGAEAVFDYHDPDCAAAIRAYTKNTLAYALDCLALAETTQLCYGALGRAGGRYVTLEPFREAIAAQRPHTVTPSWLLALTIFGRKVALDGEYGREANPEDREFGARLTEQVQGLLDEGKVDVHPVRVMGGGWQGVLEGVDLVRRQTVSGHKLVYAV

[Multiple Choices]
A. LPS O-antigen biosynthesis. .
B. glycosylphosphatidylinositol-anchor biosynthesis. .
C. L-methionine biosynthesis via de novo pathway. .
D. Secondary metabolite biosynthesis. .
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

> The sequence-matched archived UniProt record assigns the protein to secondary metabolite biosynthesis. That pathway annotation is transferred from another UniProt protein (ECO:0000250), so it supports the key as a database annotation rather than as direct experimental confirmation for this exact protein.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact soluble enzyme and has a glycine-rich region (including “AIVAEGAG”) compatible with a nucleotide-binding reductase. Enoyl-reduction enzymes can participate in natural-product biosynthesis; that enzyme class and soluble architecture make secondary-metabolite biosynthesis a credible choice over LPS O-antigen or GPI-anchor biosynthesis, which involve glycan or membrane-associated machinery, and over the specifically named methionine pathway. This is a probabilistic inference, not a pathway identification from a unique motif.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and enzyme-family knowledge provides a meaningful, if limited, basis for preferring D among these choices. The sequence alone does not establish the enzyme’s pathway context, and reductases can also function in primary metabolism, so genomic context would strengthen the inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is as defensible from the sequence-level inference, though the pathway assignment is not uniquely established by sequence features.


### Important caveats

- The pathway annotation in the supplied source is explicitly transferred by similarity; it is not direct experimental evidence for this sequence.
- The original input provides no organism or gene-cluster context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact soluble enzyme and has a glycine-rich region (including “AIVAEGAG”) compatible with a nucleotide-binding reductase. Enoyl-reduction enzymes can participate in natural-product biosynthesis; that enzyme class and soluble architecture make secondary-metabolite biosynthesis a credible choice over LPS O-antigen or GPI-anchor biosynthesis, which involve glycan or membrane-associated machinery, and over the specifically named methionine pathway. This is a probabilistic inference, not a pathway identification from a unique motif.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge provides a meaningful, if limited, basis for preferring D among these choices. The sequence alone does not establish the enzyme’s pathway context, and reductases can also function in primary metabolism, so genomic context would strengthen the inference."
  },
  "case_id": "pathway_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record assigns the protein to secondary metabolite biosynthesis. That pathway annotation is transferred from another UniProt protein (ECO:0000250), so it supports the key as a database annotation rather than as direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The pathway annotation in the supplied source is explicitly transferred by similarity; it is not direct experimental evidence for this sequence.",
    "The original input provides no organism or gene-cluster context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is as defensible from the sequence-level inference, though the pathway assignment is not uniquely established by sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt record assigns the protein to secondary metabolite biosynthesis. That pathway annotation is transferred from another UniProt protein (ECO:0000250), so it supports the key as a database annotation rather than as direct experimental confirmation for this exact protein.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact soluble enzyme and has a glycine-rich region (including “AIVAEGAG”) compatible with a nucleotide-binding reductase. Enoyl-reduction enzymes can participate in natural-product biosynthesis; that enzyme class and soluble architecture make secondary-metabolite biosynthesis a credible choice over LPS O-antigen or GPI-anchor biosynthesis, which involve glycan or membrane-associated machinery, and over the specifically named methionine pathway. This is a probabilistic inference, not a pathway identification from a unique motif.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and enzyme-family knowledge provides a meaningful, if limited, basis for preferring D among these choices. The sequence alone does not establish the enzyme’s pathway context, and reductases can also function in primary metabolism, so genomic context would strengthen the inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is as defensible from the sequence-level inference, though the pathway assignment is not uniquely established by sequence features."
  },
  "important_caveats": [
    "The pathway annotation in the supplied source is explicitly transferred by similarity; it is not direct experimental evidence for this sequence.",
    "The original input provides no organism or gene-cluster context."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A2QQU5) annotates this protein with pathway 'Secondary metabolite biosynthesis' (ECO:0000250, inferred by similarity to A0A0E0RXA7). The protein is named 'Trans-enoyl reductase caaB' / 'Carlosic acid biosynthesis cluster protein B,' and carlosic acid is described as a noncanonical cryptic polyketide from Aspergillus niger (PubMed:25044953). Polyketides are classic fungal secondary metabolites, so the pathway assignment is biologically coherent. The pathway comment itself is by similarity (ECO:0000250), but the protein's function as a trans-enoyl reductase in a polyketide biosynthetic cluster is experimentally supported (ECO:0000269 for EC, and the reference paper provides FUNCTION, CATALYTIC ACTIVITY, INDUCTION, and PATHWAY data).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Rossmann-fold-like nucleotide-binding motif (GxGxxG pattern visible in 'VAGGSTATGTRALQ' and 'GGGWQGVLEGVDLVRRQ'), characteristic of an NAD(P)-dependent reductase. Among the four options: (A) LPS O-antigen biosynthesis involves glycosyltransferases, polymerases, and specific transferases — not NAD(P)-dependent reductases with this architecture; (B) GPI-anchor biosynthesis involves phosphatases, glycosyltransferases, and transamidases — again not a reductase of this type; (C) L-methionine de novo biosynthesis involves homoserine dehydrogenase (a different reductase family with distinct domain organization), cystathionine synthases, and related enzymes — the domain architecture here does not match these; (D) Secondary metabolite (polyketide) biosynthesis clusters in fungi routinely encode NADPH-dependent trans-enoyl reductases as tailoring enzymes, and the observed reductase domain architecture is consistent with this family. A knowledgeable model can eliminate A and B based on the absence of glycosyltransferase/transferase features, and distinguish C from D by recognizing that the specific reductase domain architecture aligns with polyketide-cluster enoyl reductases rather than amino-acid-biosynthesis dehydrogenases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The domain architecture (NAD(P)-binding Rossmann fold consistent with a reductase) combined with knowledge of enzyme families in each pathway allows meaningful discrimination. Glycosyltransferase/polymerase enzymes (A, B) are structurally distinct. The specific reductase architecture is more consistent with polyketide tailoring enzymes (D) than with homoserine dehydrogenase or methionine-pathway enzymes (C). This is a family-level inference from transferable knowledge of enzyme domain architectures across pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 'Secondary metabolite biosynthesis' is a broad category, the four options are sufficiently distinct in the types of enzymes they involve. The reductase domain architecture does not match glycosyltransferases (A, B) or the specific enzymes of methionine biosynthesis (C). No other option is equally defensible given the domain architecture.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental pathway proof for this exact protein, though the protein's function and catalytic activity are experimentally supported.
- 'Secondary metabolite biosynthesis' is a very broad pathway category; the specific sub-pathway is polyketide (carlosic acid) biosynthesis, but the question only asks at the broad level.
- The organism (Aspergillus niger) is not given to the model, but the reasoning does not require knowing the organism — the domain architecture alone distinguishes the options.
- The sequence is 366 aa and contains a reductase domain; a model unfamiliar with trans-enoyl reductase domain architecture in polyketide clusters might struggle to definitively exclude option C, though the domain organizations are distinguishable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like nucleotide-binding motif (GxGxxG pattern visible in 'VAGGSTATGTRALQ' and 'GGGWQGVLEGVDLVRRQ'), characteristic of an NAD(P)-dependent reductase. Among the four options: (A) LPS O-antigen biosynthesis involves glycosyltransferases, polymerases, and specific transferases — not NAD(P)-dependent reductases with this architecture; (B) GPI-anchor biosynthesis involves phosphatases, glycosyltransferases, and transamidases — again not a reductase of this type; (C) L-methionine de novo biosynthesis involves homoserine dehydrogenase (a different reductase family with distinct domain organization), cystathionine synthases, and related enzymes — the domain architecture here does not match these; (D) Secondary metabolite (polyketide) biosynthesis clusters in fungi routinely encode NADPH-dependent trans-enoyl reductases as tailoring enzymes, and the observed reductase domain architecture is consistent with this family. A knowledgeable model can eliminate A and B based on the absence of glycosyltransferase/transferase features, and distinguish C from D by recognizing that the specific reductase domain architecture aligns with polyketide-cluster enoyl reductases rather than amino-acid-biosynthesis dehydrogenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The domain architecture (NAD(P)-binding Rossmann fold consistent with a reductase) combined with knowledge of enzyme families in each pathway allows meaningful discrimination. Glycosyltransferase/polymerase enzymes (A, B) are structurally distinct. The specific reductase architecture is more consistent with polyketide tailoring enzymes (D) than with homoserine dehydrogenase or methionine-pathway enzymes (C). This is a family-level inference from transferable knowledge of enzyme domain architectures across pathways."
  },
  "case_id": "pathway_0074",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A2QQU5) annotates this protein with pathway 'Secondary metabolite biosynthesis' (ECO:0000250, inferred by similarity to A0A0E0RXA7). The protein is named 'Trans-enoyl reductase caaB' / 'Carlosic acid biosynthesis cluster protein B,' and carlosic acid is described as a noncanonical cryptic polyketide from Aspergillus niger (PubMed:25044953). Polyketides are classic fungal secondary metabolites, so the pathway assignment is biologically coherent. The pathway comment itself is by similarity (ECO:0000250), but the protein's function as a trans-enoyl reductase in a polyketide biosynthetic cluster is experimentally supported (ECO:0000269 for EC, and the reference paper provides FUNCTION, CATALYTIC ACTIVITY, INDUCTION, and PATHWAY data)."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental pathway proof for this exact protein, though the protein's function and catalytic activity are experimentally supported.",
    "'Secondary metabolite biosynthesis' is a very broad pathway category; the specific sub-pathway is polyketide (carlosic acid) biosynthesis, but the question only asks at the broad level.",
    "The organism (Aspergillus niger) is not given to the model, but the reasoning does not require knowing the organism — the domain architecture alone distinguishes the options.",
    "The sequence is 366 aa and contains a reductase domain; a model unfamiliar with trans-enoyl reductase domain architecture in polyketide clusters might struggle to definitively exclude option C, though the domain organizations are distinguishable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'Secondary metabolite biosynthesis' is a broad category, the four options are sufficiently distinct in the types of enzymes they involve. The reductase domain architecture does not match glycosyltransferases (A, B) or the specific enzymes of methionine biosynthesis (C). No other option is equally defensible given the domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0074",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A2QQU5) annotates this protein with pathway 'Secondary metabolite biosynthesis' (ECO:0000250, inferred by similarity to A0A0E0RXA7). The protein is named 'Trans-enoyl reductase caaB' / 'Carlosic acid biosynthesis cluster protein B,' and carlosic acid is described as a noncanonical cryptic polyketide from Aspergillus niger (PubMed:25044953). Polyketides are classic fungal secondary metabolites, so the pathway assignment is biologically coherent. The pathway comment itself is by similarity (ECO:0000250), but the protein's function as a trans-enoyl reductase in a polyketide biosynthetic cluster is experimentally supported (ECO:0000269 for EC, and the reference paper provides FUNCTION, CATALYTIC ACTIVITY, INDUCTION, and PATHWAY data).",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold-like nucleotide-binding motif (GxGxxG pattern visible in 'VAGGSTATGTRALQ' and 'GGGWQGVLEGVDLVRRQ'), characteristic of an NAD(P)-dependent reductase. Among the four options: (A) LPS O-antigen biosynthesis involves glycosyltransferases, polymerases, and specific transferases — not NAD(P)-dependent reductases with this architecture; (B) GPI-anchor biosynthesis involves phosphatases, glycosyltransferases, and transamidases — again not a reductase of this type; (C) L-methionine de novo biosynthesis involves homoserine dehydrogenase (a different reductase family with distinct domain organization), cystathionine synthases, and related enzymes — the domain architecture here does not match these; (D) Secondary metabolite (polyketide) biosynthesis clusters in fungi routinely encode NADPH-dependent trans-enoyl reductases as tailoring enzymes, and the observed reductase domain architecture is consistent with this family. A knowledgeable model can eliminate A and B based on the absence of glycosyltransferase/transferase features, and distinguish C from D by recognizing that the specific reductase domain architecture aligns with polyketide-cluster enoyl reductases rather than amino-acid-biosynthesis dehydrogenases.",
    "missing_item_specific_fact": "",
    "reason": "The domain architecture (NAD(P)-binding Rossmann fold consistent with a reductase) combined with knowledge of enzyme families in each pathway allows meaningful discrimination. Glycosyltransferase/polymerase enzymes (A, B) are structurally distinct. The specific reductase architecture is more consistent with polyketide tailoring enzymes (D) than with homoserine dehydrogenase or methionine-pathway enzymes (C). This is a family-level inference from transferable knowledge of enzyme domain architectures across pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'Secondary metabolite biosynthesis' is a broad category, the four options are sufficiently distinct in the types of enzymes they involve. The reductase domain architecture does not match glycosyltransferases (A, B) or the specific enzymes of methionine biosynthesis (C). No other option is equally defensible given the domain architecture."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (inferred by similarity), not direct experimental pathway proof for this exact protein, though the protein's function and catalytic activity are experimentally supported.",
    "'Secondary metabolite biosynthesis' is a very broad pathway category; the specific sub-pathway is polyketide (carlosic acid) biosynthesis, but the question only asks at the broad level.",
    "The organism (Aspergillus niger) is not given to the model, but the reasoning does not require knowing the organism — the domain architecture alone distinguishes the options.",
    "The sequence is 366 aa and contains a reductase domain; a model unfamiliar with trans-enoyl reductase domain architecture in polyketide clusters might struggle to definitively exclude option C, though the domain organizations are distinguishable."
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
  "benchmark_sequence_length": 366,
  "benchmark_sequence_sha256": "e8c47c98be4b92604db479b0e043223ec279e935102532b224ab7194cb91d5c6",
  "current_entry_audit": {
    "entryVersion": 101,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-03-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 366,
  "current_source_sequence_sha256": "e8c47c98be4b92604db479b0e043223ec279e935102532b224ab7194cb91d5c6",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A2QQU5",
  "selected_historical_entry_version": 100,
  "selected_historical_record_sha256": "1d9df0690710a301b1081da4f1701485317bbf1008a1422094bc639434427cf1",
  "selected_historical_source_sequence_length": 366,
  "selected_historical_source_sequence_sha256": "e8c47c98be4b92604db479b0e043223ec279e935102532b224ab7194cb91d5c6",
  "selected_historical_version": {
    "accession": "A2QQU5",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CAAB_ASPNC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A2QQU5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":101,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-03-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513)\",\"taxonId\":425011}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Carlosic acid biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Trans-enoyl reductase caaB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0E0RXA7\",\"source\":\"UniProtKB\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.L.\",\"Awakawa T.\",\"Wakimoto T.\",\"Abe I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25044953\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201402172\"}],\"citationType\":\"journal article\",\"firstPage\":\"1578\",\"id\":\"25044953\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1583\",\"publicationDate\":\"2014\",\"title\":\"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from Aspergillus niger identified by genome mining.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:50.908499+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ec0720d681f22d21e385e54c1260725a15cf2c30e21daab42ba29c923141a8dd",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H1",
  "excerpt": "ID   CAAB_ASPNC              Reviewed;         366 AA.\nAC   A2QQU5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-MAR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Trans-enoyl reductase caaB {ECO:0000303|PubMed:25044953};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:25044953};\nDE   AltName: Full=Carlosic acid biosynthesis cluster protein B {ECO:0000303|PubMed:25044953};\nGN   Name=caaB {ECO:0000303|PubMed:25044953}; ORFNames=An08g03740;\nOS   Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=425011;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:55.145395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1d9df0690710a301b1081da4f1701485317bbf1008a1422094bc639434427cf1",
  "url": "https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, INDUCTION, AND PATHWAY.\nRX   PubMed=25044953; DOI=10.1002/cbic.201402172;\nRA   Yang X.L., Awakawa T., Wakimoto T., Abe I.;\nRT   \"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from\nRT   Aspergillus niger identified by genome mining.\";\nRL   ChemBioChem 15:1578-1583(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:55.145395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1d9df0690710a301b1081da4f1701485317bbf1008a1422094bc639434427cf1",
  "url": "https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100)

```json
{
  "entry_version": 100,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000250|UniProtKB:A0A0E0RXA7}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:55.145395+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-63",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1d9df0690710a301b1081da4f1701485317bbf1008a1422094bc639434427cf1",
  "url": "https://rest.uniprot.org/unisave/A2QQU5?format=txt&versions=100"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 74. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
