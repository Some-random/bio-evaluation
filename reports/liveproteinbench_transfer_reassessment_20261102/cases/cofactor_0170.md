# cofactor_0170

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0170.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MISKSIILRFSELSMRKKATLVGLPLLAVAAISSSLNSPTRQQRIELSLPESPLVQFSSAEHTVEVVKVGHPDYEYEIKPGDNLSTIFNQLGFAYTELMKVMETDLNYLALDTLRPGNVLRFWKGSDNTLAKMELEFSLVDRAVYTRLNDGSYEFEERKIPGTWKVEPLIGEVDGSFSLSANRAGLGAADVDQIVTLLKDKINFGRDLRRGDRFEVVLSRQLVGEKLTGNSEIQAIKIFNRGKEITAYLHQDGQYYDKNGDSLQRAFQRYPVDSKWRISSNFDPRRLHPVTKRVAPHNGTDFAMPIGTPVYTSGDGVVVMTRNHPYAGNYVVIQHGNTYMTRYLHLSKILVKKGQKVSRGQRIGLSGNTGRVTGPHLHYELIVRGRPVNAMKANIPMASSVPKKEMAQFIAKRKELDQMLARQESMLAAQ

[Multiple Choices]
A. Zn(2+)
B. pantetheine 4'-phosphate
C. FAD
D. Mo-bis(molybdopterin guanine dinucleotide)
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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1140)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates Zn(2+) as a cofactor and says that each subunit binds one zinc ion, with experimental evidence code ECO:0000269. This supports the keyed choice.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal export signal and an enzyme-like region with histidine/aspartate-rich motifs, a pattern consistent with an exported metallopeptidase. Transferable knowledge of zinc-dependent peptidases makes Zn(2+) a credible choice; the alternatives are less consistent with this sequence, which lacks an obvious flavoprotein or molybdenum-enzyme signature.",
    "missing_item_specific_fact": "",
    "reason": "A family-level metallopeptidase inference from the sequence can meaningfully distinguish zinc from the other offered cofactors, even without knowing the exact protein's annotation. The inference is probabilistic, not a direct demonstration of metal binding from sequence alone.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered cofactor is comparably supported by the sequence-level metallopeptidase inference."
  },
  "important_caveats": [
    "The source annotation reports zinc binding; binding alone is not a complete demonstration that zinc is essential for catalysis. The experimental cofactor annotation supports the key, but the underlying study was not independently reviewed here."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices.


### Important caveats

- The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.
- The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.
- The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases."
  },
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.",
    "The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.",
    "The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q9KN86) annotates this protein as Peptidoglycan DD-endopeptidase ShyA (EC 3.4.24.-), a metalloendopeptidase. The cofactor is explicitly annotated as Zn(2+) with experimental evidence (ECO:0000269|PubMed:32393643), confirmed by X-ray crystallography (PDB 6U2A, 6UE4) showing the protein in complex with Zn(2+). The entry also lists 'Zn-metalloprotease' as an alternative name. The answer A (Zn(2+)) is directly supported by structural and biochemical evidence.",
    "evidence_ids": ["C5", "C8", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish Zn(2+) from the other three options through multiple transferable lines of reasoning: (1) The sequence contains a hydrophobic N-terminal signal peptide (GLPLLAVAAISSS) indicating periplasmic/extracellular localization, and the overall domain architecture with clustered histidines in the C-terminal region (e.g., HPYAG...QHG...PHLHY) is consistent with a metalloprotease active site. (2) Peptidases/proteases overwhelmingly use metal-ion cofactors, most commonly Zn(2+), whereas FAD is a cofactor for oxidoreductases, Mo-bis-MGD is specific to certain anaerobic oxidoreductases (nitrate reductase, DMSO reductase), and pantetheine 4'-phosphate is a prosthetic group for acyl carrier proteins or phosphopantetheinyl transferases. None of these three alternative cofactors are ever used by peptidases. (3) The sequence lacks Rossmann-fold motifs (GxGxxG) for FAD binding, lacks the distinctive molybdopterin-binding fold, and lacks the ACP-like short helical bundle for pantetheine attachment. (4) The presence of multiple histidines in spatial proximity in the C-terminal catalytic domain is a hallmark of zinc coordination in metalloproteases (M23, M48, and related families). Together, these features allow a model to confidently select Zn(2+) while eliminating the other three options as belonging to entirely different enzyme classes.",
    "missing_item_specific_fact": "",
    "reason": "The four answer choices belong to four distinct enzyme classes (metalloprotease, acyl-transfer, flavoprotein oxidoreductase, molybdoenzyme). Recognizing the sequence as a peptidase/protease and noting the absence of FAD-binding, molybdopterin-binding, or pantetheine-attachment motifs allows elimination of B, C, and D. The clustered histidines further support zinc coordination. This is standard family-level and class-level biological reasoning transferable from knowledge of other metalloproteases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options correspond to four mutually exclusive enzyme classes. A peptidase sequence cannot plausibly use FAD, Mo-bis-MGD, or pantetheine 4'-phosphate as its catalytic cofactor. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The reviewer evidence confirms the protein is ShyA (Q9KN86) from Vibrio cholerae, but this identity was not provided to the evaluated model. The reasoning relies solely on sequence features and general enzyme-class knowledge.",
    "The EC 3.4.24.- designation (metalloendopeptidase) is assigned in the UniProt entry with experimental evidence, but the model must infer the protease class from sequence features rather than from a provided annotation.",
    "The exact zinc-binding residues (His-376, His-378) were confirmed by mutagenesis and crystallography; a model identifying histidine clusters in the C-terminal region is making a reasonable structural inference consistent with known metalloprotease families."
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
  "benchmark_sequence_length": 430,
  "benchmark_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "current_entry_audit": {
    "entryVersion": 112,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 430,
  "current_source_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 110,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9KN86",
  "selected_historical_entry_version": 110,
  "selected_historical_record_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "selected_historical_source_sequence_length": 430,
  "selected_historical_source_sequence_sha256": "0520ed638d8cdb09bee8796cafa9092296b04e973c78b3a4073bed6df5a3e163",
  "selected_historical_version": {
    "accession": "Q9KN86",
    "database": "Swiss-Prot",
    "entryVersion": 110,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SHYA_VIBCH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9KN86\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":112,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF95993.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000584\",\"source\":\"Proteomes\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Vibrionales\",\"Vibrionaceae\",\"Vibrio\"],\"scientificName\":\"Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961)\",\"taxonId\":243277}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Autolysin ShyA\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Major peptidoglycan endopeptidase ShyA\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Major PG EP ShyA\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Sidewall hydrolase A\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"value\":\"Zn-metalloprotease\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23834664\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30782657\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"3.4.24.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"value\":\"Peptidoglycan DD-endopeptidase ShyA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 zinc ion per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Doerr T.\",\"Cava F.\",\"Lam H.\",\"Davis B.M.\",\"Waldor M.K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23834664\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12323\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"23834664\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"962\",\"publicationDate\":\"2013\",\"title\":\"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.\",\"volume\":\"89\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23834664\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBSTRATE SPECIFICITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-378\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Murphy S.G.\",\"Alvarez L.\",\"Adams M.C.\",\"Liu S.\",\"Chappie J.S.\",\"Cava F.\",\"Doerr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30782657\"},{\"database\":\"DOI\",\"id\":\"10.1128/mbio.02620-18\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30782657\",\"journal\":\"MBio\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc Starvation Response.\",\"volume\":\"10\"},\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30782657\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KN86.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Shin J.H.\",\"Sulpizio A.G.\",\"Kelley A.\",\"Alvarez L.\",\"Murphy S.G.\",\"Fan L.\",\"Cava F.\",\"Mao Y.\",\"Saper M.A.\",\"Dorr T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32393643\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.2001661117\"}],\"citationType\":\"journal article\",\"firstPage\":\"11692\",\"id\":\"32393643\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"11702\",\"publicationDate\":\"2020\",\"title\":\"Structural basis of peptidoglycan endopeptidase regulation.\",\"volume\":\"117\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6U2A\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6UE4\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32393643\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ATCC 39315 / El Tor Inaba N16961\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"PATHWAY\",\"SUBCELLULAR LOCATION\",\"DOMAIN\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF 1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112; ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND 427-LEU--GLN-430\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:59.163450+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "44d2c8a45b16e56b34df4f1bd7d0a028fa3ca633fa1e652a9c6c6017353865da",
  "url": "https://rest.uniprot.org/uniprotkb/Q9KN86.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H1",
  "excerpt": "ID   SHYA_VIBCH              Reviewed;         430 AA.\nAC   Q9KN86;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2000, sequence version 1.\nDT   28-JAN-2026, entry version 110.\nDE   RecName: Full=Peptidoglycan DD-endopeptidase ShyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:23834664, ECO:0000269|PubMed:30782657, ECO:0000269|PubMed:32393643};\nDE   AltName: Full=Autolysin ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Major peptidoglycan endopeptidase ShyA {ECO:0000303|PubMed:32393643};\nDE            Short=Major PG EP ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Sidewall hydrolase A {ECO:0000303|PubMed:23834664};\nDE   AltName: Full=Zn-metalloprotease {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\nGN   Name=shyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nGN   OrderedLocusNames=VC_A0079 {ECO:0000303|PubMed:23834664,\nGN   ECO:0000312|EMBL:AAF95993.1};\nOS   Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Vibrionales;\nOC   Vibrionaceae; Vibrio.\nOX   NCBI_TaxID=243277 {ECO:0000312|EMBL:AAF95993.1, ECO:0000312|Proteomes:UP000000584};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Peptidoglycan DD-endopeptidase ShyA {ECO:0000303|PubMed:23834664, ECO:0000303|PubMed:30782657};\nDE            EC=3.4.24.- {ECO:0000269|PubMed:23834664, ECO:0000269|PubMed:30782657, ECO:0000269|PubMed:32393643};\nDE   AltName: Full=Autolysin ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Major peptidoglycan endopeptidase ShyA {ECO:0000303|PubMed:32393643};\nDE            Short=Major PG EP ShyA {ECO:0000303|PubMed:32393643};\nDE   AltName: Full=Sidewall hydrolase A {ECO:0000303|PubMed:23834664};\nDE   AltName: Full=Zn-metalloprotease {ECO:0000303|PubMed:23834664};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBCELLULAR LOCATION, DISRUPTION\nRP   PHENOTYPE, AND MUTAGENESIS OF HIS-378.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:23834664};\nRX   PubMed=23834664; DOI=10.1111/mmi.12323;\nRA   Doerr T., Cava F., Lam H., Davis B.M., Waldor M.K.;\nRT   \"Substrate specificity of an elongation-specific peptidoglycan\nRT   endopeptidase and its implications for cell wall architecture and growth of\nRT   Vibrio cholerae.\";\nRL   Mol. Microbiol. 89:949-962(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:30782657};\nRX   PubMed=30782657; DOI=10.1128/mbio.02620-18;\nRA   Murphy S.G., Alvarez L., Adams M.C., Liu S., Chappie J.S., Cava F.,\nRA   Doerr T.;\nRT   \"Endopeptidase Regulation as a Novel Function of the Zur-Dependent Zinc\nRT   Starvation Response.\";\nRL   MBio 10:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H5",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6U2A, ECO:0007744|PDB:6UE4}\nRP   X-RAY CRYSTALLOGRAPHY (2.08 ANGSTROMS) OF 36-430 IN COMPLEX WITH ZN(2+),\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, PATHWAY,\nRP   SUBCELLULAR LOCATION, DOMAIN, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF\nRP   1-MET--ARG-265; 1-MET--ILE-160; 1-MET--VAL-66; GLU-103; LEU-109; ASP-112;\nRP   ARG-286; HIS-297; ASP-301; LEU-344; HIS-345; HIS-376; HIS-378 AND\nRP   427-LEU--GLN-430.\nRC   STRAIN=ATCC 39315 / El Tor Inaba N16961 {ECO:0000303|PubMed:32393643};\nRX   PubMed=32393643; DOI=10.1073/pnas.2001661117;\nRA   Shin J.H., Sulpizio A.G., Kelley A., Alvarez L., Murphy S.G., Fan L.,\nRA   Cava F., Mao Y., Saper M.A., Dorr T.;\nRT   \"Structural basis of peptidoglycan endopeptidase regulation.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 117:11692-11702(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110)

```json
{
  "entry_version": 110,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000269|PubMed:32393643};\nCC       Note=Binds 1 zinc ion per subunit. {ECO:0000269|PubMed:32393643};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:01.774065+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cae96b85e934e839cb149ce7330703f9f664096875a15b934b8fdd0af9ad226f",
  "url": "https://rest.uniprot.org/unisave/Q9KN86?format=txt&versions=110"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
