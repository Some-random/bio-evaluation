# EC_number_0069

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0069.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.7.8.43

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. 2.7.8.41
B. 2.7.8.43
C. 2.5.1.15
D. 4.1.1.129
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1312)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as phosphatidylethanolamine transferase Mcr-2 with EC 2.7.8.43. The record also assigns that EC number to the catalytic reaction. This is curated database evidence linked to a publication, not an independent assessment of the underlying experiments.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an extended hydrophobic, multipass N-terminal region followed by a large catalytic domain, a characteristic architecture of MCR-family lipid A phosphoethanolamine transferases. Transferable knowledge of that family supports a phosphoethanolamine-transferase EC classification, distinguishing B from the unrelated reaction classes represented by C and D and the alternative transferase class in A.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition from the sequence provides a meaningful basis for selecting B among these alternatives; recalling this exact protein's database entry is not necessary. The sequence-based inference is not itself a direct measurement of the catalytic reaction.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives represent sufficiently different enzyme classifications that the MCR-family inference favors B."
  },
  "important_caveats": [
    "The reviewer-only source identifies the sequence as a matched Mcr-2 record; that identity was not part of the original model input.",
    "The cited UniProt catalytic annotation is attributed to a publication, but the supplied excerpts do not independently validate the experimental evidence."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) is annotated with EC 2.7.8.43 based on experimental evidence (ECO:0000305, PubMed:30194678) including X-ray crystallography (PDB:6A7W) and functional mutagenesis studies. The catalytic activity is well-defined: transfer of phosphoethanolamine from phosphatidylethanolamine to lipid A. The sequence matches the benchmark input exactly (538 aa, SHA256 match confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits the hallmark architecture of the MCR (Mobilized Colistin Resistance) protein family: an N-terminal region (~200 residues) with multiple predicted transmembrane helices (highly hydrophobic stretches: MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDT...) followed by a large (~340 residue) soluble C-terminal catalytic domain. This TM + catalytic domain organization, combined with the ~538 aa total length, is diagnostic of MCR-family phosphoethanolamine transferases. The MCR family (MCR-1 through MCR-10+) is extremely well-characterized in the literature as colistin-resistance enzymes, all uniformly classified as EC 2.7.8.43. The catalytic domain contains conserved zinc-binding and phosphotransferase motifs. This eliminates C (2.5.1.15, alkyltransferase) and D (4.1.1.129, carbon-carbon lyase) because neither matches the TM+phosphotransferase architecture. Distinguishing B (2.7.8.43) from A (2.7.8.41) relies on recognizing the MCR family signature: the specific combination of multiple TM segments, the catalytic domain fold with Zn-coordinating residues, and the overall domain topology are shared across all characterized MCR variants and are all annotated as EC 2.7.8.43. EC 2.7.8.41 represents a mechanistically or structurally distinct phosphotransferase that does not share this MCR architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The MCR protein family is one of the most extensively studied protein families in recent microbiology (discovered 2015-2016, hundreds of publications). The sequence features—multiple TM helices, ~538 aa length, large soluble catalytic domain with Zn-binding—are highly distinctive of this family. A model with knowledge of the MCR family from other homologs (MCR-1, MCR-3, MCR-5, etc.) can recognize the architecture and assign EC 2.7.8.43. Options C and D are eliminated by basic enzyme-class reasoning (lyase and alkyltransferase do not match the observed domain architecture). The distinction between A and B rests on family-level recognition of the MCR catalytic domain fold, which is transferable knowledge from the many characterized MCR homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (2.5.1.15) and D (4.1.1.129) are clearly incompatible with the observed TM+phosphotransferase architecture. The MCR family signature is sufficiently distinctive to separate B (2.7.8.43) from A (2.7.8.41), as the MCR family uniformly carries EC 2.7.8.43 and its domain architecture does not match the enzyme class implied by 2.7.8.41.


### Important caveats

- The exact identity of EC 2.7.8.41 was not independently verified from the provided evidence; the argument assumes it represents a structurally/mechanistically distinct phosphotransferase from the MCR family.
- The MCR family annotation is based on experimental evidence (crystallography, mutagenesis) but the family-level EC assignment across all MCR variants relies on sequence similarity and shared mechanism, not independent experimental validation for every variant.
- The reviewer-only source (UniProt A0A1C3NEV1) was not available to the evaluated model; the reasoning relies on recognizing MCR-family sequence features from general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits the hallmark architecture of the MCR (Mobilized Colistin Resistance) protein family: an N-terminal region (~200 residues) with multiple predicted transmembrane helices (highly hydrophobic stretches: MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDT...) followed by a large (~340 residue) soluble C-terminal catalytic domain. This TM + catalytic domain organization, combined with the ~538 aa total length, is diagnostic of MCR-family phosphoethanolamine transferases. The MCR family (MCR-1 through MCR-10+) is extremely well-characterized in the literature as colistin-resistance enzymes, all uniformly classified as EC 2.7.8.43. The catalytic domain contains conserved zinc-binding and phosphotransferase motifs. This eliminates C (2.5.1.15, alkyltransferase) and D (4.1.1.129, carbon-carbon lyase) because neither matches the TM+phosphotransferase architecture. Distinguishing B (2.7.8.43) from A (2.7.8.41) relies on recognizing the MCR family signature: the specific combination of multiple TM segments, the catalytic domain fold with Zn-coordinating residues, and the overall domain topology are shared across all characterized MCR variants and are all annotated as EC 2.7.8.43. EC 2.7.8.41 represents a mechanistically or structurally distinct phosphotransferase that does not share this MCR architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The MCR protein family is one of the most extensively studied protein families in recent microbiology (discovered 2015-2016, hundreds of publications). The sequence features—multiple TM helices, ~538 aa length, large soluble catalytic domain with Zn-binding—are highly distinctive of this family. A model with knowledge of the MCR family from other homologs (MCR-1, MCR-3, MCR-5, etc.) can recognize the architecture and assign EC 2.7.8.43. Options C and D are eliminated by basic enzyme-class reasoning (lyase and alkyltransferase do not match the observed domain architecture). The distinction between A and B rests on family-level recognition of the MCR catalytic domain fold, which is transferable knowledge from the many characterized MCR homologs."
  },
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) is annotated with EC 2.7.8.43 based on experimental evidence (ECO:0000305, PubMed:30194678) including X-ray crystallography (PDB:6A7W) and functional mutagenesis studies. The catalytic activity is well-defined: transfer of phosphoethanolamine from phosphatidylethanolamine to lipid A. The sequence matches the benchmark input exactly (538 aa, SHA256 match confirmed)."
  },
  "important_caveats": [
    "The exact identity of EC 2.7.8.41 was not independently verified from the provided evidence; the argument assumes it represents a structurally/mechanistically distinct phosphotransferase from the MCR family.",
    "The MCR family annotation is based on experimental evidence (crystallography, mutagenesis) but the family-level EC assignment across all MCR variants relies on sequence similarity and shared mechanism, not independent experimental validation for every variant.",
    "The reviewer-only source (UniProt A0A1C3NEV1) was not available to the evaluated model; the reasoning relies on recognizing MCR-family sequence features from general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.5.1.15) and D (4.1.1.129) are clearly incompatible with the observed TM+phosphotransferase architecture. The MCR family signature is sufficiently distinctive to separate B (2.7.8.43) from A (2.7.8.41), as the MCR family uniformly carries EC 2.7.8.43 and its domain architecture does not match the enzyme class implied by 2.7.8.41."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1C3NEV1 (MCR-2, E. coli) is annotated with EC 2.7.8.43 based on experimental evidence (ECO:0000305, PubMed:30194678) including X-ray crystallography (PDB:6A7W) and functional mutagenesis studies. The catalytic activity is well-defined: transfer of phosphoethanolamine from phosphatidylethanolamine to lipid A. The sequence matches the benchmark input exactly (538 aa, SHA256 match confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits the hallmark architecture of the MCR (Mobilized Colistin Resistance) protein family: an N-terminal region (~200 residues) with multiple predicted transmembrane helices (highly hydrophobic stretches: MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDT...) followed by a large (~340 residue) soluble C-terminal catalytic domain. This TM + catalytic domain organization, combined with the ~538 aa total length, is diagnostic of MCR-family phosphoethanolamine transferases. The MCR family (MCR-1 through MCR-10+) is extremely well-characterized in the literature as colistin-resistance enzymes, all uniformly classified as EC 2.7.8.43. The catalytic domain contains conserved zinc-binding and phosphotransferase motifs. This eliminates C (2.5.1.15, alkyltransferase) and D (4.1.1.129, carbon-carbon lyase) because neither matches the TM+phosphotransferase architecture. Distinguishing B (2.7.8.43) from A (2.7.8.41) relies on recognizing the MCR family signature: the specific combination of multiple TM segments, the catalytic domain fold with Zn-coordinating residues, and the overall domain topology are shared across all characterized MCR variants and are all annotated as EC 2.7.8.43. EC 2.7.8.41 represents a mechanistically or structurally distinct phosphotransferase that does not share this MCR architecture.",
    "missing_item_specific_fact": "",
    "reason": "The MCR protein family is one of the most extensively studied protein families in recent microbiology (discovered 2015-2016, hundreds of publications). The sequence features—multiple TM helices, ~538 aa length, large soluble catalytic domain with Zn-binding—are highly distinctive of this family. A model with knowledge of the MCR family from other homologs (MCR-1, MCR-3, MCR-5, etc.) can recognize the architecture and assign EC 2.7.8.43. Options C and D are eliminated by basic enzyme-class reasoning (lyase and alkyltransferase do not match the observed domain architecture). The distinction between A and B rests on family-level recognition of the MCR catalytic domain fold, which is transferable knowledge from the many characterized MCR homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (2.5.1.15) and D (4.1.1.129) are clearly incompatible with the observed TM+phosphotransferase architecture. The MCR family signature is sufficiently distinctive to separate B (2.7.8.43) from A (2.7.8.41), as the MCR family uniformly carries EC 2.7.8.43 and its domain architecture does not match the enzyme class implied by 2.7.8.41."
  },
  "important_caveats": [
    "The exact identity of EC 2.7.8.41 was not independently verified from the provided evidence; the argument assumes it represents a structurally/mechanistically distinct phosphotransferase from the MCR family.",
    "The MCR family annotation is based on experimental evidence (crystallography, mutagenesis) but the family-level EC assignment across all MCR variants relies on sequence similarity and shared mechanism, not independent experimental validation for every variant.",
    "The reviewer-only source (UniProt A0A1C3NEV1) was not available to the evaluated model; the reasoning relies on recognizing MCR-family sequence features from general biological knowledge."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1C3NEV1",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "selected_historical_version": {
    "accession": "A0A1C3NEV1",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MCR2_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1C3NEV1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"SBV31106.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0R6L508\",\"source\":\"UniProtKB\"}],\"value\":\"Polymyxin resistance protein MCR-2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30194678\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.1\",\"source\":\"Reference\"}],\"value\":\"Phosphatidylethanolamine transferase Mcr-2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.8.43\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"name\":\"lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17815\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64612\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:87097\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:134257\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Lu Q.\",\"Qi J.\",\"Chai Y.\",\"Wang Y.\",\"Gao G.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30194678\"},{\"database\":\"DOI\",\"id\":\"10.1007/s11427-018-9363-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"1432\",\"id\":\"30194678\",\"journal\":\"Sci. China Life Sci.\",\"lastPage\":\"1436\",\"publicationDate\":\"2018\",\"title\":\"Structural and functional insights into MCR-2 mediated colistin resistance.\",\"volume\":\"61\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6A7W\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WHI04997.1\",\"source\":\"EMBL\"}],\"type\":\"PLASMID\",\"value\":\"unnamed5\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)\",\"DISULFIDE BONDS\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   MCR2_ECOLX              Reviewed;         538 AA.\nAC   A0A1C3NEV1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2016, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\nGN   Name=mcr2 {ECO:0000305}; Synonyms=mcr-2 {ECO:0000312|EMBL:SBV31106.1};\nGN   ORFNames=QDW62_28200 {ECO:0000312|EMBL:WHI04997.1};\nOS   Escherichia coli.\nOG   Plasmid pKP37-BE {ECO:0000312|EMBL:SBV31106.1}, and\nOG   Plasmid unnamed5 {ECO:0000312|EMBL:WHI04997.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:SBV31106.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6A7W}\nRP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),\nRP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;\nRP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;\nRP   LYS-331 AND HIS-476.\nRC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};\nRX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;\nRA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;\nRT   \"Structural and functional insights into MCR-2 mediated colistin\nRT   resistance.\";\nRL   Sci. China Life Sci. 61:1432-1436(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-\nCC         phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate)\nCC         (E. coli) + a 1,2-diacyl-sn-glycerol; Xref=Rhea:RHEA:46900,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17815, ChEBI:CHEBI:64612,\nCC         ChEBI:CHEBI:87097, ChEBI:CHEBI:134257; EC=2.7.8.43;\nCC         Evidence={ECO:0000305|PubMed:30194678};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
