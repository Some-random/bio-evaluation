# GO_molecular_function_0116

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0116.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — transcription cis-regulatory region binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDLANTAERRGEKRPAGGNRRGNRLPRDERRGQLLIAASEVFVDRGYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLQRHVDNLVSGVRQALRTTTDNRQRLRAAVEAFFDFIEHDSQGYRLIFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWLNNDRPIDKDSAVEGTVQFAWGGLSHVPLTRS

[Multiple Choices]
A. ATPase-coupled transmembrane transporter activity
B. RNA polymerase II cis-regulatory region sequence-specific DNA binding
C. transcription cis-regulatory region binding
D. quercetin 7-O-glucosyltransferase activity
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

> The matched-sequence UniProt annotation describes a transcriptional activator that binds conserved operator sequences in a promoter region. The annotation cites experimental evidence for its regulatory role and similarity-based evidence for the specific binding statement; the GO annotation for transcription cis-regulatory region binding is computationally inferred. These support option C, while distinguishing the evidence types.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact, soluble, strongly helix-rich protein with a basic N-terminal region, a pattern consistent with a bacterial transcriptional regulator bearing a DNA-binding helix-turn-helix domain. Such regulators bind transcriptional control regions, favoring C. The sequence lacks the long hydrophobic segments expected of a membrane transporter (A) and does not suggest a glucosyltransferase enzyme (D). B is specifically RNA polymerase II cis-regulatory binding, a eukaryotic transcription context, whereas C is the general regulatory-region binding choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence and protein-family patterns meaningfully distinguish generic transcriptional regulatory-region binding from the membrane-transport, enzyme, and RNA polymerase II-specific alternatives. This is a credible inference, though the sequence alone does not establish the exact biological targets or prove the function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad wording of C fits a DNA-binding transcriptional regulator; B is narrower and specifies RNA polymerase II, unlike the general regulatory-region activity asked for here.


### Important caveats

- The organism and target-specific annotation in reviewer-only evidence were not part of the original input and are not used as premises for the transferability judgment.
- The evidence for promoter/operator binding is partly similarity-based; the GO annotation is computationally inferred.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, soluble, strongly helix-rich protein with a basic N-terminal region, a pattern consistent with a bacterial transcriptional regulator bearing a DNA-binding helix-turn-helix domain. Such regulators bind transcriptional control regions, favoring C. The sequence lacks the long hydrophobic segments expected of a membrane transporter (A) and does not suggest a glucosyltransferase enzyme (D). B is specifically RNA polymerase II cis-regulatory binding, a eukaryotic transcription context, whereas C is the general regulatory-region binding choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-family patterns meaningfully distinguish generic transcriptional regulatory-region binding from the membrane-transport, enzyme, and RNA polymerase II-specific alternatives. This is a credible inference, though the sequence alone does not establish the exact biological targets or prove the function."
  },
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation describes a transcriptional activator that binds conserved operator sequences in a promoter region. The annotation cites experimental evidence for its regulatory role and similarity-based evidence for the specific binding statement; the GO annotation for transcription cis-regulatory region binding is computationally inferred. These support option C, while distinguishing the evidence types."
  },
  "important_caveats": [
    "The organism and target-specific annotation in reviewer-only evidence were not part of the original input and are not used as premises for the transferability judgment.",
    "The evidence for promoter/operator binding is partly similarity-based; the GO annotation is computationally inferred."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad wording of C fits a DNA-binding transcriptional regulator; B is narrower and specifies RNA polymerase II, unlike the general regulatory-region activity asked for here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation describes a transcriptional activator that binds conserved operator sequences in a promoter region. The annotation cites experimental evidence for its regulatory role and similarity-based evidence for the specific binding statement; the GO annotation for transcription cis-regulatory region binding is computationally inferred. These support option C, while distinguishing the evidence types.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact, soluble, strongly helix-rich protein with a basic N-terminal region, a pattern consistent with a bacterial transcriptional regulator bearing a DNA-binding helix-turn-helix domain. Such regulators bind transcriptional control regions, favoring C. The sequence lacks the long hydrophobic segments expected of a membrane transporter (A) and does not suggest a glucosyltransferase enzyme (D). B is specifically RNA polymerase II cis-regulatory binding, a eukaryotic transcription context, whereas C is the general regulatory-region binding choice.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence and protein-family patterns meaningfully distinguish generic transcriptional regulatory-region binding from the membrane-transport, enzyme, and RNA polymerase II-specific alternatives. This is a credible inference, though the sequence alone does not establish the exact biological targets or prove the function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad wording of C fits a DNA-binding transcriptional regulator; B is narrower and specifies RNA polymerase II, unlike the general regulatory-region activity asked for here."
  },
  "important_caveats": [
    "The organism and target-specific annotation in reviewer-only evidence were not part of the original input and are not used as premises for the transferability judgment.",
    "The evidence for promoter/operator binding is partly similarity-based; the GO annotation is computationally inferred."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0QTR3 (FasR, HTH-type transcriptional activator from Mycolicibacterium smegmatis) carries the GO annotation GO:0000976 'transcription cis-regulatory region binding' (evidence IEA:TreeGrafter, C7/H5). The experimental evidence (PubMed:23721164) confirms the protein 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region,' which matches the GO:0000976 definition: 'Binding to a specific sequence of DNA that is part of a regulatory region that controls transcription.' The GO ontology also lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym of GO:0000976, confirming applicability to bacterial transcription factors. The annotation evidence code is IEA (computational), but the underlying experimental data independently support the functional claim.

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [GO1](#evidence-go1), [H5](#evidence-h5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (219 aa) exhibits the classic architecture of a bacterial HTH-type transcriptional regulator: an N-terminal region containing a helix-turn-helix DNA-binding motif (the segment 'RQALRTTTDNRQRLRAAVEAFF' fits the HTH consensus) followed by a C-terminal ligand-sensing domain (the 'IFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWL' region resembles the ligand-binding fold of TetR/MarR-family bacterial regulators). This architecture immediately eliminates A (no transmembrane helices, no Walker A/B ATPase motifs) and D (no UDP-glucosyltransferase motifs or plant-specific features). The critical distinction between B and C relies on transferable knowledge: RNA Polymerase II is exclusively eukaryotic, so GO:0000978 (RNA Pol II cis-regulatory region sequence-specific DNA binding) cannot apply to a bacterial protein. The HTH-type bacterial regulator architecture, the absence of eukaryotic-specific features (no zinc fingers, bZIP, or nuclear localization signals), and the overall sequence composition are consistent with a bacterial transcription factor. GO:0000976 explicitly includes 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym, making it the correct term for a bacterial transcriptional activator binding operator/promoter sequences.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The HTH motif recognition from the sequence, combined with the well-established biological principle that RNA Pol II is eukaryotic-specific (eliminating B) and that bacterial HTH regulators bind cis-regulatory DNA (supporting C), provides a concrete transferable inference path. The absence of transporter and glycosyltransferase structural features eliminates A and D. No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GO ontology structure clearly separates B (RNA Pol II, eukaryotic) from C (general transcription regulatory region binding, includes bacterial). The sequence architecture unambiguously indicates a bacterial HTH transcription factor, not a transporter or glycosyltransferase. Only C is defensible.


### Important caveats

- The GO:0000976 annotation carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental annotation to this specific term. However, experimental evidence confirms the protein binds operator sequences in promoter regions, which is functionally equivalent to the term's definition.
- The model must infer bacterial origin from sequence architecture (HTH + ligand-binding domain, lack of eukaryotic features) rather than from an explicit organism label in the input.
- GO:0003700 (DNA-binding transcription factor activity) is also annotated to this protein and would be a more specific answer, but it is not among the offered choices.
- The historical UniProt entry (version 121, released Jan 2026) already contained the GO:0000976 annotation, so the answer was available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (219 aa) exhibits the classic architecture of a bacterial HTH-type transcriptional regulator: an N-terminal region containing a helix-turn-helix DNA-binding motif (the segment 'RQALRTTTDNRQRLRAAVEAFF' fits the HTH consensus) followed by a C-terminal ligand-sensing domain (the 'IFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWL' region resembles the ligand-binding fold of TetR/MarR-family bacterial regulators). This architecture immediately eliminates A (no transmembrane helices, no Walker A/B ATPase motifs) and D (no UDP-glucosyltransferase motifs or plant-specific features). The critical distinction between B and C relies on transferable knowledge: RNA Polymerase II is exclusively eukaryotic, so GO:0000978 (RNA Pol II cis-regulatory region sequence-specific DNA binding) cannot apply to a bacterial protein. The HTH-type bacterial regulator architecture, the absence of eukaryotic-specific features (no zinc fingers, bZIP, or nuclear localization signals), and the overall sequence composition are consistent with a bacterial transcription factor. GO:0000976 explicitly includes 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym, making it the correct term for a bacterial transcriptional activator binding operator/promoter sequences.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The HTH motif recognition from the sequence, combined with the well-established biological principle that RNA Pol II is eukaryotic-specific (eliminating B) and that bacterial HTH regulators bind cis-regulatory DNA (supporting C), provides a concrete transferable inference path. The absence of transporter and glycosyltransferase structural features eliminates A and D. No target-specific memorization is required."
  },
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "GO1",
      "H5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0QTR3 (FasR, HTH-type transcriptional activator from Mycolicibacterium smegmatis) carries the GO annotation GO:0000976 'transcription cis-regulatory region binding' (evidence IEA:TreeGrafter, C7/H5). The experimental evidence (PubMed:23721164) confirms the protein 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region,' which matches the GO:0000976 definition: 'Binding to a specific sequence of DNA that is part of a regulatory region that controls transcription.' The GO ontology also lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym of GO:0000976, confirming applicability to bacterial transcription factors. The annotation evidence code is IEA (computational), but the underlying experimental data independently support the functional claim."
  },
  "important_caveats": [
    "The GO:0000976 annotation carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental annotation to this specific term. However, experimental evidence confirms the protein binds operator sequences in promoter regions, which is functionally equivalent to the term's definition.",
    "The model must infer bacterial origin from sequence architecture (HTH + ligand-binding domain, lack of eukaryotic features) rather than from an explicit organism label in the input.",
    "GO:0003700 (DNA-binding transcription factor activity) is also annotated to this protein and would be a more specific answer, but it is not among the offered choices.",
    "The historical UniProt entry (version 121, released Jan 2026) already contained the GO:0000976 annotation, so the answer was available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO ontology structure clearly separates B (RNA Pol II, eukaryotic) from C (general transcription regulatory region binding, includes bacterial). The sequence architecture unambiguously indicates a bacterial HTH transcription factor, not a transporter or glycosyltransferase. Only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0QTR3 (FasR, HTH-type transcriptional activator from Mycolicibacterium smegmatis) carries the GO annotation GO:0000976 'transcription cis-regulatory region binding' (evidence IEA:TreeGrafter, C7/H5). The experimental evidence (PubMed:23721164) confirms the protein 'specifically binds to three conserved operator sequences present in the fas-acpS promoter region,' which matches the GO:0000976 definition: 'Binding to a specific sequence of DNA that is part of a regulatory region that controls transcription.' The GO ontology also lists 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym of GO:0000976, confirming applicability to bacterial transcription factors. The annotation evidence code is IEA (computational), but the underlying experimental data independently support the functional claim.",
    "evidence_ids": ["C7", "C5", "GO1", "H5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (219 aa) exhibits the classic architecture of a bacterial HTH-type transcriptional regulator: an N-terminal region containing a helix-turn-helix DNA-binding motif (the segment 'RQALRTTTDNRQRLRAAVEAFF' fits the HTH consensus) followed by a C-terminal ligand-sensing domain (the 'IFENDYVTEPQVAAQVKVATEACTDAVFDLISRDSGLEAHRARMIAVGLVAISVDSARYWL' region resembles the ligand-binding fold of TetR/MarR-family bacterial regulators). This architecture immediately eliminates A (no transmembrane helices, no Walker A/B ATPase motifs) and D (no UDP-glucosyltransferase motifs or plant-specific features). The critical distinction between B and C relies on transferable knowledge: RNA Polymerase II is exclusively eukaryotic, so GO:0000978 (RNA Pol II cis-regulatory region sequence-specific DNA binding) cannot apply to a bacterial protein. The HTH-type bacterial regulator architecture, the absence of eukaryotic-specific features (no zinc fingers, bZIP, or nuclear localization signals), and the overall sequence composition are consistent with a bacterial transcription factor. GO:0000976 explicitly includes 'bacterial-type RNA polymerase regulatory region DNA binding' as a narrow synonym, making it the correct term for a bacterial transcriptional activator binding operator/promoter sequences.",
    "missing_item_specific_fact": "",
    "reason": "The HTH motif recognition from the sequence, combined with the well-established biological principle that RNA Pol II is eukaryotic-specific (eliminating B) and that bacterial HTH regulators bind cis-regulatory DNA (supporting C), provides a concrete transferable inference path. The absence of transporter and glycosyltransferase structural features eliminates A and D. No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GO ontology structure clearly separates B (RNA Pol II, eukaryotic) from C (general transcription regulatory region binding, includes bacterial). The sequence architecture unambiguously indicates a bacterial HTH transcription factor, not a transporter or glycosyltransferase. Only C is defensible."
  },
  "important_caveats": [
    "The GO:0000976 annotation carries IEA (Inferred from Electronic Annotation) evidence, not direct experimental annotation to this specific term. However, experimental evidence confirms the protein binds operator sequences in promoter regions, which is functionally equivalent to the term's definition.",
    "The model must infer bacterial origin from sequence architecture (HTH + ligand-binding domain, lack of eukaryotic features) rather than from an explicit organism label in the input.",
    "GO:0003700 (DNA-binding transcription factor activity) is also annotated to this protein and would be a more specific answer, but it is not among the offered choices.",
    "The historical UniProt entry (version 121, released Jan 2026) already contained the GO:0000976 annotation, so the answer was available at benchmark construction time."
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
  "benchmark_sequence_length": 219,
  "benchmark_sequence_sha256": "7655cf7e660aa0356101859ec630e218188ac533362de09980c127dec1f2e84a",
  "current_entry_audit": {
    "entryVersion": 123,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 219,
  "current_source_sequence_sha256": "7655cf7e660aa0356101859ec630e218188ac533362de09980c127dec1f2e84a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 121,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0QTR3",
  "selected_historical_entry_version": 121,
  "selected_historical_record_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "selected_historical_source_sequence_length": 219,
  "selected_historical_source_sequence_sha256": "7655cf7e660aa0356101859ec630e218188ac533362de09980c127dec1f2e84a",
  "selected_historical_version": {
    "accession": "A0QTR3",
    "database": "Swiss-Prot",
    "entryVersion": 121,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FASR_MYCS2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0QTR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":123,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mycobacterium smegmatis\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycolicibacterium\"],\"scientificName\":\"Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155)\",\"taxonId\":246196}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23721164\",\"source\":\"PubMed\"}],\"value\":\"Fatty acid synthesis regulator\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HTH-type transcriptional activator FasR\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O05858\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23721164\",\"source\":\"PubMed\"}],\"value\":\"Transcriptional activator that plays a central role in sensing mycobacterial long-chain fatty acids and regulating lipid biosynthesis (PubMed:23721164). Activates the expression of the genes encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products are involved in the fatty acid and mycolic acid biosynthesis (PubMed:23721164). Specifically binds to three conserved operator sequences present in the fas-acpS promoter region (By similarity). Essential for M.smegmatis viability (PubMed:23721164)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003700\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:DNA-binding transcription factor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000976\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:transcription cis-regulatory region binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/16",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0QTR3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Mondino S.\",\"Gago G.\",\"Gramajo H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23721164\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12282\"}],\"citationType\":\"journal article\",\"firstPage\":\"372\",\"id\":\"23721164\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"387\",\"publicationDate\":\"2013\",\"title\":\"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\",\"volume\":\"89\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"H37Rv\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DNA-BINDING\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:56.364123+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8cf2c8b486d8c72d205fd0d9007bd62d07c0a8e903a99695cdc94552a5fc09a5",
  "url": "https://rest.uniprot.org/uniprotkb/A0QTR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H1",
  "excerpt": "ID   FASR_MYCS2              Reviewed;         219 AA.\nAC   A0QTR3; I7FA01;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 1.\nDT   28-JAN-2026, entry version 121.\nDE   RecName: Full=HTH-type transcriptional activator FasR {ECO:0000305};\nDE   AltName: Full=Fatty acid synthesis regulator {ECO:0000303|PubMed:23721164};\nGN   Name=fasR {ECO:0000303|PubMed:23721164};\nGN   OrderedLocusNames=MSMEG_1935 {ECO:0000312|EMBL:ABK72683.1},\nGN   MSMEI_1893 {ECO:0000312|EMBL:AFP38365.1};\nOS   Mycolicibacterium smegmatis (strain ATCC 700084 / mc(2)155) (Mycobacterium\nOS   smegmatis).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycolicibacterium.\nOX   NCBI_TaxID=246196;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:44.625980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "url": "https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, DNA-BINDING, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=H37Rv;\nRX   PubMed=23721164; DOI=10.1111/mmi.12282;\nRA   Mondino S., Gago G., Gramajo H.;\nRT   \"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\";\nRL   Mol. Microbiol. 89:372-387(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:44.625980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "url": "https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Transcriptional activator that plays a central role in\nCC       sensing mycobacterial long-chain fatty acids and regulating lipid\nCC       biosynthesis (PubMed:23721164). Activates the expression of the genes\nCC       encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl\nCC       transferase (acpS), whose products are involved in the fatty acid and\nCC       mycolic acid biosynthesis (PubMed:23721164). Specifically binds to\nCC       three conserved operator sequences present in the fas-acpS promoter\nCC       region (By similarity). Essential for M.smegmatis viability\nCC       (PubMed:23721164). {ECO:0000250|UniProtKB:O05858,\nCC       ECO:0000269|PubMed:23721164}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:44.625980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "url": "https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:44.625980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "url": "https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121)

```json
{
  "entry_version": 121,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0000976; F:transcription cis-regulatory region binding; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:44.625980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bcd24040722af499e5b64bc73a390a5b6fc97de2775d647dcbfa09a8e9dc372e",
  "url": "https://rest.uniprot.org/unisave/A0QTR3?format=txt&versions=121"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000976\nname: transcription cis-regulatory region binding\nnamespace: molecular_function\nalt_id: GO:0000975\nalt_id: GO:0000984\nalt_id: GO:0001017\nalt_id: GO:0044212\ndef: \"Binding to a specific sequence of DNA that is part of a regulatory region that controls transcription of that section of the DNA. The transcribed region might be described as a gene, cistron, or operon.\" [GOC:txnOH]\ncomment: Note that this term is meant to also capture non-specific binding to regulatory regions. Also, to minimize ambiguity in the use of the word \"promoter\" in GO, we have chosen the phrase \"transcription regulatory region\" to refer to all of the regulatory regions. Regulatory regions in the DNA which control initiation may include the \"core promoter\" where the basal transcription machinery binds, the \"core promoter proximal region\" where regulatory factors other than the basal machinery bind. There are also additional regulatory regions, in both the DNA and the RNA transcript, which regulate elongation or termination of transcription.\nsynonym: \"bacterial-type RNA polymerase regulatory region DNA binding\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcription regulatory region sequence-specific DNA binding\" NARROW []\nsynonym: \"eubacterial-type RNA polymerase regulatory region DNA binding\" NARROW []\nsynonym: \"eubacterial-type RNA polymerase regulatory region sequence-specific DNA binding\" NARROW []\nsynonym: \"regulatory region DNA binding\" BROAD []\nsynonym: \"transcription regulatory region DNA binding\" RELATED []\nsynonym: \"transcription regulatory region sequence-specific DNA binding\" EXACT []\nis_a: GO:0001067 ! transcription regulatory region nucleic acid binding\nis_a: GO:1990837 ! sequence-specific double-stranded DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000976",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 7096-7115",
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
  "excerpt": "[Term]\nid: GO:0000978\nname: RNA polymerase II cis-regulatory region sequence-specific DNA binding\nnamespace: molecular_function\nalt_id: GO:0000980\ndef: \"Binding to a specific upstream regulatory DNA sequence (transcription factor recognition sequence or binding site) located in cis relative to the transcription start site (i.e., on the same strand of DNA) of a gene transcribed by RNA polymerase II.\" [GOC:txnOH-2018]\ncomment: Note that the phrase \"upstream activating sequence\", or UAS is often used in S. cerevisiae literature to refer to cis-regulatory sequences. In bacteria such as E. coli, the phrase \"upstream activating sequence\", or UAS is usually a synonym for \"enhancer\".\nsynonym: \"RNA polymerase II core promoter proximal region sequence-specific DNA binding\" RELATED []\nsynonym: \"RNA polymerase II distal enhancer sequence-specific DNA binding\" RELATED []\nsynonym: \"RNA polymerase II promoter proximal region sequence-specific DNA binding\" RELATED []\nsynonym: \"RNA polymerase II proximal promoter sequence-specific DNA binding\" RELATED []\nsynonym: \"RNA polymerase II upstream activating sequence (UAS) sequence-specific DNA binding\" RELATED []\nxref: Reactome:R-HSA-400204 \"PPARA binds RXRA\"\nis_a: GO:0000977 ! RNA polymerase II transcription regulatory region sequence-specific DNA binding\nis_a: GO:0000987 ! cis-regulatory region sequence-specific DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000978",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 7126-7141",
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
  "excerpt": "[Term]\nid: GO:0042626\nname: ATPase-coupled transmembrane transporter activity\nnamespace: molecular_function\nalt_id: GO:0015405\nalt_id: GO:0016820\nalt_id: GO:0043492\ndef: \"Primary active transporter of a solute across a membrane, via the reaction: ATP + H2O = ADP + phosphate, to directly drive the transport of a substance across a membrane. The transport protein may be transiently phosphorylated (P-type transporters), or not (ABC-type transporters and other families of transporters). Primary active transport occurs up the solute's concentration gradient and is driven by a primary energy source.\" [GOC:mtg_transport, ISBN:0815340729]\nsynonym: \"ATP-coupled transmembrane transporter activity\" EXACT []\nsynonym: \"ATP-dependent transmembrane transporter activity\" EXACT []\nsynonym: \"ATPase activity, coupled to movement of substances\" BROAD []\nsynonym: \"ATPase activity, coupled to transmembrane movement of substances\" EXACT []\nsynonym: \"hydrolase activity, acting on acid anhydrides, catalyzing transmembrane movement of substances\" NARROW []\nsynonym: \"P-P-bond-hydrolysis-driven transmembrane transporter activity\" BROAD []\nsynonym: \"P-P-bond-hydrolysis-driven transporter\" BROAD []\nxref: EC:7.2.2.-\nxref: Reactome:R-HSA-1454916 \"The ABCC family mediates organic anion transport\"\nxref: Reactome:R-HSA-1467457 \"ABCA8,B1,B5 transport xenobiotics from cytosol to extracellular region\"\nxref: Reactome:R-HSA-2161506 \"abacavir [cytosol] + ATP + H2O => abacavir[extracellular] + ADP + phosphate\"\nxref: Reactome:R-HSA-2161538 \"abacavir [cytosol] + ATP + H2O => abacavir[extracellular] + ADP + phosphate\"\nxref: Reactome:R-HSA-390393 \"Peroxisomal uptake of very long-chain fatty acyl CoA\"\nxref: Reactome:R-HSA-5690340 \"Defective ABCC6 does not transport organic anion from cytosol to extracellular region\"\nxref: Reactome:R-HSA-9033499 \"PEX1:PEX6:PEX26:ZFAND6 dissociates Ub:PEX5L and PEX7 from PEX14:PEX13:PEX2:PEX10:PEX12 and translocates PEX5L and PEX7 from the peroxisomal membrane to the cytosol\"\nxref: Reactome:R-HSA-9033505 \"PEX1:PEX6:PEX26:ZFAND6:Ub:PEX5S,L:PEX14:PEX13:PEX2:PEX10:PEX12 dissociates yielding cytosolic Ub:PEX5S,L and membrane PEX14:PEX13:PEX2:PEX10:PEX12\"\nxref: Reactome:R-HSA-9659680 \"ABCB1 transports xenobiotics out of the cell\"\nxref: Reactome:R-HSA-9750546 \"ABCC4 transports TPMP substrates from cytosol to extracellular region\"\nxref: Reactome:R-HSA-9750617 \"ABCC5 transports TPMP substrates from cytosol to extracellular region\"\nxref: Reactome:R-HSA-9753278 \"ABCC2,ABCG2 transport APAP-GlcA, APAP-SO3\"\nxref: Reactome:R-HSA-9753283 \"ABCC3,ABCC4 transport APAP-GlcA, APAP-SO3\"\nxref: Reactome:R-HSA-9753284 \"ABCC1,4,5 transport APAP-Cys,APAP-Mer from cytosol to extracellular region\"\nxref: Reactome:R-HSA-9759454 \"ABCB1 transports PREDN,PREDL out of kidney cells\"\nxref: Reactome:R-HSA-9759461 \"ABCB1 transports PREDN,PREDL out of hepatic cells\"\nxref: Reactome:R-HSA-9794120 \"ABCG2 transports Cipro from intestinal cell to extracellular space\"\nxref: Reactome:R-HSA-9794572 \"ABCG2 transports Cipro from hepatic cell to extracellular space\"\nis_a: GO:0015399 ! primary active transmembrane transporter activity\nis_a: GO:0140657 ! ATP-dependent activity\nproperty_value: skos:exactMatch EC:7.2.2.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042626",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 239260-239297",
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
  "excerpt": "[Term]\nid: GO:0080044\nname: quercetin 7-O-glucosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a glucosyl group from UDP-glucose to the 7-hydroxy group of a quercetin molecule.\" [PMID:15352060]\nis_a: GO:0035251 ! UDP-glucosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0080044",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 392459-392465",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
