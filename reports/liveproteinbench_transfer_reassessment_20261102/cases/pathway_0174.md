# pathway_0174

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0174.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRFSASLLLALTGSAAASPIRAEEEIRVYDLPISLFDDLQGLDAAMKAAGREYIGTSLTVRNDFQEQNIIRTEFGSITPENAQKWDATEPNRGQFTFGSADQHMDWARQNGKHVRCHTLVWYSQLPGWVSNSGFNNATLQQVMQNHINQVMGRYRGRCNHWDVVNEAPRLMAMRLQIGEAYIPIAFRMAAQADPSAKLYYNDYNLEYLGPKVEGAARIVRLVKQYGARIDGVGYQAHLVTEPTPTQSTPTPSEEDLIKALRITADLGVDVAYTEIDIRMRTPSNAQKLQQLADAYYRVARSCMKVPRCVGMTIWGVTDRYSWVPNTFRGEGDALLWDSNYQRKAAYNAFLRGIQEPVN

[Multiple Choices]
A. Glycan degradation
B. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
C. Cell wall degradation
D. L-histidine biosynthesis
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

> The sequence-matched UniProt entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The annotation cites experimental evidence, although the supplied excerpts do not independently validate the underlying study.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with secretion, and a fungal secreted polysaccharide hydrolase would make glycan breakdown more plausible than cystathionine formation or histidine biosynthesis. But that inference does not resolve the offered overlap between glycan degradation and cell wall degradation: xylan is both a glycan and a component of plant cell walls.


**Missing item-specific fact**

> The protein's specific substrate/activity annotation, or an equivalent fact establishing whether the benchmark categorizes its role as glycan degradation rather than cell wall degradation.


**Reason**

> Transferable biological knowledge can narrow the choices to carbohydrate breakdown, but the offered A and C categories both fit that general role. Selecting the keyed pathway label therefore requires information about this protein's specific activity or its pathway categorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> A xylan-degrading enzyme directly acts on a glycan, while xylan is also a plant cell-wall component; the choices do not specify which level of pathway categorization is intended.


### Important caveats

- The source excerpts identify a sequence-matched protein, but the author's exact source snapshot is unknown.
- The reviewer-only identity and annotation were not part of the original model input and are not used as transferable input evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and a fungal secreted polysaccharide hydrolase would make glycan breakdown more plausible than cystathionine formation or histidine biosynthesis. But that inference does not resolve the offered overlap between glycan degradation and cell wall degradation: xylan is both a glycan and a component of plant cell walls.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific substrate/activity annotation, or an equivalent fact establishing whether the benchmark categorizes its role as glycan degradation rather than cell wall degradation.",
    "reason": "Transferable biological knowledge can narrow the choices to carbohydrate breakdown, but the offered A and C categories both fit that general role. Selecting the keyed pathway label therefore requires information about this protein's specific activity or its pathway categorization."
  },
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The annotation cites experimental evidence, although the supplied excerpts do not independently validate the underlying study."
  },
  "important_caveats": [
    "The source excerpts identify a sequence-matched protein, but the author's exact source snapshot is unknown.",
    "The reviewer-only identity and annotation were not part of the original model input and are not used as transferable input evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "A xylan-degrading enzyme directly acts on a glycan, while xylan is also a plant cell-wall component; the choices do not specify which level of pathway categorization is intended."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry identifies the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The annotation cites experimental evidence, although the supplied excerpts do not independently validate the underlying study.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with secretion, and a fungal secreted polysaccharide hydrolase would make glycan breakdown more plausible than cystathionine formation or histidine biosynthesis. But that inference does not resolve the offered overlap between glycan degradation and cell wall degradation: xylan is both a glycan and a component of plant cell walls.",
    "missing_item_specific_fact": "The protein's specific substrate/activity annotation, or an equivalent fact establishing whether the benchmark categorizes its role as glycan degradation rather than cell wall degradation.",
    "reason": "Transferable biological knowledge can narrow the choices to carbohydrate breakdown, but the offered A and C categories both fit that general role. Selecting the keyed pathway label therefore requires information about this protein's specific activity or its pathway categorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "A xylan-degrading enzyme directly acts on a glycan, while xylan is also a plant cell-wall component; the choices do not specify which level of pathway categorization is intended."
  },
  "important_caveats": [
    "The source excerpts identify a sequence-matched protein, but the author's exact source snapshot is unknown.",
    "The reviewer-only identity and annotation were not part of the original model input and are not used as transferable input evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) from Humicola insolens is explicitly annotated with the pathway 'Glycan degradation; xylan degradation' supported by experimental evidence (ECO:0000269, PubMed:23306124). The expected answer 'Glycan degradation' directly matches this pathway annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence begins with a clear fungal secretion signal peptide (MRFSASLLLALTGSAAASPIR), indicating an extracellular enzyme. The mature sequence (~336 aa) contains multiple tryptophan residues in positions and contexts characteristic of glycoside hydrolase active sites (e.g., 'WV' and 'WVPNT' motifs reminiscent of GH10/GH11 xylanase catalytic pockets). The overall aromatic-rich composition and domain architecture are consistent with a β-jelly roll or (β/α)8-barrel glycan-binding fold. This rules out B (PLP-dependent cystathionine synthase, an intracellular transferase) and D (histidine biosynthesis enzymes, intracellular). Against C ('Cell wall degradation' in UniProt/KEGG taxonomy specifically denotes peptidoglycan/bacterial cell wall hydrolysis by lysozymes, amidases, and transglycosylases with entirely different folds), the GH-family sequence motifs point to a glycan-active enzyme. In the UniProt pathway hierarchy, xylanases are classified under 'Glycan degradation,' not 'Cell wall degradation.' A model recognizing GH-family sequence signatures and the pathway taxonomy can distinguish A from C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The signal peptide, GH-family aromatic motifs, and overall fold architecture provide transferable evidence that this is a secreted glycoside hydrolase (xylanase). Pathway taxonomy knowledge (learned from many other GH enzymes annotated under 'Glycan degradation' vs. peptidoglycan enzymes under 'Cell wall degradation') allows distinguishing A from C without memorizing this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is a major plant cell wall component, so a model might reason that a xylanase participates in 'cell wall degradation.' However, in UniProt/KEGG pathway nomenclature, 'Cell wall degradation' specifically refers to bacterial peptidoglycan hydrolysis, while xylan degradation falls under 'Glycan degradation.' The ambiguity is resolvable by pathway taxonomy knowledge but could trip up a model unfamiliar with this specific classification convention.


### Important caveats

- The distinction between 'Glycan degradation' and 'Cell wall degradation' relies on UniProt/KEGG pathway taxonomy conventions rather than pure biochemistry, since xylan is indeed a cell wall polymer.
- The GH-family assignment (GH10 vs GH11) is inferred from sequence motifs and length; the exact family could not be confirmed without structural data.
- The reviewer evidence confirms the annotation is experimentally supported (PubMed:23306124), not merely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence begins with a clear fungal secretion signal peptide (MRFSASLLLALTGSAAASPIR), indicating an extracellular enzyme. The mature sequence (~336 aa) contains multiple tryptophan residues in positions and contexts characteristic of glycoside hydrolase active sites (e.g., 'WV' and 'WVPNT' motifs reminiscent of GH10/GH11 xylanase catalytic pockets). The overall aromatic-rich composition and domain architecture are consistent with a β-jelly roll or (β/α)8-barrel glycan-binding fold. This rules out B (PLP-dependent cystathionine synthase, an intracellular transferase) and D (histidine biosynthesis enzymes, intracellular). Against C ('Cell wall degradation' in UniProt/KEGG taxonomy specifically denotes peptidoglycan/bacterial cell wall hydrolysis by lysozymes, amidases, and transglycosylases with entirely different folds), the GH-family sequence motifs point to a glycan-active enzyme. In the UniProt pathway hierarchy, xylanases are classified under 'Glycan degradation,' not 'Cell wall degradation.' A model recognizing GH-family sequence signatures and the pathway taxonomy can distinguish A from C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide, GH-family aromatic motifs, and overall fold architecture provide transferable evidence that this is a secreted glycoside hydrolase (xylanase). Pathway taxonomy knowledge (learned from many other GH enzymes annotated under 'Glycan degradation' vs. peptidoglycan enzymes under 'Cell wall degradation') allows distinguishing A from C without memorizing this specific protein's record."
  },
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) from Humicola insolens is explicitly annotated with the pathway 'Glycan degradation; xylan degradation' supported by experimental evidence (ECO:0000269, PubMed:23306124). The expected answer 'Glycan degradation' directly matches this pathway annotation."
  },
  "important_caveats": [
    "The distinction between 'Glycan degradation' and 'Cell wall degradation' relies on UniProt/KEGG pathway taxonomy conventions rather than pure biochemistry, since xylan is indeed a cell wall polymer.",
    "The GH-family assignment (GH10 vs GH11) is inferred from sequence motifs and length; the exact family could not be confirmed without structural data.",
    "The reviewer evidence confirms the annotation is experimentally supported (PubMed:23306124), not merely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is a major plant cell wall component, so a model might reason that a xylanase participates in 'cell wall degradation.' However, in UniProt/KEGG pathway nomenclature, 'Cell wall degradation' specifically refers to bacterial peptidoglycan hydrolysis, while xylan degradation falls under 'Glycan degradation.' The ambiguity is resolvable by pathway taxonomy knowledge but could trip up a model unfamiliar with this specific classification convention."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry M4MLB5 (Endo-1,4-beta-xylanase B, EC 3.2.1.8) from Humicola insolens is explicitly annotated with the pathway 'Glycan degradation; xylan degradation' supported by experimental evidence (ECO:0000269, PubMed:23306124). The expected answer 'Glycan degradation' directly matches this pathway annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence begins with a clear fungal secretion signal peptide (MRFSASLLLALTGSAAASPIR), indicating an extracellular enzyme. The mature sequence (~336 aa) contains multiple tryptophan residues in positions and contexts characteristic of glycoside hydrolase active sites (e.g., 'WV' and 'WVPNT' motifs reminiscent of GH10/GH11 xylanase catalytic pockets). The overall aromatic-rich composition and domain architecture are consistent with a β-jelly roll or (β/α)8-barrel glycan-binding fold. This rules out B (PLP-dependent cystathionine synthase, an intracellular transferase) and D (histidine biosynthesis enzymes, intracellular). Against C ('Cell wall degradation' in UniProt/KEGG taxonomy specifically denotes peptidoglycan/bacterial cell wall hydrolysis by lysozymes, amidases, and transglycosylases with entirely different folds), the GH-family sequence motifs point to a glycan-active enzyme. In the UniProt pathway hierarchy, xylanases are classified under 'Glycan degradation,' not 'Cell wall degradation.' A model recognizing GH-family sequence signatures and the pathway taxonomy can distinguish A from C.",
    "missing_item_specific_fact": "",
    "reason": "The signal peptide, GH-family aromatic motifs, and overall fold architecture provide transferable evidence that this is a secreted glycoside hydrolase (xylanase). Pathway taxonomy knowledge (learned from many other GH enzymes annotated under 'Glycan degradation' vs. peptidoglycan enzymes under 'Cell wall degradation') allows distinguishing A from C without memorizing this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is a major plant cell wall component, so a model might reason that a xylanase participates in 'cell wall degradation.' However, in UniProt/KEGG pathway nomenclature, 'Cell wall degradation' specifically refers to bacterial peptidoglycan hydrolysis, while xylan degradation falls under 'Glycan degradation.' The ambiguity is resolvable by pathway taxonomy knowledge but could trip up a model unfamiliar with this specific classification convention."
  },
  "important_caveats": [
    "The distinction between 'Glycan degradation' and 'Cell wall degradation' relies on UniProt/KEGG pathway taxonomy conventions rather than pure biochemistry, since xylan is indeed a cell wall polymer.",
    "The GH-family assignment (GH10 vs GH11) is inferred from sequence motifs and length; the exact family could not be confirmed without structural data.",
    "The reviewer evidence confirms the annotation is experimentally supported (PubMed:23306124), not merely computational."
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
  "benchmark_sequence_length": 358,
  "benchmark_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_entry_audit": {
    "entryVersion": 33,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 358,
  "current_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 31,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "M4MLB5",
  "selected_historical_entry_version": 31,
  "selected_historical_record_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "selected_historical_source_sequence_length": 358,
  "selected_historical_source_sequence_sha256": "0e3a88e10bc9db802cafcf77a32ab155d7b9003c45924dd5d25ec8dc07d86905",
  "selected_historical_version": {
    "accession": "M4MLB5",
    "database": "Swiss-Prot",
    "entryVersion": 31,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XYNB_HUMIN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"M4MLB5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":33,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Soft-rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Sordariales\",\"Chaetomiaceae\",\"Mycothermus\"],\"scientificName\":\"Humicola insolens\",\"taxonId\":85995}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"1,4-beta-D-xylan xylanohydrolase B\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase B\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23306124\",\"source\":\"PubMed\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/M4MLB5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Du Y.\",\"Shi P.\",\"Huang H.\",\"Zhang X.\",\"Luo H.\",\"Wang Y.\",\"Yao B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23306124\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.biortech.2012.12.067\"}],\"citationType\":\"journal article\",\"firstPage\":\"161\",\"id\":\"23306124\",\"journal\":\"Bioresour. Technol.\",\"lastPage\":\"167\",\"publicationDate\":\"2013\",\"title\":\"Characterization of three novel thermophilic xylanases from Humicola insolens Y1 with application potentials in the brewing industry.\",\"volume\":\"130\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Y1\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:12.159556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9737e107c7508ede0abc7bd8c8f14f35fc885d5000f5778fdd13b8d4054f912f",
  "url": "https://rest.uniprot.org/uniprotkb/M4MLB5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H1",
  "excerpt": "ID   XYNB_HUMIN              Reviewed;         358 AA.\nAC   M4MLB5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2013, sequence version 1.\nDT   28-JAN-2026, entry version 31.\nDE   RecName: Full=Endo-1,4-beta-xylanase B {ECO:0000303|PubMed:23306124};\nDE            EC=3.2.1.8 {ECO:0000269|PubMed:23306124};\nDE   AltName: Full=1,4-beta-D-xylan xylanohydrolase B {ECO:0000305};\nDE   Flags: Precursor;\nGN   Name=XynB {ECO:0000303|PubMed:23306124};\nOS   Humicola insolens (Soft-rot fungus).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Sordariales; Chaetomiaceae; Mycothermus.\nOX   NCBI_TaxID=85995;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   AND BIOTECHNOLOGY.\nRC   STRAIN=Y1;\nRX   PubMed=23306124; DOI=10.1016/j.biortech.2012.12.067;\nRA   Du Y., Shi P., Huang H., Zhang X., Luo H., Wang Y., Yao B.;\nRT   \"Characterization of three novel thermophilic xylanases from Humicola\nRT   insolens Y1 with application potentials in the brewing industry.\";\nRL   Bioresour. Technol. 130:161-167(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31)

```json
{
  "entry_version": 31,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation.\nCC       {ECO:0000269|PubMed:23306124}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.229298+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8a61ff0bb76d82894c8a3570170d306b45992420e142ae76129e353039c9cab6",
  "url": "https://rest.uniprot.org/unisave/M4MLB5?format=txt&versions=31"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
