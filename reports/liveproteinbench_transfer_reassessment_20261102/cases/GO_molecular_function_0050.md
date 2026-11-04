# GO_molecular_function_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0050.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — N6-methyladenosine-containing RNA reader activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGDAPLPPGSGKEFTQVQQQHNNYSNHQQQHAFASQYDMTQQQQPFGRGLSGPYNMGLMMHALPHPSYRPGQQQQHQYGSPPNTNGNAQPMPQAHGNNTMNSMPGPPQYYMQQQHGLPPQYYAQQMQGSQQQQQHQRGSMSPRANMALYQQPHTQGQQYYYPQGAQFPNHGPMPQNSMLAGPYPLASHMQHVDHRLAQRQVGDQRDVDNTEQSQPRVDGARFESQSNVVRGPPRKPRQSGHAIWIGNLPPQTDLMSLVYHVCKEAPGLESLFLISKSNCAFANFKDEEACISAQQKIHDSKFQTVRLVSRLRKSTVEGATGLTAPTGPAASAPQSNISQEVKGDALSVVTTTEDLIASSNVSSPKVTSPAPVETDRSAPQKEKYFILKSLTVEDLEQSIKTGIWATQAHNEKALNKAYETAESVYLIFSANKSGEYFGYARMTSQINEDPAAAVEFAPKAQAASDVALPKAIPTEANEYMPKGSIMDDSERGTIFWEADPPEDADGVDSNDTTTAAVADDTVSIKSCETGGPDSKVWGKPFQIEWLSVARLPFYRTRGIRNPWNSNREVKIARDGTELEPSVGRKLTGLFTSRGVGQLQQQPHPHHHHVMGGGMPMPGGMVHGYPPMYAQ

[Multiple Choices]
A. rRNA (uridine-N3-)-methyltransferase activity
B. snRNA methyltransferase activity
C. tetraketide alpha-pyrone synthase activity
D. N6-methyladenosine-containing RNA reader activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt record identifies the protein as a YTH-domain family protein and describes m6A-containing RNA recognition and binding. The function is qualified as inferred by similarity, and the GO annotation is computationally transferred, so this supports the key without constituting direct experimental demonstration of binding by this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a long low-complexity, glutamine/proline-rich region followed by a distinct globular C-terminal region consistent with a YTH-family RNA-binding domain. YTH domains are a transferable family feature associated with recognizing m6A-modified RNA, which meaningfully favors D. The methyltransferase choices imply catalytic RNA-modification functions, while the tetraketide synthase choice implies a different enzymatic protein class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family/domain-level inference from the sequence provides a concrete basis for distinguishing D among these options; knowing this exact protein's database entry is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered choices distinguish m6A-reader activity from unrelated methyltransferase and polyketide-synthase activities.


### Important caveats

- The reviewer-only annotation supports the key but describes the specific m6A-binding function as inferred by similarity; the cited experimental evidence concerns pathogenicity, not necessarily direct binding measurements for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a long low-complexity, glutamine/proline-rich region followed by a distinct globular C-terminal region consistent with a YTH-family RNA-binding domain. YTH domains are a transferable family feature associated with recognizing m6A-modified RNA, which meaningfully favors D. The methyltransferase choices imply catalytic RNA-modification functions, while the tetraketide synthase choice implies a different enzymatic protein class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family/domain-level inference from the sequence provides a concrete basis for distinguishing D among these options; knowing this exact protein's database entry is not necessary."
  },
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record identifies the protein as a YTH-domain family protein and describes m6A-containing RNA recognition and binding. The function is qualified as inferred by similarity, and the GO annotation is computationally transferred, so this supports the key without constituting direct experimental demonstration of binding by this exact protein."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but describes the specific m6A-binding function as inferred by similarity; the cited experimental evidence concerns pathogenicity, not necessarily direct binding measurements for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish m6A-reader activity from unrelated methyltransferase and polyketide-synthase activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record identifies the protein as a YTH-domain family protein and describes m6A-containing RNA recognition and binding. The function is qualified as inferred by similarity, and the GO annotation is computationally transferred, so this supports the key without constituting direct experimental demonstration of binding by this exact protein.",
    "evidence_ids": ["C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a long low-complexity, glutamine/proline-rich region followed by a distinct globular C-terminal region consistent with a YTH-family RNA-binding domain. YTH domains are a transferable family feature associated with recognizing m6A-modified RNA, which meaningfully favors D. The methyltransferase choices imply catalytic RNA-modification functions, while the tetraketide synthase choice implies a different enzymatic protein class.",
    "missing_item_specific_fact": "",
    "reason": "A family/domain-level inference from the sequence provides a concrete basis for distinguishing D among these options; knowing this exact protein's database entry is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered choices distinguish m6A-reader activity from unrelated methyltransferase and polyketide-synthase activities."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but describes the specific m6A-binding function as inferred by similarity; the cited experimental evidence concerns pathogenicity, not necessarily direct binding measurements for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G4MRQ6) annotates this protein as 'YTH domain-containing family protein 1' with GO:1990247 (N6-methyladenosine-containing RNA reader activity). The FUNCTION comment states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' with evidence from by-similarity (ECO:0000250) and one PubMed reference (30535195). The GO annotation uses IEA:TreeGrafter (computational inference). While the primary evidence is computational/by-similarity rather than direct experimental characterization of this exact protein, the annotation is consistent with the expected answer and supported by the cited publication on m6A RNA methylation in Pyricularia oryzae.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The YTH domain is one of the most well-characterized protein families in RNA biology, found in YTHDF1-3, YTHDC1-2, and homologs across eukaryotes. Key transferable features include: (1) an aromatic cage typically formed by 3 conserved tryptophans that accommodate the m6A methyl group — the sequence shows multiple tryptophans clustered in the C-terminal structured region (GIWAT, IFWEAD, DSKVWG, IEWLSV, RTRGIRNPWNSNRE); (2) a ~130-140 aa structured domain flanked by low-complexity regions (poly-Q, poly-P stretches visible in the N-terminal half), matching YTH protein architecture; (3) the absence of any SAM-binding methyltransferase motifs (e.g., VLDIGVG-type) needed for options A and B, and absence of polyketide synthase KS/AT/ACP domains needed for option C. A knowledgeable model can eliminate A (rRNA uridine-N3-methyltransferase) and B (snRNA methyltransferase) because neither catalytic methyltransferase fold nor SAM-binding motifs are present, and eliminate C (tetraketide alpha-pyrone synthase) because polyketide synthase domains are absent. The tryptophan-rich structured domain in an RNA-biology context strongly points to a reader/binder (D) rather than a catalyst (A, B, C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The YTH domain family is extensively characterized across many organisms and proteins. The sequence features (aromatic cage tryptophans, domain architecture with flanking low-complexity regions, absence of methyltransferase or PKS motifs) provide a credible transferable inference from well-known YTH family biology. The alternatives A, B, and C require entirely different domain architectures (SAM-binding catalytic fold, polyketide synthase modules) that are clearly absent from this sequence. This constitutes legitimate family-level pattern recognition.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular activities: two methyltransferase catalytic activities (A, B), one polyketide synthase activity (C), and one reader/binding activity (D). The sequence lacks any catalytic methyltransferase or PKS domain features, making A, B, and C clearly incompatible. Only D (a binding/reader activity) is consistent with the observed domain architecture.


### Important caveats

- The GO annotation for this protein is IEA:TreeGrafter (computational inference by homology), not direct experimental evidence for this exact protein.
- The FUNCTION comment combines 'By similarity' (to another YTH protein, A0A9P4XWM4) with one PubMed reference (30535195) that demonstrates a role in pathogenicity but primarily establishes m6A involvement in virulence rather than direct m6A-binding assays on this specific protein.
- The YTH domain is moderately conserved at the sequence level; primary-sequence recognition without domain databases is challenging but the tryptophan clustering and overall architecture provide reasonable family-level cues.
- The protein is from Pyricularia oryzae (fungal YTH homolog); fungal YTH proteins are less extensively characterized than mammalian YTHDF/YTHDC proteins, but the domain fold and function are conserved.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The YTH domain is one of the most well-characterized protein families in RNA biology, found in YTHDF1-3, YTHDC1-2, and homologs across eukaryotes. Key transferable features include: (1) an aromatic cage typically formed by 3 conserved tryptophans that accommodate the m6A methyl group — the sequence shows multiple tryptophans clustered in the C-terminal structured region (GIWAT, IFWEAD, DSKVWG, IEWLSV, RTRGIRNPWNSNRE); (2) a ~130-140 aa structured domain flanked by low-complexity regions (poly-Q, poly-P stretches visible in the N-terminal half), matching YTH protein architecture; (3) the absence of any SAM-binding methyltransferase motifs (e.g., VLDIGVG-type) needed for options A and B, and absence of polyketide synthase KS/AT/ACP domains needed for option C. A knowledgeable model can eliminate A (rRNA uridine-N3-methyltransferase) and B (snRNA methyltransferase) because neither catalytic methyltransferase fold nor SAM-binding motifs are present, and eliminate C (tetraketide alpha-pyrone synthase) because polyketide synthase domains are absent. The tryptophan-rich structured domain in an RNA-biology context strongly points to a reader/binder (D) rather than a catalyst (A, B, C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The YTH domain family is extensively characterized across many organisms and proteins. The sequence features (aromatic cage tryptophans, domain architecture with flanking low-complexity regions, absence of methyltransferase or PKS motifs) provide a credible transferable inference from well-known YTH family biology. The alternatives A, B, and C require entirely different domain architectures (SAM-binding catalytic fold, polyketide synthase modules) that are clearly absent from this sequence. This constitutes legitimate family-level pattern recognition."
  },
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H3",
      "H5",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G4MRQ6) annotates this protein as 'YTH domain-containing family protein 1' with GO:1990247 (N6-methyladenosine-containing RNA reader activity). The FUNCTION comment states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' with evidence from by-similarity (ECO:0000250) and one PubMed reference (30535195). The GO annotation uses IEA:TreeGrafter (computational inference). While the primary evidence is computational/by-similarity rather than direct experimental characterization of this exact protein, the annotation is consistent with the expected answer and supported by the cited publication on m6A RNA methylation in Pyricularia oryzae."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:TreeGrafter (computational inference by homology), not direct experimental evidence for this exact protein.",
    "The FUNCTION comment combines 'By similarity' (to another YTH protein, A0A9P4XWM4) with one PubMed reference (30535195) that demonstrates a role in pathogenicity but primarily establishes m6A involvement in virulence rather than direct m6A-binding assays on this specific protein.",
    "The YTH domain is moderately conserved at the sequence level; primary-sequence recognition without domain databases is challenging but the tryptophan clustering and overall architecture provide reasonable family-level cues.",
    "The protein is from Pyricularia oryzae (fungal YTH homolog); fungal YTH proteins are less extensively characterized than mammalian YTHDF/YTHDC proteins, but the domain fold and function are conserved."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular activities: two methyltransferase catalytic activities (A, B), one polyketide synthase activity (C), and one reader/binding activity (D). The sequence lacks any catalytic methyltransferase or PKS domain features, making A, B, and C clearly incompatible. Only D (a binding/reader activity) is consistent with the observed domain architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G4MRQ6) annotates this protein as 'YTH domain-containing family protein 1' with GO:1990247 (N6-methyladenosine-containing RNA reader activity). The FUNCTION comment states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs' with evidence from by-similarity (ECO:0000250) and one PubMed reference (30535195). The GO annotation uses IEA:TreeGrafter (computational inference). While the primary evidence is computational/by-similarity rather than direct experimental characterization of this exact protein, the annotation is consistent with the expected answer and supported by the cited publication on m6A RNA methylation in Pyricularia oryzae.",
    "evidence_ids": ["C4", "C5", "C7", "H3", "H5", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The YTH domain is one of the most well-characterized protein families in RNA biology, found in YTHDF1-3, YTHDC1-2, and homologs across eukaryotes. Key transferable features include: (1) an aromatic cage typically formed by 3 conserved tryptophans that accommodate the m6A methyl group — the sequence shows multiple tryptophans clustered in the C-terminal structured region (GIWAT, IFWEAD, DSKVWG, IEWLSV, RTRGIRNPWNSNRE); (2) a ~130-140 aa structured domain flanked by low-complexity regions (poly-Q, poly-P stretches visible in the N-terminal half), matching YTH protein architecture; (3) the absence of any SAM-binding methyltransferase motifs (e.g., VLDIGVG-type) needed for options A and B, and absence of polyketide synthase KS/AT/ACP domains needed for option C. A knowledgeable model can eliminate A (rRNA uridine-N3-methyltransferase) and B (snRNA methyltransferase) because neither catalytic methyltransferase fold nor SAM-binding motifs are present, and eliminate C (tetraketide alpha-pyrone synthase) because polyketide synthase domains are absent. The tryptophan-rich structured domain in an RNA-biology context strongly points to a reader/binder (D) rather than a catalyst (A, B, C).",
    "missing_item_specific_fact": "",
    "reason": "The YTH domain family is extensively characterized across many organisms and proteins. The sequence features (aromatic cage tryptophans, domain architecture with flanking low-complexity regions, absence of methyltransferase or PKS motifs) provide a credible transferable inference from well-known YTH family biology. The alternatives A, B, and C require entirely different domain architectures (SAM-binding catalytic fold, polyketide synthase modules) that are clearly absent from this sequence. This constitutes legitimate family-level pattern recognition."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular activities: two methyltransferase catalytic activities (A, B), one polyketide synthase activity (C), and one reader/binding activity (D). The sequence lacks any catalytic methyltransferase or PKS domain features, making A, B, and C clearly incompatible. Only D (a binding/reader activity) is consistent with the observed domain architecture."
  },
  "important_caveats": [
    "The GO annotation for this protein is IEA:TreeGrafter (computational inference by homology), not direct experimental evidence for this exact protein.",
    "The FUNCTION comment combines 'By similarity' (to another YTH protein, A0A9P4XWM4) with one PubMed reference (30535195) that demonstrates a role in pathogenicity but primarily establishes m6A involvement in virulence rather than direct m6A-binding assays on this specific protein.",
    "The YTH domain is moderately conserved at the sequence level; primary-sequence recognition without domain databases is challenging but the tryptophan clustering and overall architecture provide reasonable family-level cues.",
    "The protein is from Pyricularia oryzae (fungal YTH homolog); fungal YTH proteins are less extensively characterized than mammalian YTHDF/YTHDC proteins, but the domain fold and function are conserved."
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
  "benchmark_sequence_length": 630,
  "benchmark_sequence_sha256": "e8a11d01832120f9a13087099eed687cfa578ca456019f1c189df807f5e113e5",
  "current_entry_audit": {
    "entryVersion": 50,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 630,
  "current_source_sequence_sha256": "e8a11d01832120f9a13087099eed687cfa578ca456019f1c189df807f5e113e5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 50,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4MRQ6",
  "selected_historical_entry_version": 50,
  "selected_historical_record_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "selected_historical_source_sequence_length": 630,
  "selected_historical_source_sequence_sha256": "e8a11d01832120f9a13087099eed687cfa578ca456019f1c189df807f5e113e5",
  "selected_historical_version": {
    "accession": "G4MRQ6",
    "database": "Swiss-Prot",
    "entryVersion": 50,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "YTH1_PYRO7",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4MRQ6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":50,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"M6A reader YTH1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30535195\",\"source\":\"PubMed\"}],\"value\":\"YTH domain-containing family protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A9P4XWM4\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30535195\",\"source\":\"PubMed\"}],\"value\":\"Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability (By similarity). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (By similarity). Plays a role in pathogenicity towards plant host (PubMed:30535195)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003729\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:mRNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:1990247\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:N6-methyladenosine-containing RNA reader activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MRQ6.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi Y.\",\"Wang H.\",\"Wang J.\",\"Liu X.\",\"Lin F.\",\"Lu J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30535195\"},{\"database\":\"DOI\",\"id\":\"10.1093/femsle/fny286\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30535195\",\"journal\":\"FEMS Microbiol. Lett.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"N6-methyladenosine RNA methylation is involved in virulence of the rice blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\",\"volume\":\"366\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:40.980195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1253cf7758fed16034da0ace21eaedef9d586c60bf29ed9cf5d2a587b7427c4a",
  "url": "https://rest.uniprot.org/uniprotkb/G4MRQ6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H1",
  "excerpt": "ID   YTH1_PYRO7              Reviewed;         630 AA.\nAC   G4MRQ6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 50.\nDE   RecName: Full=YTH domain-containing family protein 1 {ECO:0000303|PubMed:30535195};\nDE   AltName: Full=M6A reader YTH1 {ECO:0000305};\nGN   Name=YTH1 {ECO:0000303|PubMed:30535195}; ORFNames=MGG_04621;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:43.231635+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "url": "https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=30535195; DOI=10.1093/femsle/fny286;\nRA   Shi Y., Wang H., Wang J., Liu X., Lin F., Lu J.;\nRT   \"N6-methyladenosine RNA methylation is involved in virulence of the rice\nRT   blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\";\nRL   FEMS Microbiol. Lett. 366:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:43.231635+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "url": "https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Specifically recognizes and binds N6-methyladenosine (m6A)-\nCC       containing mRNAs, and regulates their stability (By similarity). M6A is\nCC       a modification present at internal sites of mRNAs and some non-coding\nCC       RNAs and plays a role in mRNA stability and processing (By similarity).\nCC       Plays a role in pathogenicity towards plant host (PubMed:30535195).\nCC       {ECO:0000250|UniProtKB:A0A9P4XWM4, ECO:0000269|PubMed:30535195}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:43.231635+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "url": "https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0003729; F:mRNA binding; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:43.231635+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "url": "https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:1990247; F:N6-methyladenosine-containing RNA reader activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:43.231635+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0e3fd045231c72df6a89528c9ea84aac218d1c347b0c4633352bdbffaaf288d9",
  "url": "https://rest.uniprot.org/unisave/G4MRQ6?format=txt&versions=50"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0070042\nname: rRNA (uridine-N3-)-methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: S-adenosyl-L-methionine + rRNA = S-adenosyl-L-homocysteine + rRNA containing N3-methyluridine.\" [GOC:imk, GOC:mah]\nis_a: GO:0008170 ! N-methyltransferase activity\nis_a: GO:0016436 ! rRNA (uridine) methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0070042",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 363692-363699",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0090439\nname: tetraketide alpha-pyrone synthase activity\nnamespace: molecular_function\ndef: \"Catalyzes the reaction: 7-hydroxylauroyl-CoA + 3 malonyl-CoA + 2 H+ = 2-(8-hydroxy-2-oxotridecyl)-6-oxopyran-4-olate + 3 CO2 + 4 coenzyme A.\" [MetaCyc:RXN-16407, PMID:21193570]\nxref: MetaCyc:RXN-16407\nis_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups\nproperty_value: skos:exactMatch MetaCyc:RXN-16407\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0090439",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 399100-399108",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0106346\nname: snRNA methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group from a donor to a nucleoside residue in an snRNA molecule.\" [PMID:27573892]\nis_a: GO:0008173 ! RNA methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106346",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 429765-429771",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:1990247\nname: N6-methyladenosine-containing RNA reader activity\nnamespace: molecular_function\ndef: \"A protein adaptor that recognizes and binds an RNA molecule modified by N6-methyladenosine (m6A), a modification present at internal sites of mRNAs and some non-coding RNAs.\" [PMID:22575960, PMID:24284625]\nsynonym: \"N6-methyladenosine-containing RNA binding\" RELATED []\nis_a: GO:0140517 ! protein-RNA adaptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990247",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 550531-550538",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
