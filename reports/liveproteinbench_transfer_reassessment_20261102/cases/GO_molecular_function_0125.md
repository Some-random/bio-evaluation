# GO_molecular_function_0125

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0125.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — RNA binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWPNLFWGFDAYDGSNFNAFPIYFPTEFMQTEPRDQSSCQQLSMEQATEPSMNPDQEDIVEGGENYGELSNQQETVPSFENADQNLSRLEMSTLARELKEKVKQSRALRQSVNNAAEQQPSTKPQPVQQEVQDLINDILKSQDQDDNLKNPSKLTGPQDDTETEKPASTLPTTPRTIKESPLSTYSIPVYCPASPEGRTHIPDEILDNAPKGPRHTHRGQVQMFCNGECGRRETDKAMPAIEPSDKTEETEGATAVRIPPVATDGDLEQDVIMWLRHTGFYDKAKRTDALARWKQLAKMEQGLARPQQDHQEAGVALASASQGSKEAGMGTRPGPDADCPPVCRPEQGGPGSSQAALSCKSKQSTDIQRATLAETRGGSLRDRAANQQPSKKSDRGRCARRHRSSSPRGRSGSHKSRRATTDSPVSRSTTKSTPSRARQPGHRDYREYRDDRNRDTKPRSPLVSCRAAVAFNPGVKGAPLVRQRFRPRQTNTDLQHKARIVGAPPRDMESNIKERQNHDPERQSGQFGIRWLCTSPLALQNTKSLRNSFDDLKPVLLGRDGQEMDDYCGRDLLRLMDASERGLHRP

[Multiple Choices]
A. magnesium ion binding
B. olfactory receptor activity
C. RNA binding
D. nicotinate-nucleotide adenylyltransferase activity
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

> The sequence-matched entry describes a YTH-domain protein that recognizes and binds m6A-containing mRNAs, and annotates RNA binding. The functional description is supported partly by similarity, while the GO annotation is computational; these support the broad RNA-binding choice but do not by themselves establish every detail experimentally.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a C-terminal folded-domain region and an architecture consistent with YTH-family m6A reader proteins; transferable knowledge of this family connects it to binding RNA. That meaningfully favors C over the alternatives: an olfactory receptor would typically have multiple membrane-spanning segments, and nicotinate-nucleotide adenylyltransferase activity would require an enzyme-family signature rather than a YTH reader domain. Magnesium binding could occur incidentally in many proteins, but does not explain this family-level pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can distinguish RNA binding among these choices without knowing this exact protein's database record. This is a credible inference rather than certainty from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> RNA binding is the only offered choice that fits the YTH-reader family inference; incidental ion binding does not make magnesium binding an equally defensible primary function.


### Important caveats

- The supplied annotation describes m6A-containing RNA binding partly by similarity, and the GO term is computationally assigned; the evidence supports the broad choice, not necessarily direct experimental validation of every functional detail.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a C-terminal folded-domain region and an architecture consistent with YTH-family m6A reader proteins; transferable knowledge of this family connects it to binding RNA. That meaningfully favors C over the alternatives: an olfactory receptor would typically have multiple membrane-spanning segments, and nicotinate-nucleotide adenylyltransferase activity would require an enzyme-family signature rather than a YTH reader domain. Magnesium binding could occur incidentally in many proteins, but does not explain this family-level pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish RNA binding among these choices without knowing this exact protein's database record. This is a credible inference rather than certainty from sequence alone."
  },
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry describes a YTH-domain protein that recognizes and binds m6A-containing mRNAs, and annotates RNA binding. The functional description is supported partly by similarity, while the GO annotation is computational; these support the broad RNA-binding choice but do not by themselves establish every detail experimentally."
  },
  "important_caveats": [
    "The supplied annotation describes m6A-containing RNA binding partly by similarity, and the GO term is computationally assigned; the evidence supports the broad choice, not necessarily direct experimental validation of every functional detail."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "RNA binding is the only offered choice that fits the YTH-reader family inference; incidental ion binding does not make magnesium binding an equally defensible primary function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry describes a YTH-domain protein that recognizes and binds m6A-containing mRNAs, and annotates RNA binding. The functional description is supported partly by similarity, while the GO annotation is computational; these support the broad RNA-binding choice but do not by themselves establish every detail experimentally.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a C-terminal folded-domain region and an architecture consistent with YTH-family m6A reader proteins; transferable knowledge of this family connects it to binding RNA. That meaningfully favors C over the alternatives: an olfactory receptor would typically have multiple membrane-spanning segments, and nicotinate-nucleotide adenylyltransferase activity would require an enzyme-family signature rather than a YTH reader domain. Magnesium binding could occur incidentally in many proteins, but does not explain this family-level pattern.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish RNA binding among these choices without knowing this exact protein's database record. This is a credible inference rather than certainty from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "RNA binding is the only offered choice that fits the YTH-reader family inference; incidental ion binding does not make magnesium binding an equally defensible primary function."
  },
  "important_caveats": [
    "The supplied annotation describes m6A-containing RNA binding partly by similarity, and the GO term is computationally assigned; the evidence supports the broad choice, not necessarily direct experimental validation of every functional detail."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G4NB33) identifies this protein as 'YTH domain-containing family protein 2' (M6A reader YTH2) from Pyricularia oryzae. The functional annotation states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability.' The GO annotation GO:0003723 (RNA binding) is recorded with IEA:InterPro evidence, and the PubMed reference (30535195) supports the m6A-binding function. RNA binding is the well-established molecular function of YTH domain proteins across eukaryotes.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The YTH domain is a highly conserved ~140-residue RNA-binding domain found across eukaryotes (human YTHDF1-3, YTHDC1-2, plant and fungal homologs). Key transferable features include: (1) a conserved aromatic cage formed by tryptophan/phenylalanine residues that recognizes the m6A methyl group, visible in the sequence as conserved Trp residues (e.g., in 'IMWLRHTGFY' and 'LARWKQ'); (2) a characteristic β-sheet/α-helix fold with specific loop architectures for nucleotide reading; (3) flanking intrinsically disordered regions typical of YTH proteins. A model recognizing this domain family from homologs in other organisms would infer RNA binding. The distractors are clearly eliminable: olfactory receptor activity (B) requires 7-transmembrane GPCR topology absent here; nicotinate-nucleotide adenylyltransferase (D) requires specific catalytic motifs (e.g., the NMNAT fold with conserved Asp/Glu for Mg coordination and transfer) absent in this sequence; magnesium ion binding (A) as a primary function requires dedicated metal-binding motifs (EF-hands, DxDxDG) not evident. The YTH domain family knowledge transfers directly to the RNA-binding assignment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the YTH domain family from conserved sequence features (aromatic cage residues, domain architecture, flanking disordered regions) is well-established transferable knowledge from human and other eukaryotic YTH proteins. This family-level inference directly supports RNA binding over the other three options, which require structurally or mechanistically incompatible features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent mechanistically distinct molecular functions. Olfactory receptor activity requires 7TM topology, nicotinate-nucleotide adenylyltransferase requires specific catalytic motifs, and magnesium ion binding as a primary function requires dedicated metal-binding sites. None of these are present in the sequence. The YTH domain's RNA-binding role is unambiguous among the choices.


### Important caveats

- The GO RNA binding annotation carries IEA:InterPro (computational inference) evidence, not direct experimental binding data for this specific fungal protein. However, the YTH domain family's RNA-binding function is extensively validated experimentally in other organisms.
- The PubMed reference (30535195) supports the m6A role in pathogenicity but the direct RNA-binding evidence for this specific protein is by similarity to other YTH proteins.
- Sequence-based YTH domain recognition depends on the model having encountered YTH domain homologs during training; the domain is well-represented in databases.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The YTH domain is a highly conserved ~140-residue RNA-binding domain found across eukaryotes (human YTHDF1-3, YTHDC1-2, plant and fungal homologs). Key transferable features include: (1) a conserved aromatic cage formed by tryptophan/phenylalanine residues that recognizes the m6A methyl group, visible in the sequence as conserved Trp residues (e.g., in 'IMWLRHTGFY' and 'LARWKQ'); (2) a characteristic β-sheet/α-helix fold with specific loop architectures for nucleotide reading; (3) flanking intrinsically disordered regions typical of YTH proteins. A model recognizing this domain family from homologs in other organisms would infer RNA binding. The distractors are clearly eliminable: olfactory receptor activity (B) requires 7-transmembrane GPCR topology absent here; nicotinate-nucleotide adenylyltransferase (D) requires specific catalytic motifs (e.g., the NMNAT fold with conserved Asp/Glu for Mg coordination and transfer) absent in this sequence; magnesium ion binding (A) as a primary function requires dedicated metal-binding motifs (EF-hands, DxDxDG) not evident. The YTH domain family knowledge transfers directly to the RNA-binding assignment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the YTH domain family from conserved sequence features (aromatic cage residues, domain architecture, flanking disordered regions) is well-established transferable knowledge from human and other eukaryotic YTH proteins. This family-level inference directly supports RNA binding over the other three options, which require structurally or mechanistically incompatible features."
  },
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G4NB33) identifies this protein as 'YTH domain-containing family protein 2' (M6A reader YTH2) from Pyricularia oryzae. The functional annotation states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability.' The GO annotation GO:0003723 (RNA binding) is recorded with IEA:InterPro evidence, and the PubMed reference (30535195) supports the m6A-binding function. RNA binding is the well-established molecular function of YTH domain proteins across eukaryotes."
  },
  "important_caveats": [
    "The GO RNA binding annotation carries IEA:InterPro (computational inference) evidence, not direct experimental binding data for this specific fungal protein. However, the YTH domain family's RNA-binding function is extensively validated experimentally in other organisms.",
    "The PubMed reference (30535195) supports the m6A role in pathogenicity but the direct RNA-binding evidence for this specific protein is by similarity to other YTH proteins.",
    "Sequence-based YTH domain recognition depends on the model having encountered YTH domain homologs during training; the domain is well-represented in databases."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct molecular functions. Olfactory receptor activity requires 7TM topology, nicotinate-nucleotide adenylyltransferase requires specific catalytic motifs, and magnesium ion binding as a primary function requires dedicated metal-binding sites. None of these are present in the sequence. The YTH domain's RNA-binding role is unambiguous among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G4NB33) identifies this protein as 'YTH domain-containing family protein 2' (M6A reader YTH2) from Pyricularia oryzae. The functional annotation states it 'Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability.' The GO annotation GO:0003723 (RNA binding) is recorded with IEA:InterPro evidence, and the PubMed reference (30535195) supports the m6A-binding function. RNA binding is the well-established molecular function of YTH domain proteins across eukaryotes.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The YTH domain is a highly conserved ~140-residue RNA-binding domain found across eukaryotes (human YTHDF1-3, YTHDC1-2, plant and fungal homologs). Key transferable features include: (1) a conserved aromatic cage formed by tryptophan/phenylalanine residues that recognizes the m6A methyl group, visible in the sequence as conserved Trp residues (e.g., in 'IMWLRHTGFY' and 'LARWKQ'); (2) a characteristic β-sheet/α-helix fold with specific loop architectures for nucleotide reading; (3) flanking intrinsically disordered regions typical of YTH proteins. A model recognizing this domain family from homologs in other organisms would infer RNA binding. The distractors are clearly eliminable: olfactory receptor activity (B) requires 7-transmembrane GPCR topology absent here; nicotinate-nucleotide adenylyltransferase (D) requires specific catalytic motifs (e.g., the NMNAT fold with conserved Asp/Glu for Mg coordination and transfer) absent in this sequence; magnesium ion binding (A) as a primary function requires dedicated metal-binding motifs (EF-hands, DxDxDG) not evident. The YTH domain family knowledge transfers directly to the RNA-binding assignment.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the YTH domain family from conserved sequence features (aromatic cage residues, domain architecture, flanking disordered regions) is well-established transferable knowledge from human and other eukaryotic YTH proteins. This family-level inference directly supports RNA binding over the other three options, which require structurally or mechanistically incompatible features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent mechanistically distinct molecular functions. Olfactory receptor activity requires 7TM topology, nicotinate-nucleotide adenylyltransferase requires specific catalytic motifs, and magnesium ion binding as a primary function requires dedicated metal-binding sites. None of these are present in the sequence. The YTH domain's RNA-binding role is unambiguous among the choices."
  },
  "important_caveats": [
    "The GO RNA binding annotation carries IEA:InterPro (computational inference) evidence, not direct experimental binding data for this specific fungal protein. However, the YTH domain family's RNA-binding function is extensively validated experimentally in other organisms.",
    "The PubMed reference (30535195) supports the m6A role in pathogenicity but the direct RNA-binding evidence for this specific protein is by similarity to other YTH proteins.",
    "Sequence-based YTH domain recognition depends on the model having encountered YTH domain homologs during training; the domain is well-represented in databases."
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
  "benchmark_sequence_length": 586,
  "benchmark_sequence_sha256": "718d8a3ac5ea539fcbbd3f521572126f1d1934d09b81f683b9d32bd5a5265845",
  "current_entry_audit": {
    "entryVersion": 42,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-01-28",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 586,
  "current_source_sequence_sha256": "718d8a3ac5ea539fcbbd3f521572126f1d1934d09b81f683b9d32bd5a5265845",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 42,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4NB33",
  "selected_historical_entry_version": 42,
  "selected_historical_record_sha256": "230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2",
  "selected_historical_source_sequence_length": 586,
  "selected_historical_source_sequence_sha256": "718d8a3ac5ea539fcbbd3f521572126f1d1934d09b81f683b9d32bd5a5265845",
  "selected_historical_version": {
    "accession": "G4NB33",
    "database": "Swiss-Prot",
    "entryVersion": 42,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_03/2026_03",
    "lastReleaseDate": "02-Sep-2026",
    "name": "YTH2_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4NB33\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":42,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-01-28\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"M6A reader YTH2\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30535195\",\"source\":\"PubMed\"}],\"value\":\"YTH domain-containing family protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A9P4XWM4\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30535195\",\"source\":\"PubMed\"}],\"value\":\"Specifically recognizes and binds N6-methyladenosine (m6A)-containing mRNAs, and regulates their stability (By similarity). M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in mRNA stability and processing (By similarity). Plays a role in pathogenicity towards plant host (PubMed:30535195)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003723\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:RNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NB33.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Shi Y.\",\"Wang H.\",\"Wang J.\",\"Liu X.\",\"Lin F.\",\"Lu J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30535195\"},{\"database\":\"DOI\",\"id\":\"10.1093/femsle/fny286\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30535195\",\"journal\":\"FEMS Microbiol. Lett.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"N6-methyladenosine RNA methylation is involved in virulence of the rice blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\",\"volume\":\"366\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:07.149739+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "12d384b1b63c01ae54789687c2477c5a4dedf554ec7ee6db71b77e36b31c2d45",
  "url": "https://rest.uniprot.org/uniprotkb/G4NB33.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H1",
  "excerpt": "ID   YTH2_PYRO7              Reviewed;         586 AA.\nAC   G4NB33;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 42.\nDE   RecName: Full=YTH domain-containing family protein 2 {ECO:0000303|PubMed:30535195};\nDE   AltName: Full=M6A reader YTH2 {ECO:0000305};\nGN   Name=YTH2 {ECO:0000303|PubMed:30535195}; ORFNames=MGG_00637;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.832385+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2",
  "url": "https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=30535195; DOI=10.1093/femsle/fny286;\nRA   Shi Y., Wang H., Wang J., Liu X., Lin F., Lu J.;\nRT   \"N6-methyladenosine RNA methylation is involved in virulence of the rice\nRT   blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).\";\nRL   FEMS Microbiol. Lett. 366:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.832385+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2",
  "url": "https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Specifically recognizes and binds N6-methyladenosine (m6A)-\nCC       containing mRNAs, and regulates their stability (By similarity). M6A is\nCC       a modification present at internal sites of mRNAs and some non-coding\nCC       RNAs and plays a role in mRNA stability and processing (By similarity).\nCC       Plays a role in pathogenicity towards plant host (PubMed:30535195).\nCC       {ECO:0000250|UniProtKB:A0A9P4XWM4, ECO:0000269|PubMed:30535195}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.832385+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2",
  "url": "https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42)

```json
{
  "entry_version": 42,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0003723; F:RNA binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:05.832385+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "230bc6ccb816d8ed7059ee0b42ed0d37caff3a2e8ab4e2e4c89efbb6f5954ec2",
  "url": "https://rest.uniprot.org/unisave/G4NB33?format=txt&versions=42"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000287\nname: magnesium ion binding\nnamespace: molecular_function\ndef: \"Binding to a magnesium (Mg) ion.\" [GOC:ai]\nsynonym: \"magnesium binding\" EXACT []\nsynonym: \"Mg binding\" EXACT []\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000287",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 3126-3134",
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
  "excerpt": "[Term]\nid: GO:0003723\nname: RNA binding\nnamespace: molecular_function\nalt_id: GO:0000498\nalt_id: GO:0044822\ndef: \"Binding to an RNA molecule or a portion thereof.\" [GOC:jl, GOC:mah]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"base pairing with RNA\" NARROW []\nsynonym: \"poly(A) RNA binding\" RELATED []\nsynonym: \"poly(A)-RNA binding\" RELATED []\nsynonym: \"poly-A RNA binding\" RELATED []\nxref: Reactome:R-HSA-203922 \"Exportin-5 recognizes 3' overhang of pre-miRNA\"\nis_a: GO:0003676 ! nucleic acid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003723",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28242-28268",
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
  "excerpt": "[Term]\nid: GO:0004515\nname: nicotinate-nucleotide adenylyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: nicotinate beta-D-ribonucleotide + ATP + H+ = deamido-NAD+ + diphosphate.\" [RHEA:22860]\nsynonym: \"ATP:nicotinate-nucleotide adenylyltransferase activity\" EXACT []\nsynonym: \"ATP:nicotinate-ribonucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) diphosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD+ pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamidonicotinamide adenine dinucleotide pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"NaMN-ATase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinate mononucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinic acid mononucleotide adenylyltransferase\" NARROW []\nxref: EC:2.7.7.18\nxref: MetaCyc:NICONUCADENYLYLTRAN-RXN\nxref: Reactome:R-HSA-197235 \"NMNAT2 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200474 \"NMNAT3 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200512 \"NMNAT1 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: RHEA:22860\nis_a: GO:0070566 ! adenylyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.7.18\nproperty_value: skos:exactMatch MetaCyc:NICONUCADENYLYLTRAN-RXN\nproperty_value: skos:exactMatch RHEA:22860\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004515",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 43770-43794",
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
  "excerpt": "[Term]\nid: GO:0004984\nname: olfactory receptor activity\nnamespace: molecular_function\ndef: \"Combining with an odorant and transmitting the signal from one side of the membrane to the other to initiate a change in cell activity in response to detection of smell.\" [GOC:bf, GOC:dph, GOC:sart, PMID:19135896, PMID:21041441]\nsynonym: \"odorant receptor activity\" EXACT [PMID:19135896, PMID:21041441]\nis_a: GO:0004888 ! transmembrane signaling receptor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004984",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 52529-52536",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
