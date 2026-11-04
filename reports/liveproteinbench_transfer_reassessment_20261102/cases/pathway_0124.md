# pathway_0124

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0124.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. Cell wall biogenesis
B. nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1. .
C. iron-sulfur cluster biosynthesis. .
D. Lipid metabolism. .
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

> The sequence-matched UniProt entry explicitly assigns this protein to lipid metabolism. The annotation names cysteate synthase and cites a characterization paper, though the pathway assignment itself is a database annotation rather than direct experimental proof in these excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The sequence's specific identification as cysteate synthase, with a role in producing a precursor for sulfonolipid (capnine) biosynthesis, is not provided in the original input.


**Reason**

> The sequence is consistent with an enzyme, and sulfur-related enzyme chemistry might make some choices more plausible, but that does not meaningfully distinguish lipid metabolism from iron-sulfur cluster biosynthesis here. No clear sequence feature in the input identifies the specific cysteate-synthase activity or its connection to sulfonolipids; that functional link is needed to select D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence-matched annotation supports D, and the choices describe distinct pathways; no second choice is comparably supported by the supplied evidence.


### Important caveats

- The reviewer-only source evidence was not part of the evaluated model's input.
- The pathway annotation cites a characterization paper, but the excerpts do not independently establish the experimental basis for the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's specific identification as cysteate synthase, with a role in producing a precursor for sulfonolipid (capnine) biosynthesis, is not provided in the original input.",
    "reason": "The sequence is consistent with an enzyme, and sulfur-related enzyme chemistry might make some choices more plausible, but that does not meaningfully distinguish lipid metabolism from iron-sulfur cluster biosynthesis here. No clear sequence feature in the input identifies the specific cysteate-synthase activity or its connection to sulfonolipids; that functional link is needed to select D."
  },
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry explicitly assigns this protein to lipid metabolism. The annotation names cysteate synthase and cites a characterization paper, though the pathway assignment itself is a database annotation rather than direct experimental proof in these excerpts."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the evaluated model's input.",
    "The pathway annotation cites a characterization paper, but the excerpts do not independently establish the experimental basis for the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched annotation supports D, and the choices describe distinct pathways; no second choice is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry explicitly assigns this protein to lipid metabolism. The annotation names cysteate synthase and cites a characterization paper, though the pathway assignment itself is a database annotation rather than direct experimental proof in these excerpts.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The sequence's specific identification as cysteate synthase, with a role in producing a precursor for sulfonolipid (capnine) biosynthesis, is not provided in the original input.",
    "reason": "The sequence is consistent with an enzyme, and sulfur-related enzyme chemistry might make some choices more plausible, but that does not meaningfully distinguish lipid metabolism from iron-sulfur cluster biosynthesis here. No clear sequence feature in the input identifies the specific cysteate-synthase activity or its connection to sulfonolipids; that functional link is needed to select D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence-matched annotation supports D, and the choices describe distinct pathways; no second choice is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The reviewer-only source evidence was not part of the evaluated model's input.",
    "The pathway annotation cites a characterization paper, but the excerpts do not independently establish the experimental basis for the pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (C7M8J5) annotates the pathway as 'Lipid metabolism' (evidence IDs C5, H3) with curator-inferred evidence (ECO:0000305) citing PubMed:35414181, which characterized the biosynthetic pathway of the sulfonolipid Capnine. Cysteate synthase (EC 2.5.1.76) catalyzes a key step in sulfonolipid biosynthesis. Sulfonolipids are a recognized class of lipids, making the 'Lipid metabolism' pathway assignment scientifically appropriate. The EC number and catalytic activity are experimentally supported (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark motifs of the serine palmitoyltransferase (SPT) / cysteate synthase family of PLP-dependent enzymes: the 'CSGTGG' PLP-binding motif (residues ~170-176) and the conserved 'FADH' region (~280-283), which together with the ~333 aa length are characteristic of SPT-family enzymes. Transferable knowledge: SPT is the canonical PLP enzyme initiating sphingolipid (lipid) biosynthesis; cysteate synthase is its sulfonolipid-pathway homolog performing an analogous condensation. Recognizing the SPT-family signature from these motifs and knowing that SPT/cysteate synthase enzymes function in lipid (sphingolipid/sulfonolipid) biosynthesis meaningfully selects 'Lipid metabolism' (D). Option C (iron-sulfur cluster biosynthesis) is a plausible distractor because IscS/NifS are also PLP fold-type I enzymes, but IscS proteins are typically longer (~400-450 aa), lack the 'CSGTGG' and 'FADH' motif arrangement seen here, and have different active-site architectures. Option B (NAD synthetase reaction) involves an entirely different enzyme class with no PLP motif. Option A (cell wall biogenesis) is inconsistent with a PLP condensation enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the SPT/cysteate synthase family from the distinctive PLP-binding and FADH motifs, the ~333 aa length, and the overall fold-type I architecture. Family-level knowledge that SPT and its homologs (including cysteate synthase) catalyze the first committed step in lipid (sphingolipid or sulfonolipid) biosynthesis provides a concrete, transferable inference distinguishing D from the alternatives, particularly from the IscS/NifS distractor (C).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option C (iron-sulfur cluster biosynthesis) is the closest distractor due to IscS also being a PLP fold-type I enzyme, the specific 'CSGTGG' motif, 'FADH' region, and ~333 aa length are hallmarks of the SPT/cysteate synthase subfamily rather than IscS/NifS. This sequence-level distinction, combined with family-level functional knowledge, adequately separates D from C.


### Important caveats

- The pathway annotation uses curator-inferred evidence (ECO:0000305), not direct experimental proof that the enzyme's pathway is 'Lipid metabolism'; the experimental evidence (ECO:0000269) supports the EC number and catalytic activity, from which the lipid-pathway assignment is inferred.
- The reviewer-only evidence reveals the organism (Capnocytophaga ochracea) and exact identity (Cysteate synthase / capA), which were not available to the evaluated model. The reasoning argument relies solely on sequence motifs and transferable SPT-family knowledge.
- The 'FADH' motif in PLP fold-type I enzymes is a historical naming artifact (it is part of the PLP-binding region, not a true FAD-binding site); this does not affect the SPT-family identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the serine palmitoyltransferase (SPT) / cysteate synthase family of PLP-dependent enzymes: the 'CSGTGG' PLP-binding motif (residues ~170-176) and the conserved 'FADH' region (~280-283), which together with the ~333 aa length are characteristic of SPT-family enzymes. Transferable knowledge: SPT is the canonical PLP enzyme initiating sphingolipid (lipid) biosynthesis; cysteate synthase is its sulfonolipid-pathway homolog performing an analogous condensation. Recognizing the SPT-family signature from these motifs and knowing that SPT/cysteate synthase enzymes function in lipid (sphingolipid/sulfonolipid) biosynthesis meaningfully selects 'Lipid metabolism' (D). Option C (iron-sulfur cluster biosynthesis) is a plausible distractor because IscS/NifS are also PLP fold-type I enzymes, but IscS proteins are typically longer (~400-450 aa), lack the 'CSGTGG' and 'FADH' motif arrangement seen here, and have different active-site architectures. Option B (NAD synthetase reaction) involves an entirely different enzyme class with no PLP motif. Option A (cell wall biogenesis) is inconsistent with a PLP condensation enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SPT/cysteate synthase family from the distinctive PLP-binding and FADH motifs, the ~333 aa length, and the overall fold-type I architecture. Family-level knowledge that SPT and its homologs (including cysteate synthase) catalyze the first committed step in lipid (sphingolipid or sulfonolipid) biosynthesis provides a concrete, transferable inference distinguishing D from the alternatives, particularly from the IscS/NifS distractor (C)."
  },
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (C7M8J5) annotates the pathway as 'Lipid metabolism' (evidence IDs C5, H3) with curator-inferred evidence (ECO:0000305) citing PubMed:35414181, which characterized the biosynthetic pathway of the sulfonolipid Capnine. Cysteate synthase (EC 2.5.1.76) catalyzes a key step in sulfonolipid biosynthesis. Sulfonolipids are a recognized class of lipids, making the 'Lipid metabolism' pathway assignment scientifically appropriate. The EC number and catalytic activity are experimentally supported (ECO:0000269)."
  },
  "important_caveats": [
    "The pathway annotation uses curator-inferred evidence (ECO:0000305), not direct experimental proof that the enzyme's pathway is 'Lipid metabolism'; the experimental evidence (ECO:0000269) supports the EC number and catalytic activity, from which the lipid-pathway assignment is inferred.",
    "The reviewer-only evidence reveals the organism (Capnocytophaga ochracea) and exact identity (Cysteate synthase / capA), which were not available to the evaluated model. The reasoning argument relies solely on sequence motifs and transferable SPT-family knowledge.",
    "The 'FADH' motif in PLP fold-type I enzymes is a historical naming artifact (it is part of the PLP-binding region, not a true FAD-binding site); this does not affect the SPT-family identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (iron-sulfur cluster biosynthesis) is the closest distractor due to IscS also being a PLP fold-type I enzyme, the specific 'CSGTGG' motif, 'FADH' region, and ~333 aa length are hallmarks of the SPT/cysteate synthase subfamily rather than IscS/NifS. This sequence-level distinction, combined with family-level functional knowledge, adequately separates D from C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0124",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (C7M8J5) annotates the pathway as 'Lipid metabolism' (evidence IDs C5, H3) with curator-inferred evidence (ECO:0000305) citing PubMed:35414181, which characterized the biosynthetic pathway of the sulfonolipid Capnine. Cysteate synthase (EC 2.5.1.76) catalyzes a key step in sulfonolipid biosynthesis. Sulfonolipids are a recognized class of lipids, making the 'Lipid metabolism' pathway assignment scientifically appropriate. The EC number and catalytic activity are experimentally supported (ECO:0000269).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark motifs of the serine palmitoyltransferase (SPT) / cysteate synthase family of PLP-dependent enzymes: the 'CSGTGG' PLP-binding motif (residues ~170-176) and the conserved 'FADH' region (~280-283), which together with the ~333 aa length are characteristic of SPT-family enzymes. Transferable knowledge: SPT is the canonical PLP enzyme initiating sphingolipid (lipid) biosynthesis; cysteate synthase is its sulfonolipid-pathway homolog performing an analogous condensation. Recognizing the SPT-family signature from these motifs and knowing that SPT/cysteate synthase enzymes function in lipid (sphingolipid/sulfonolipid) biosynthesis meaningfully selects 'Lipid metabolism' (D). Option C (iron-sulfur cluster biosynthesis) is a plausible distractor because IscS/NifS are also PLP fold-type I enzymes, but IscS proteins are typically longer (~400-450 aa), lack the 'CSGTGG' and 'FADH' motif arrangement seen here, and have different active-site architectures. Option B (NAD synthetase reaction) involves an entirely different enzyme class with no PLP motif. Option A (cell wall biogenesis) is inconsistent with a PLP condensation enzyme.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the SPT/cysteate synthase family from the distinctive PLP-binding and FADH motifs, the ~333 aa length, and the overall fold-type I architecture. Family-level knowledge that SPT and its homologs (including cysteate synthase) catalyze the first committed step in lipid (sphingolipid or sulfonolipid) biosynthesis provides a concrete, transferable inference distinguishing D from the alternatives, particularly from the IscS/NifS distractor (C)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (iron-sulfur cluster biosynthesis) is the closest distractor due to IscS also being a PLP fold-type I enzyme, the specific 'CSGTGG' motif, 'FADH' region, and ~333 aa length are hallmarks of the SPT/cysteate synthase subfamily rather than IscS/NifS. This sequence-level distinction, combined with family-level functional knowledge, adequately separates D from C."
  },
  "important_caveats": [
    "The pathway annotation uses curator-inferred evidence (ECO:0000305), not direct experimental proof that the enzyme's pathway is 'Lipid metabolism'; the experimental evidence (ECO:0000269) supports the EC number and catalytic activity, from which the lipid-pathway assignment is inferred.",
    "The reviewer-only evidence reveals the organism (Capnocytophaga ochracea) and exact identity (Cysteate synthase / capA), which were not available to the evaluated model. The reasoning argument relies solely on sequence motifs and transferable SPT-family knowledge.",
    "The 'FADH' motif in PLP fold-type I enzymes is a historical naming artifact (it is part of the PLP-binding region, not a true FAD-binding site); this does not affect the SPT-family identification."
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
  "benchmark_sequence_length": 333,
  "benchmark_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "current_entry_audit": {
    "entryVersion": 67,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-10-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 333,
  "current_source_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 65,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C7M8J5",
  "selected_historical_entry_version": 65,
  "selected_historical_record_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "selected_historical_source_sequence_length": 333,
  "selected_historical_source_sequence_sha256": "27d70ef70b1e05efb4edd9f772e95f338a911fbeff53d81928bf3b959e4fbb62",
  "selected_historical_version": {
    "accession": "C7M8J5",
    "database": "Swiss-Prot",
    "entryVersion": 65,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAPA_CAPOD",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C7M8J5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":67,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-10-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Bacteroides ochraceus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Flavobacteriaceae\",\"Capnocytophaga\"],\"scientificName\":\"Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM 12966 / NCTC 12371 / SS31 / VPI 2845)\",\"taxonId\":521097}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.76\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"Cysteate synthase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"Lipid metabolism\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF LYS-241\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:27:35.457032+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6",
  "url": "https://rest.uniprot.org/uniprotkb/C7M8J5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H1",
  "excerpt": "ID   CAPA_CAPOD              Reviewed;         333 AA.\nAC   C7M8J5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-OCT-2009, sequence version 1.\nDT   28-JAN-2026, entry version 65.\nDE   RecName: Full=Cysteate synthase {ECO:0000303|PubMed:35414181};\nDE            EC=2.5.1.76 {ECO:0000269|PubMed:35414181};\nGN   Name=capA {ECO:0000303|PubMed:35414181};\nGN   OrderedLocusNames=Coch_1829 {ECO:0000312|EMBL:ACU93374.1};\nOS   Capnocytophaga ochracea (strain ATCC 27872 / DSM 7271 / CCUG 9716 / JCM\nOS   12966 / NCTC 12371 / SS31 / VPI 2845) (Bacteroides ochraceus).\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Flavobacteriaceae; Capnocytophaga.\nOX   NCBI_TaxID=521097;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   MUTAGENESIS OF LYS-241.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)

```json
{
  "entry_version": 65,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:40.735965+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110",
  "url": "https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 124. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
