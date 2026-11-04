# active_site_0020

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0020.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 120 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM

[Multiple Choices]
A. Position 250 (Proton acceptor)
B. Position 95 (Nucleophile)
C. Position 1045 (Proton acceptor; for dehydratase activity)
D. Position 120 (Nucleophile)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif.


### Important caveats

- The reviewer-only record supports the answer but was not part of the original model input.
- The database annotation cites literature, but the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role."
  },
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment."
  },
  "important_caveats": [
    "The reviewer-only record supports the answer but was not part of the original model input.",
    "The database annotation cites literature, but the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "For the sequence-matched protein, the UniProt active-site annotation identifies position 120 as the nucleophile and cites PubMed 33846308; the historical record gives the same annotation. This supports choice D, though the source annotation is not an independent review of the underlying experiment.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 120 is a glutamate in the sequence's acidic E...E motif around residues 120–124. In retaining glycosidases, a catalytic carboxylate can act as the nucleophile, with a nearby carboxylate serving as the acid/base partner. That makes the glutamate at 120 a credible nucleophile candidate; the other listed positions are inconsistent with this motif, and position 1045 exceeds the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable glycosidase catalytic principles provide a meaningful basis for selecting position 120 as the nucleophile, without needing the exact protein's recorded annotation. This is a family-level, probabilistic inference rather than proof of the residue's experimentally assigned role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported: the position-1045 choice is outside the 391-residue sequence, and the other proposed positions do not fit the catalytic acidic-residue motif."
  },
  "important_caveats": [
    "The reviewer-only record supports the answer but was not part of the original model input.",
    "The database annotation cites literature, but the primary study was not independently reviewed here."
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
  "benchmark_sequence_length": 391,
  "benchmark_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 391,
  "current_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384J6C4",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "selected_historical_source_sequence_length": 391,
  "selected_historical_source_sequence_sha256": "45397ff42b669bfa8d792796bca49c6799638f51b62028337c71133258f86793",
  "selected_historical_version": {
    "accession": "A0A384J6C4",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRH1_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384J6C4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"3.2.1.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitinase crh1\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"value\":\"Chitin transglycosylase crh1\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"value\":\"Crh-like protein 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":120},\"start\":{\"modifier\":\"EXACT\",\"value\":120}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33846308\",\"source\":\"PubMed\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":124},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":124},\"start\":{\"modifier\":\"EXACT\",\"value\":124}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":210},\"start\":{\"modifier\":\"EXACT\",\"value\":210}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8J0P4\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:17029\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:17029\",\"name\":\"chitin\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":227},\"start\":{\"modifier\":\"EXACT\",\"value\":227}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384J6C4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Bi K.\",\"Scalschi L.\",\"Jaiswal N.\",\"Mengiste T.\",\"Fried R.\",\"Sanz A.B.\",\"Arroyo J.\",\"Zhu W.\",\"Masrati G.\",\"Sharon A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33846308\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-021-22436-1\"}],\"citationType\":\"journal article\",\"firstPage\":\"2166\",\"id\":\"33846308\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2166\",\"publicationDate\":\"2021\",\"title\":\"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector triggering plant cell death and defense response.\",\"volume\":\"12\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"DOMAIN\",\"MUTAGENESIS OF CYS-33; GLU-120; ASP-122 AND GLU-124\",\"SUBUNIT\",\"INTERACTION WITH CRH2 AND CRH3\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:56.188291+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1aecb325f5593cc4373d6635585c88802bf5afedf29330745842f8b0c516c1c1",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384J6C4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   CRH1_BOTFB              Reviewed;         391 AA.\nAC   A0A384J6C4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Crh-like protein 1 {ECO:0000303|PubMed:33846308};\nDE   Includes:\nDE     RecName: Full=Chitinase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=3.2.1.14 {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Includes:\nDE     RecName: Full=Chitin transglycosylase crh1 {ECO:0000250|UniProtKB:Q8J0P4};\nDE              EC=2.4.-.- {ECO:0000250|UniProtKB:Q8J0P4};\nDE   Flags: Precursor;\nGN   Name=crh1 {ECO:0000303|PubMed:33846308}; ORFNames=BCIN_01g06010;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, DOMAIN, MUTAGENESIS\nRP   OF CYS-33; GLU-120; ASP-122 AND GLU-124, SUBUNIT, AND INTERACTION WITH CRH2\nRP   AND CRH3.\nRX   PubMed=33846308; DOI=10.1038/s41467-021-22436-1;\nRA   Bi K., Scalschi L., Jaiswal N., Mengiste T., Fried R., Sanz A.B.,\nRA   Arroyo J., Zhu W., Masrati G., Sharon A.;\nRT   \"The Botrytis cinerea Crh1 transglycosylase is a cytoplasmic effector\nRT   triggering plant cell death and defense response.\";\nRL   Nat. Commun. 12:2166-2166(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        120\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        124\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000305|PubMed:33846308\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         124\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-178",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         206\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 179-182",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         210\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 183-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         227\nFT                   /ligand=\"chitin\"\nFT                   /ligand_id=\"ChEBI:CHEBI:17029\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q8J0P4\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:58.365606+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-190",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "47e6aea78882143ac7edfaa1c3552ca5206fb63c59d64c8096716a243b69e750",
  "url": "https://rest.uniprot.org/unisave/A0A384J6C4?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
