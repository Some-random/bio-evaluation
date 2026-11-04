# cofactor_0135

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0135.txt)

**Task:** `cofactor`  
**Expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASSDLEAATALKVQGNKAFGQHEWPTAVDFYTQAIAKYDREPSFFSNRAQAHIKLEAYGFAIADATKALELDPAYTKAYWRRALANTAILNYKDALRDFKVVAKREPNNRDAKVKLADCEKLVRRMEFEKAIEVGDPPSAFEDLDIDAIAVDDSYDGVRLEKEMTQEFIDDMIERFKNGKKIHRKYAFQIVKAVKDIVYAEPTMVEIGVDQGTKLTVCGDTHGQFFDLLEIFRLNGYPSEKHAYLFNGDFVDRGSWSTEIALLLYAYKWLRPNGIFLNRGNHETDDMNKVYGFEGECKAKYNERMFKVFSESFSALPLATLIGNKYLVLHGGLFSDDNTSLDDIRKLDRHNQRQPGQQGLMMEMLWTDPQTEPGRGPSKRGVGLQFGPDVTKRFCEKNGLEAIIRSHEVRMEGYEVEHDGRCITVFSAPKYCDTTENKGAFINVGPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM

[Multiple Choices]
A. heme
B. Zn(2+)
C. Mn(2+)
D. Mg(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry lists Mg(2+) as a cofactor, supporting the keyed answer. The same annotation also lists Mn(2+), so Mg(2+) is not uniquely supported.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

> The sequence is consistent with a metal-dependent serine/threonine phosphatase. Transferable knowledge of this phosphatase family supports Mg(2+) or Mn(2+) over heme or Zn(2+), but does not meaningfully prefer Mg(2+) to Mn(2+).


**Missing item-specific fact**

> A target-specific activity measurement or other evidence establishing whether Mg(2+) or Mn(2+) is intended as the required cofactor.


**Reason**

> Family-level knowledge narrows the plausible choices to C and D but does not select the author's keyed choice. The supplied evidence likewise reports binding either ion, leaving the singular-choice distinction unresolved.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The sequence-matched annotation states that the protein binds two Mg(2+) or Mn(2+) cations per subunit, making both options defensible.


### Important caveats

- The cofactor annotation is transferred by similarity from another UniProt entry, rather than presented as direct experimental evidence for this exact protein.
- The evidence supports Mg(2+) as a cofactor but does not establish that it is exclusive or preferred over Mn(2+).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a metal-dependent serine/threonine phosphatase. Transferable knowledge of this phosphatase family supports Mg(2+) or Mn(2+) over heme or Zn(2+), but does not meaningfully prefer Mg(2+) to Mn(2+).",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "A target-specific activity measurement or other evidence establishing whether Mg(2+) or Mn(2+) is intended as the required cofactor.",
    "reason": "Family-level knowledge narrows the plausible choices to C and D but does not select the author's keyed choice. The supplied evidence likewise reports binding either ion, leaving the singular-choice distinction unresolved."
  },
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry lists Mg(2+) as a cofactor, supporting the keyed answer. The same annotation also lists Mn(2+), so Mg(2+) is not uniquely supported."
  },
  "important_caveats": [
    "The cofactor annotation is transferred by similarity from another UniProt entry, rather than presented as direct experimental evidence for this exact protein.",
    "The evidence supports Mg(2+) as a cofactor but does not establish that it is exclusive or preferred over Mn(2+)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The sequence-matched annotation states that the protein binds two Mg(2+) or Mn(2+) cations per subunit, making both options defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0135",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry lists Mg(2+) as a cofactor, supporting the keyed answer. The same annotation also lists Mn(2+), so Mg(2+) is not uniquely supported.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "The sequence is consistent with a metal-dependent serine/threonine phosphatase. Transferable knowledge of this phosphatase family supports Mg(2+) or Mn(2+) over heme or Zn(2+), but does not meaningfully prefer Mg(2+) to Mn(2+).",
    "missing_item_specific_fact": "A target-specific activity measurement or other evidence establishing whether Mg(2+) or Mn(2+) is intended as the required cofactor.",
    "reason": "Family-level knowledge narrows the plausible choices to C and D but does not select the author's keyed choice. The supplied evidence likewise reports binding either ion, leaving the singular-choice distinction unresolved."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The sequence-matched annotation states that the protein binds two Mg(2+) or Mn(2+) cations per subunit, making both options defensible."
  },
  "important_caveats": [
    "The cofactor annotation is transferred by similarity from another UniProt entry, rather than presented as direct experimental evidence for this exact protein.",
    "The evidence supports Mg(2+) as a cofactor but does not establish that it is exclusive or preferred over Mn(2+)."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Saved visible final text:** empty string (`""`).

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 478,
  "benchmark_sequence_sha256": "c5cf3682979f916b743dae9d58b015b87b664ef42086c83e4f9416f69c814f7f",
  "current_entry_audit": {
    "entryVersion": 129,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 478,
  "current_source_sequence_sha256": "c5cf3682979f916b743dae9d58b015b87b664ef42086c83e4f9416f69c814f7f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 127,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2U919",
  "selected_historical_entry_version": 127,
  "selected_historical_record_sha256": "2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20",
  "selected_historical_source_sequence_length": 478,
  "selected_historical_source_sequence_sha256": "c5cf3682979f916b743dae9d58b015b87b664ef42086c83e4f9416f69c814f7f",
  "selected_historical_version": {
    "accession": "Q2U919",
    "database": "Swiss-Prot",
    "entryVersion": 127,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PPP5_ASPOR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2U919\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":129,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yellow koji mold\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000006564\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus oryzae (strain ATCC 42149 / RIB 40)\",\"taxonId\":510516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17475320\",\"source\":\"PubMed\"}],\"value\":\"AoPPT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17475320\",\"source\":\"PubMed\"}],\"value\":\"3.1.3.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53043\",\"source\":\"UniProtKB\"}],\"value\":\"Serine/threonine-protein phosphatase T\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53043\",\"source\":\"UniProtKB\"}],\"value\":\"PPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P53041\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 Mg(2+) or Mn(2+) cations per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Feng B.\",\"Zhao C.H.\",\"Tanaka S.\",\"Imanaka H.\",\"Imamura K.\",\"Nakanishi K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17475320\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ijbiomac.2007.03.005\"}],\"citationType\":\"journal article\",\"firstPage\":\"281\",\"id\":\"17475320\",\"journal\":\"Int. J. Biol. Macromol.\",\"lastPage\":\"285\",\"publicationDate\":\"2007\",\"title\":\"TPR domain of Ser/Thr phosphatase of Aspergillus oryzae shows no auto-inhibitory effect on the dephosphorylation activity.\",\"volume\":\"41\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17475320\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"AGL142-72\"}],\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:21.139726+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23",
  "url": "https://rest.uniprot.org/uniprotkb/Q2U919.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H1",
  "excerpt": "ID   PPP5_ASPOR              Reviewed;         478 AA.\nAC   Q2U919;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 127.\nDE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000250|UniProtKB:P53043};\nDE            Short=PPT {ECO:0000250|UniProtKB:P53043};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:17475320};\nDE   AltName: Full=AoPPT {ECO:0000303|PubMed:17475320};\nGN   Name=ppt1 {ECO:0000305};\nGN   ORFNames=AO090701000208 {ECO:0000312|EMBL:BAE61946.1};\nOS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=510516 {ECO:0000312|Proteomes:UP000006564};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:33.211950+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20",
  "url": "https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000250|UniProtKB:P53043};\nDE            Short=PPT {ECO:0000250|UniProtKB:P53043};\nDE            EC=3.1.3.16 {ECO:0000305|PubMed:17475320};\nDE   AltName: Full=AoPPT {ECO:0000303|PubMed:17475320};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:33.211950+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20",
  "url": "https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=AGL142-72 {ECO:0000303|PubMed:17475320};\nRX   PubMed=17475320; DOI=10.1016/j.ijbiomac.2007.03.005;\nRA   Feng B., Zhao C.H., Tanaka S., Imanaka H., Imamura K., Nakanishi K.;\nRT   \"TPR domain of Ser/Thr phosphatase of Aspergillus oryzae shows no auto-\nRT   inhibitory effect on the dephosphorylation activity.\";\nRL   Int. J. Biol. Macromol. 41:281-285(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:33.211950+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20",
  "url": "https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)

```json
{
  "entry_version": 127,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:P53041};\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000250|UniProtKB:P53041};\nCC       Note=Binds 2 Mg(2+) or Mn(2+) cations per subunit.\nCC       {ECO:0000250|UniProtKB:P53041};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:33.211950+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20",
  "url": "https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 135. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
