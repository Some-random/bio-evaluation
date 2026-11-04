# EC_number_0182

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0182.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 3.4.21.62

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. 3.4.13.22
B. 1.1.1.195
C. 3.4.21.62
D. 1.97.1.13
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives.


### Important caveats

- Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating."
  },
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence."
  },
  "important_caveats": [
    "Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed UniProt sequence. Its annotation assigns EC 3.4.21.62, and the catalytic-activity annotation is supported by evidence coded ECO:0000269, indicating experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the architecture of a secreted precursor with a long prodomain followed by a subtilisin-like catalytic region. Recognition of the subtilase family and its serine-protease function supports a peptide-bond hydrolase, distinguishing choice C from the dehydrogenase and oxidoreductase choices and the peptidase with a different EC class.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of subtilase-family sequences and functions gives a meaningful basis for choosing C among these alternatives. The exact EC subtype may require finer family knowledge, but the offered choices make the family-level inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice C is consistent with the sequence's apparent subtilase precursor and serine-protease function among the offered alternatives."
  },
  "important_caveats": [
    "Sequence-based family recognition supports the choice but is not, by itself, direct experimental confirmation of the exact EC subtype."
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
  "benchmark_sequence_length": 630,
  "benchmark_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "current_entry_audit": {
    "entryVersion": 80,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-03-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 630,
  "current_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 78,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E6Y8B9",
  "selected_historical_entry_version": 78,
  "selected_historical_record_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "selected_historical_source_sequence_length": 630,
  "selected_historical_source_sequence_sha256": "26d75cef4b12afe63e95e1e558255f990bc3a1fb29980dad1ff271270e9bc1c3",
  "selected_historical_version": {
    "accession": "E6Y8B9",
    "database": "Swiss-Prot",
    "entryVersion": 78,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SUB1_PLAVI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E6Y8B9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":80,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-03-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACT76164.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Plasmodium\"],\"scientificName\":\"Plasmodium vivax\",\"taxonId\":5855}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"PvS1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"PvSUB1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"SUB1 protease\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25204226\",\"source\":\"PubMed\"}],\"value\":\"Subtilase SUB1\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"3.4.21.62\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"value\":\"Subtilisin-like protease 1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.4.21.62\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23653352\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"25204226\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37428845\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38386597\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503166\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of proteins with broad specificity for peptide bonds, and a preference for a large uncharged residue in P1. Hydrolyzes peptide amides.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Bouillon A.\",\"Giganti D.\",\"Benedet C.\",\"Gorgette O.\",\"Petres S.\",\"Crublet E.\",\"Girard-Blanc C.\",\"Witkowski B.\",\"Menard D.\",\"Nilges M.\",\"Mercereau-Puijalon O.\",\"Stoven V.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23653352\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m113.456764\"}],\"citationType\":\"journal article\",\"firstPage\":\"18561\",\"id\":\"23653352\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"18573\",\"publicationDate\":\"2013\",\"title\":\"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.\",\"volume\":\"288\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Bouillon A.\",\"Brule S.\",\"Raynal B.\",\"Haouz A.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38386597\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.00198-24\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0019824\",\"id\":\"38386597\",\"journal\":\"MBio\",\"lastPage\":\"e0019824\",\"publicationDate\":\"2024\",\"title\":\"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition mechanism that controls Plasmodium Sub1 activity before merozoite egress.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Giganti D.\",\"Bouillon A.\",\"Tawk L.\",\"Robert F.\",\"Martinez M.\",\"Crublet E.\",\"Weber P.\",\"Girard-Blanc C.\",\"Petres S.\",\"Haouz A.\",\"Hernandez J.F.\",\"Mercereau-Puijalon O.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25204226\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms5833\"}],\"citationType\":\"journal article\",\"firstPage\":\"4833\",\"id\":\"25204226\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"4833\",\"publicationDate\":\"2014\",\"title\":\"A novel Plasmodium-specific prodomain fold regulates the malaria drug target SUB1 subtilase.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"4TR2\",\"source\":\"PDB\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"SUBUNIT\",\"PROTEOLYTIC CLEAVAGE\",\"CLEAVAGE SITE\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Martinez M.\",\"Batista F.A.\",\"Maurel M.\",\"Bouillon A.\",\"Ortega Varga L.\",\"Wehenkel A.M.\",\"Le Chevalier-Sontag L.\",\"Blondel A.\",\"Haouz A.\",\"Hernandez J.F.\",\"Alzari P.M.\",\"Barale J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37428845\"},{\"database\":\"DOI\",\"id\":\"10.1107/s2059798323004710\"}],\"citationType\":\"journal article\",\"firstPage\":\"721\",\"id\":\"37428845\",\"journal\":\"Acta Crystallogr. D Struct. Biol.\",\"lastPage\":\"734\",\"publicationDate\":\"2023\",\"title\":\"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1 reveal conformational changes to accommodate a substrate-derived alpha-ketoamide inhibitor.\",\"volume\":\"79\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8COZ\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITOR\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PROTEOLYTIC CLEAVAGE\",\"GLYCOSYLATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\",\"MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Legru A.\",\"Batista F.A.\",\"Puszko A.K.\",\"Bouillon A.\",\"Maurel M.\",\"Martinez M.\",\"Ejjoummany A.\",\"Ortega Varga L.\",\"Adler P.\",\"Mechaly A.\",\"Hadjadj M.\",\"Sosnowski P.\",\"Hopfgartner G.\",\"Alzari P.M.\",\"Blondel A.\",\"Haouz A.\",\"Barale J.C.\",\"Hernandez J.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38503166\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ejmech.2024.116308\"}],\"citationType\":\"journal article\",\"firstPage\":\"116308\",\"id\":\"38503166\",\"journal\":\"Eur. J. Med. Chem.\",\"lastPage\":\"116308\",\"publicationDate\":\"2024\",\"title\":\"Insights from structure-activity relationships and the binding mode of peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-like SUB1.\",\"volume\":\"269\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKE\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8QKG\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITORS\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"GLYCOSYLATION AT ASN-546\",\"DISULFIDE BONDS\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:28:01.366318+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b",
  "url": "https://rest.uniprot.org/uniprotkb/E6Y8B9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H1",
  "excerpt": "ID   SUB1_PLAVI              Reviewed;         630 AA.\nAC   E6Y8B9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-MAR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 78.\nDE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};\nDE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};\nDE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};\nDE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};\nDE   Flags: Precursor;\nGN   Name=sub1 {ECO:0000312|EMBL:ACT76164.1};\nGN   ORFNames=PVC01_100035100 {ECO:0000312|EMBL:SCO73277.1},\nGN   PVT01_100029100 {ECO:0000312|EMBL:SCO67822.1},\nGN   PVW1_100050600 {ECO:0000312|EMBL:CAG9475055.1};\nOS   Plasmodium vivax.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Plasmodium).\nOX   NCBI_TaxID=5855 {ECO:0000312|EMBL:ACT76164.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Subtilisin-like protease 1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE            EC=3.4.21.62 {ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226, ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597, ECO:0000269|PubMed:38503166};\nDE   AltName: Full=PvS1 {ECO:0000303|PubMed:37428845, ECO:0000303|PubMed:38386597, ECO:0000303|PubMed:38503166};\nDE   AltName: Full=PvSUB1 {ECO:0000303|PubMed:23653352, ECO:0000303|PubMed:25204226};\nDE   AltName: Full=SUB1 protease {ECO:0000303|PubMed:38503166};\nDE   AltName: Full=Subtilase SUB1 {ECO:0000303|PubMed:25204226};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, SUBUNIT, DEVELOPMENTAL STAGE, PROTEOLYTIC CLEAVAGE, AND\nRP   CLEAVAGE SITES.\nRX   PubMed=23653352; DOI=10.1074/jbc.m113.456764;\nRA   Bouillon A., Giganti D., Benedet C., Gorgette O., Petres S., Crublet E.,\nRA   Girard-Blanc C., Witkowski B., Menard D., Nilges M., Mercereau-Puijalon O.,\nRA   Stoven V., Barale J.C.;\nRT   \"In Silico screening on the three-dimensional model of the Plasmodium vivax\nRT   SUB1 protease leads to the validation of a novel anti-parasite compound.\";\nRL   J. Biol. Chem. 288:18561-18573(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND SUBUNIT.\nRX   PubMed=38386597; DOI=10.1128/mbio.00198-24;\nRA   Martinez M., Bouillon A., Brule S., Raynal B., Haouz A., Alzari P.M.,\nRA   Barale J.C.;\nRT   \"Prodomain-driven enzyme dimerization: a pH-dependent autoinhibition\nRT   mechanism that controls Plasmodium Sub1 activity before merozoite egress.\";\nRL   MBio 15:e0019824-e0019824(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H5",
  "excerpt": "RN   [5] {ECO:0007744|PDB:4TR2}\nRP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM,\nRP   CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, SUBUNIT, PROTEOLYTIC\nRP   CLEAVAGE, CLEAVAGE SITE, AND DISULFIDE BONDS.\nRX   PubMed=25204226; DOI=10.1038/ncomms5833;\nRA   Giganti D., Bouillon A., Tawk L., Robert F., Martinez M., Crublet E.,\nRA   Weber P., Girard-Blanc C., Petres S., Haouz A., Hernandez J.F.,\nRA   Mercereau-Puijalon O., Alzari P.M., Barale J.C.;\nRT   \"A novel Plasmodium-specific prodomain fold regulates the malaria drug\nRT   target SUB1 subtilase.\";\nRL   Nat. Commun. 5:4833-4833(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H6",
  "excerpt": "RN   [6] {ECO:0007744|PDB:8COY, ECO:0007744|PDB:8COZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+)\nRP   AND PEPTIDE INHIBITOR, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PROTEOLYTIC\nRP   CLEAVAGE, GLYCOSYLATION, GLYCOSYLATION AT ASN-546, DISULFIDE BONDS, AND\nRP   MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445.\nRX   PubMed=37428845; DOI=10.1107/s2059798323004710;\nRA   Martinez M., Batista F.A., Maurel M., Bouillon A., Ortega Varga L.,\nRA   Wehenkel A.M., Le Chevalier-Sontag L., Blondel A., Haouz A.,\nRA   Hernandez J.F., Alzari P.M., Barale J.C.;\nRT   \"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1\nRT   reveal conformational changes to accommodate a substrate-derived alpha-\nRT   ketoamide inhibitor.\";\nRL   Acta Crystallogr. D Struct. Biol. 79:721-734(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H7",
  "excerpt": "RN   [7] {ECO:0007744|PDB:8QKE, ECO:0007744|PDB:8QKG}\nRP   X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND\nRP   PEPTIDE INHIBITORS, CATALYTIC ACTIVITY, ACTIVITY REGULATION, GLYCOSYLATION\nRP   AT ASN-546, AND DISULFIDE BONDS.\nRX   PubMed=38503166; DOI=10.1016/j.ejmech.2024.116308;\nRA   Legru A., Batista F.A., Puszko A.K., Bouillon A., Maurel M., Martinez M.,\nRA   Ejjoummany A., Ortega Varga L., Adler P., Mechaly A., Hadjadj M.,\nRA   Sosnowski P., Hopfgartner G., Alzari P.M., Blondel A., Haouz A.,\nRA   Barale J.C., Hernandez J.F.;\nRT   \"Insights from structure-activity relationships and the binding mode of\nRT   peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-\nRT   like SUB1.\";\nRL   Eur. J. Med. Chem. 269:116308-116308(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-86",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)

```json
{
  "entry_version": 78,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of proteins with broad specificity for peptide\nCC         bonds, and a preference for a large uncharged residue in P1.\nCC         Hydrolyzes peptide amides.; EC=3.4.21.62;\nCC         Evidence={ECO:0000269|PubMed:23653352, ECO:0000269|PubMed:25204226,\nCC         ECO:0000269|PubMed:37428845, ECO:0000269|PubMed:38386597,\nCC         ECO:0000269|PubMed:38503166};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:06.789132+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0",
  "url": "https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
