# pathway_0119

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0119.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Protein biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPFQMGEAMPDLVPVLAEAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTSETIADPEARSVANRAIVTLRRIGKVPAESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLGDKRLLATPDEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEDFVQHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAILGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAEIAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGYLEASGHNWVEGQGSGERIDKKAADDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. L-methionine biosynthesis via de novo pathway. .
B. L-histidine biosynthesis
C. Protein biosynthesis
D. Polyketide biosynthesis. .
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

> The supplied sequence matches the reviewed protein record, which identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), so this supports the key but is not, by itself, direct experimental evidence.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, soluble sequence contains two widely separated P-loop nucleotide-binding motifs, including glycine-rich Walker-A-like sequences, and lacks an apparent membrane-spanning region. Together with the large multidomain architecture, these features are consistent with the eukaryotic elongation factor 3 family: a translation factor with tandem ATPase domains. Family-level knowledge therefore favors protein biosynthesis over the amino-acid-biosynthesis and polyketide alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family/architecture inference can meaningfully distinguish choice C among the offered pathways without recalling this exact protein's database entry. The sequence features alone are not definitive, but they provide a credible basis for recognizing an elongation-factor-like protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe distinct pathways, and the sequence's large soluble tandem-ATPase architecture supports translation elongation rather than the listed biosynthetic pathways.


### Important caveats

- The cited pathway annotation is similarity-transferred; the supplied evidence does not establish direct experimental validation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, soluble sequence contains two widely separated P-loop nucleotide-binding motifs, including glycine-rich Walker-A-like sequences, and lacks an apparent membrane-spanning region. Together with the large multidomain architecture, these features are consistent with the eukaryotic elongation factor 3 family: a translation factor with tandem ATPase domains. Family-level knowledge therefore favors protein biosynthesis over the amino-acid-biosynthesis and polyketide alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family/architecture inference can meaningfully distinguish choice C among the offered pathways without recalling this exact protein's database entry. The sequence features alone are not definitive, but they provide a credible basis for recognizing an elongation-factor-like protein."
  },
  "case_id": "pathway_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record, which identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), so this supports the key but is not, by itself, direct experimental evidence."
  },
  "important_caveats": [
    "The cited pathway annotation is similarity-transferred; the supplied evidence does not establish direct experimental validation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct pathways, and the sequence's large soluble tandem-ATPase architecture supports translation elongation rather than the listed biosynthetic pathways."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record, which identifies the protein as elongation factor 3 and annotates its pathway as protein biosynthesis, specifically polypeptide-chain elongation. The pathway annotation is transferred by similarity (ECO:0000250), so this supports the key but is not, by itself, direct experimental evidence.",
    "evidence_ids": ["H1", "H2", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, soluble sequence contains two widely separated P-loop nucleotide-binding motifs, including glycine-rich Walker-A-like sequences, and lacks an apparent membrane-spanning region. Together with the large multidomain architecture, these features are consistent with the eukaryotic elongation factor 3 family: a translation factor with tandem ATPase domains. Family-level knowledge therefore favors protein biosynthesis over the amino-acid-biosynthesis and polyketide alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family/architecture inference can meaningfully distinguish choice C among the offered pathways without recalling this exact protein's database entry. The sequence features alone are not definitive, but they provide a credible basis for recognizing an elongation-factor-like protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe distinct pathways, and the sequence's large soluble tandem-ATPase architecture supports translation elongation rather than the listed biosynthetic pathways."
  },
  "important_caveats": [
    "The cited pathway annotation is similarity-transferred; the supplied evidence does not establish direct experimental validation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (J9VQZ9, Elongation factor 3/eEF3 from Cryptococcus neoformans) explicitly states 'Protein biosynthesis; polypeptide chain elongation' (evidence C5, H2). The protein is EF-3, a fungal translation elongation factor. The expected answer C 'Protein biosynthesis' is directly and unambiguously supported by the database annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple canonical ABC ATPase Walker A motifs (GSGKST appearing at least twice: 'GRNGSGKSTLMNAIINNQ', 'GPNGSGKSTLVKLLTGET', and a variant 'GLSGGQKVKVVLGAATW') along with Walker B/DEPT signatures ('LLDEPTNHLDVLNVDWL', 'LLDEPTNYLDRESLA'). These are hallmark features of ABC-type ATPase domains. Among the four choices, protein biosynthesis (elongation factors EF-1A, EF-2, EF-3) is the pathway that employs proteins with multiple ABC ATPase domains. Methionine biosynthesis (A) involves PLP-dependent enzymes and smaller metabolic enzymes; histidine biosynthesis (B) involves specific enzymes like ATP-PRT, HisA, HisB with entirely different folds; polyketide synthases (D) use KS/AT/DH/ER/KR/ACP catalytic domains, not Walker A/ABC ATPase motifs. A knowledgeable model recognizing the ABC ATPase architecture can eliminate A, B, and D and select C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multiple Walker A (GSGKST) and ABC ATPase (DEPT) motifs are directly observable in the supplied sequence. Knowledge of protein families—specifically that elongation factors are the major class of proteins with multiple ABC ATPase domains in the context of metabolic/signaling pathways—allows a model to distinguish protein biosynthesis from the three metabolic biosynthesis options without needing to identify this exact protein as EF-3.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The ABC ATPase domain architecture is inconsistent with methionine biosynthesis enzymes, histidine biosynthesis enzymes, and polyketide synthases. Only protein biosynthesis (elongation factors) among the four choices uses proteins with multiple Walker A/ABC ATPase domains. No other option is defensible given these sequence features.


### Important caveats

- EF-3 is a fungal-specific elongation factor not present in animals or plants; a model familiar only with bacterial/eukaryotic EF-Tu/EF-G might not immediately map ABC ATPase domains to elongation factors, but the domain architecture still eliminates the other three choices.
- The UniProt pathway annotation is transferred by similarity (ECO:0000250 from O93796, yeast EF-3), not from direct experimental measurement on this exact protein, but the functional assignment is well-established for the EF-3 family.
- The sequence is 1055 aa, consistent with the large multi-domain architecture of EF-3.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple canonical ABC ATPase Walker A motifs (GSGKST appearing at least twice: 'GRNGSGKSTLMNAIINNQ', 'GPNGSGKSTLVKLLTGET', and a variant 'GLSGGQKVKVVLGAATW') along with Walker B/DEPT signatures ('LLDEPTNHLDVLNVDWL', 'LLDEPTNYLDRESLA'). These are hallmark features of ABC-type ATPase domains. Among the four choices, protein biosynthesis (elongation factors EF-1A, EF-2, EF-3) is the pathway that employs proteins with multiple ABC ATPase domains. Methionine biosynthesis (A) involves PLP-dependent enzymes and smaller metabolic enzymes; histidine biosynthesis (B) involves specific enzymes like ATP-PRT, HisA, HisB with entirely different folds; polyketide synthases (D) use KS/AT/DH/ER/KR/ACP catalytic domains, not Walker A/ABC ATPase motifs. A knowledgeable model recognizing the ABC ATPase architecture can eliminate A, B, and D and select C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multiple Walker A (GSGKST) and ABC ATPase (DEPT) motifs are directly observable in the supplied sequence. Knowledge of protein families—specifically that elongation factors are the major class of proteins with multiple ABC ATPase domains in the context of metabolic/signaling pathways—allows a model to distinguish protein biosynthesis from the three metabolic biosynthesis options without needing to identify this exact protein as EF-3."
  },
  "case_id": "pathway_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (J9VQZ9, Elongation factor 3/eEF3 from Cryptococcus neoformans) explicitly states 'Protein biosynthesis; polypeptide chain elongation' (evidence C5, H2). The protein is EF-3, a fungal translation elongation factor. The expected answer C 'Protein biosynthesis' is directly and unambiguously supported by the database annotation."
  },
  "important_caveats": [
    "EF-3 is a fungal-specific elongation factor not present in animals or plants; a model familiar only with bacterial/eukaryotic EF-Tu/EF-G might not immediately map ABC ATPase domains to elongation factors, but the domain architecture still eliminates the other three choices.",
    "The UniProt pathway annotation is transferred by similarity (ECO:0000250 from O93796, yeast EF-3), not from direct experimental measurement on this exact protein, but the functional assignment is well-established for the EF-3 family.",
    "The sequence is 1055 aa, consistent with the large multi-domain architecture of EF-3."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ABC ATPase domain architecture is inconsistent with methionine biosynthesis enzymes, histidine biosynthesis enzymes, and polyketide synthases. Only protein biosynthesis (elongation factors) among the four choices uses proteins with multiple Walker A/ABC ATPase domains. No other option is defensible given these sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (J9VQZ9, Elongation factor 3/eEF3 from Cryptococcus neoformans) explicitly states 'Protein biosynthesis; polypeptide chain elongation' (evidence C5, H2). The protein is EF-3, a fungal translation elongation factor. The expected answer C 'Protein biosynthesis' is directly and unambiguously supported by the database annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple canonical ABC ATPase Walker A motifs (GSGKST appearing at least twice: 'GRNGSGKSTLMNAIINNQ', 'GPNGSGKSTLVKLLTGET', and a variant 'GLSGGQKVKVVLGAATW') along with Walker B/DEPT signatures ('LLDEPTNHLDVLNVDWL', 'LLDEPTNYLDRESLA'). These are hallmark features of ABC-type ATPase domains. Among the four choices, protein biosynthesis (elongation factors EF-1A, EF-2, EF-3) is the pathway that employs proteins with multiple ABC ATPase domains. Methionine biosynthesis (A) involves PLP-dependent enzymes and smaller metabolic enzymes; histidine biosynthesis (B) involves specific enzymes like ATP-PRT, HisA, HisB with entirely different folds; polyketide synthases (D) use KS/AT/DH/ER/KR/ACP catalytic domains, not Walker A/ABC ATPase motifs. A knowledgeable model recognizing the ABC ATPase architecture can eliminate A, B, and D and select C.",
    "missing_item_specific_fact": "",
    "reason": "The multiple Walker A (GSGKST) and ABC ATPase (DEPT) motifs are directly observable in the supplied sequence. Knowledge of protein families—specifically that elongation factors are the major class of proteins with multiple ABC ATPase domains in the context of metabolic/signaling pathways—allows a model to distinguish protein biosynthesis from the three metabolic biosynthesis options without needing to identify this exact protein as EF-3."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ABC ATPase domain architecture is inconsistent with methionine biosynthesis enzymes, histidine biosynthesis enzymes, and polyketide synthases. Only protein biosynthesis (elongation factors) among the four choices uses proteins with multiple Walker A/ABC ATPase domains. No other option is defensible given these sequence features."
  },
  "important_caveats": [
    "EF-3 is a fungal-specific elongation factor not present in animals or plants; a model familiar only with bacterial/eukaryotic EF-Tu/EF-G might not immediately map ABC ATPase domains to elongation factors, but the domain architecture still eliminates the other three choices.",
    "The UniProt pathway annotation is transferred by similarity (ECO:0000250 from O93796, yeast EF-3), not from direct experimental measurement on this exact protein, but the functional assignment is well-established for the EF-3 family.",
    "The sequence is 1055 aa, consistent with the large multi-domain architecture of EF-3."
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
  "benchmark_sequence_length": 1055,
  "benchmark_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "current_entry_audit": {
    "entryVersion": 68,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2013-11-13",
    "sequenceVersion": 2
  },
  "current_record_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1055,
  "current_source_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 66,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VQZ9",
  "selected_historical_entry_version": 66,
  "selected_historical_record_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "selected_historical_source_sequence_length": 1055,
  "selected_historical_source_sequence_sha256": "6ac3a0db14920eb77abf52193ecd849165175b8df860637dda883591fdc7e600",
  "selected_historical_version": {
    "accession": "J9VQZ9",
    "database": "Swiss-Prot",
    "entryVersion": 66,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EF3_CRYN9",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VQZ9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":68,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2013-11-13\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR95029.2\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Eukaryotic elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"eEF3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q5KIM6\",\"source\":\"UniProtKB\"}],\"value\":\"3.6.4.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Elongation factor 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"EF-3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O93796\",\"source\":\"UniProtKB\"}],\"value\":\"Protein biosynthesis; polypeptide chain elongation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:10.554047+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9",
  "url": "https://rest.uniprot.org/uniprotkb/J9VQZ9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H1",
  "excerpt": "ID   EF3_CRYN9               Reviewed;        1055 AA.\nAC   J9VQZ9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-NOV-2013, sequence version 2.\nDT   28-JAN-2026, entry version 66.\nDE   RecName: Full=Elongation factor 3 {ECO:0000305};\nDE            Short=EF-3 {ECO:0000305};\nDE            EC=3.6.4.- {ECO:0000250|UniProtKB:Q5KIM6};\nDE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};\nDE            Short=eEF3 {ECO:0000305};\nGN   Name=TEF3 {ECO:0000305}; ORFNames=CNAG_01117 {ECO:0000312|EMBL:AFR95029.2};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR95029.2, ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.511490+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "url": "https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)

```json
{
  "entry_version": 66,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Protein biosynthesis; polypeptide chain elongation.\nCC       {ECO:0000250|UniProtKB:O93796}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:11.511490+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d",
  "url": "https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
