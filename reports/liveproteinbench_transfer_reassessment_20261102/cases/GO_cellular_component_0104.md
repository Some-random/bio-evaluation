# GO_cellular_component_0104

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0104.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — cytosol

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. endosome membrane
B. polytene chromosome
C. cytosol
D. heterotrimeric G-protein complex
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports cytosol, with experimental evidence cited for the localization; the archived record also contains this annotation. This supports choice C, while the exact author source snapshot is unknown.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble metabolic enzyme: it has no obvious transmembrane segment or N-terminal secretion signal. Transferable knowledge that chorismate synthase is a globular metabolic enzyme favors a soluble compartment such as cytosol over an endosome membrane, a polytene chromosome, or a heterotrimeric G-protein complex.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The enzyme-family and sequence features provide a meaningful basis to distinguish cytosol from these particularly dissimilar alternatives. That inference is not a guarantee of exact localization, but the choices do not require fine-grained compartment discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, cytosol is meaningfully favored; none of the other options is a comparably plausible location for a soluble metabolic enzyme.


### Important caveats

- The reviewer-only sequence-matched record supports the key, but the author's exact source snapshot is unknown.
- The sequence-based localization argument is probabilistic; absence of an obvious targeting signal alone would not prove cytosolic localization.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic enzyme: it has no obvious transmembrane segment or N-terminal secretion signal. Transferable knowledge that chorismate synthase is a globular metabolic enzyme favors a soluble compartment such as cytosol over an endosome membrane, a polytene chromosome, or a heterotrimeric G-protein complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The enzyme-family and sequence features provide a meaningful basis to distinguish cytosol from these particularly dissimilar alternatives. That inference is not a guarantee of exact localization, but the choices do not require fine-grained compartment discrimination."
  },
  "case_id": "GO_cellular_component_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cytosol, with experimental evidence cited for the localization; the archived record also contains this annotation. This supports choice C, while the exact author source snapshot is unknown."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the key, but the author's exact source snapshot is unknown.",
    "The sequence-based localization argument is probabilistic; absence of an obvious targeting signal alone would not prove cytosolic localization."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytosol is meaningfully favored; none of the other options is a comparably plausible location for a soluble metabolic enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cytosol, with experimental evidence cited for the localization; the archived record also contains this annotation. This supports choice C, while the exact author source snapshot is unknown.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble metabolic enzyme: it has no obvious transmembrane segment or N-terminal secretion signal. Transferable knowledge that chorismate synthase is a globular metabolic enzyme favors a soluble compartment such as cytosol over an endosome membrane, a polytene chromosome, or a heterotrimeric G-protein complex.",
    "missing_item_specific_fact": "",
    "reason": "The enzyme-family and sequence features provide a meaningful basis to distinguish cytosol from these particularly dissimilar alternatives. That inference is not a guarantee of exact localization, but the choices do not require fine-grained compartment discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, cytosol is meaningfully favored; none of the other options is a comparably plausible location for a soluble metabolic enzyme."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the key, but the author's exact source snapshot is unknown.",
    "The sequence-based localization argument is probabilistic; absence of an obvious targeting signal alone would not prove cytosolic localization."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry C6KT66 (chorismate synthase, PfCS) is annotated with subcellular location 'Cytoplasm, cytosol' with experimental evidence (ECO:0000269, PubMed:11298276, Fitzpatrick et al. 2001). The GO annotation GO:0005829 (cytosol) carries evidence type IDA (Inferred from Direct Assay). The sequence matches exactly. This experimental annotation directly supports the expected answer C.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence can be recognized as an AroC/chorismate synthase homolog (conserved FMN-binding and catalytic motifs are present). AroC family members across bacteria and eukaryotes are soluble enzymes. Critically, the N-terminus lacks a signal peptide (no hydrophobic 15–25 residue stretch) and lacks a transit peptide, meaning in Plasmodium this protein is not directed into the secretory pathway or to the apicoplast. The sequence also lacks transmembrane helices (excluding endosome membrane, option A), lacks GTPase/G-domain motifs such as GxxxxGKS or NKxD (excluding heterotrimeric G-protein complex, option D), and is clearly not a chromatin-associated protein (excluding polytene chromosome, option B). The combination of: (1) family-level knowledge that chorismate synthase is a soluble enzyme, (2) absence of any targeting signal in the N-terminus, and (3) absence of structural features required for the other three options, provides a concrete transferable inference pointing to cytosol.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use AroC family knowledge (soluble enzyme in E. coli and other organisms), recognize the absence of signal peptide/transit peptide/TM domain in the N-terminus, and exclude the three non-cytosolic options based on incompatible sequence features. This is a defensible probabilistic generalization from family-level biology, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated: endosome membrane requires TM domains, polytene chromosome requires chromatin association, heterotrimeric G-protein complex requires GTPase subunit architecture. None of these features are present in the sequence. Cytosol is the only option consistent with a soluble enzyme lacking targeting signals.


### Important caveats

- In Plasmodium, the shikimate pathway was initially expected to reside in the apicoplast; the cytoplasmic localization of PfCS was a surprising experimental finding (Fitzpatrick et al. 2001). However, 'apicoplast' is not among the offered options, so this complication does not create ambiguity among the four choices.
- The reviewer-only evidence confirms the annotation is experimental (ECO:0000269, IDA), not merely computational prediction.
- The absence of a signal peptide/transit peptide is inferred from sequence inspection; a trained signal-peptide predictor would be needed for definitive confirmation, but the N-terminal region visibly lacks the hydrophobic character expected of a signal peptide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence can be recognized as an AroC/chorismate synthase homolog (conserved FMN-binding and catalytic motifs are present). AroC family members across bacteria and eukaryotes are soluble enzymes. Critically, the N-terminus lacks a signal peptide (no hydrophobic 15–25 residue stretch) and lacks a transit peptide, meaning in Plasmodium this protein is not directed into the secretory pathway or to the apicoplast. The sequence also lacks transmembrane helices (excluding endosome membrane, option A), lacks GTPase/G-domain motifs such as GxxxxGKS or NKxD (excluding heterotrimeric G-protein complex, option D), and is clearly not a chromatin-associated protein (excluding polytene chromosome, option B). The combination of: (1) family-level knowledge that chorismate synthase is a soluble enzyme, (2) absence of any targeting signal in the N-terminus, and (3) absence of structural features required for the other three options, provides a concrete transferable inference pointing to cytosol.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use AroC family knowledge (soluble enzyme in E. coli and other organisms), recognize the absence of signal peptide/transit peptide/TM domain in the N-terminus, and exclude the three non-cytosolic options based on incompatible sequence features. This is a defensible probabilistic generalization from family-level biology, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0104",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry C6KT66 (chorismate synthase, PfCS) is annotated with subcellular location 'Cytoplasm, cytosol' with experimental evidence (ECO:0000269, PubMed:11298276, Fitzpatrick et al. 2001). The GO annotation GO:0005829 (cytosol) carries evidence type IDA (Inferred from Direct Assay). The sequence matches exactly. This experimental annotation directly supports the expected answer C."
  },
  "important_caveats": [
    "In Plasmodium, the shikimate pathway was initially expected to reside in the apicoplast; the cytoplasmic localization of PfCS was a surprising experimental finding (Fitzpatrick et al. 2001). However, 'apicoplast' is not among the offered options, so this complication does not create ambiguity among the four choices.",
    "The reviewer-only evidence confirms the annotation is experimental (ECO:0000269, IDA), not merely computational prediction.",
    "The absence of a signal peptide/transit peptide is inferred from sequence inspection; a trained signal-peptide predictor would be needed for definitive confirmation, but the N-terminal region visibly lacks the hydrophobic character expected of a signal peptide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: endosome membrane requires TM domains, polytene chromosome requires chromatin association, heterotrimeric G-protein complex requires GTPase subunit architecture. None of these features are present in the sequence. Cytosol is the only option consistent with a soluble enzyme lacking targeting signals."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0104",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry C6KT66 (chorismate synthase, PfCS) is annotated with subcellular location 'Cytoplasm, cytosol' with experimental evidence (ECO:0000269, PubMed:11298276, Fitzpatrick et al. 2001). The GO annotation GO:0005829 (cytosol) carries evidence type IDA (Inferred from Direct Assay). The sequence matches exactly. This experimental annotation directly supports the expected answer C.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence can be recognized as an AroC/chorismate synthase homolog (conserved FMN-binding and catalytic motifs are present). AroC family members across bacteria and eukaryotes are soluble enzymes. Critically, the N-terminus lacks a signal peptide (no hydrophobic 15–25 residue stretch) and lacks a transit peptide, meaning in Plasmodium this protein is not directed into the secretory pathway or to the apicoplast. The sequence also lacks transmembrane helices (excluding endosome membrane, option A), lacks GTPase/G-domain motifs such as GxxxxGKS or NKxD (excluding heterotrimeric G-protein complex, option D), and is clearly not a chromatin-associated protein (excluding polytene chromosome, option B). The combination of: (1) family-level knowledge that chorismate synthase is a soluble enzyme, (2) absence of any targeting signal in the N-terminus, and (3) absence of structural features required for the other three options, provides a concrete transferable inference pointing to cytosol.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use AroC family knowledge (soluble enzyme in E. coli and other organisms), recognize the absence of signal peptide/transit peptide/TM domain in the N-terminus, and exclude the three non-cytosolic options based on incompatible sequence features. This is a defensible probabilistic generalization from family-level biology, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated: endosome membrane requires TM domains, polytene chromosome requires chromatin association, heterotrimeric G-protein complex requires GTPase subunit architecture. None of these features are present in the sequence. Cytosol is the only option consistent with a soluble enzyme lacking targeting signals."
  },
  "important_caveats": [
    "In Plasmodium, the shikimate pathway was initially expected to reside in the apicoplast; the cytoplasmic localization of PfCS was a surprising experimental finding (Fitzpatrick et al. 2001). However, 'apicoplast' is not among the offered options, so this complication does not create ambiguity among the four choices.",
    "The reviewer-only evidence confirms the annotation is experimental (ECO:0000269, IDA), not merely computational prediction.",
    "The absence of a signal peptide/transit peptide is inferred from sequence inspection; a trained signal-peptide predictor would be needed for definitive confirmation, but the N-terminal region visibly lacks the hydrophobic character expected of a signal peptide."
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
  "benchmark_sequence_length": 527,
  "benchmark_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 527,
  "current_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "C6KT66",
  "selected_historical_entry_version": 89,
  "selected_historical_record_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "selected_historical_source_sequence_length": 527,
  "selected_historical_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "selected_historical_version": {
    "accession": "C6KT66",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AROC_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"C6KT66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"value\":\"PfCS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"id\":\"SL-0091\",\"value\":\"Cytoplasm, cytosol\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"id\":\"GO:0005829\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytosol\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Fitzpatrick T.\",\"Ricken S.\",\"Lanzer M.\",\"Amrhein N.\",\"Macheroux P.\",\"Kappes B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11298276\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.2001.02366.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"65\",\"id\":\"11298276\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"75\",\"publicationDate\":\"2001\",\"title\":\"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"DD2\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H1",
  "excerpt": "ID   AROC_PLAF7              Reviewed;         527 AA.\nAC   C6KT66;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};\nGN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};\nRX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;\nRA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;\nRT   \"Subcellular localization and characterization of chorismate synthase in\nRT   the apicomplexan Plasmodium falciparum.\";\nRL   Mol. Microbiol. 40:65-75(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:11298276}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "entry_version": 89,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005829; C:cytosol; IDA:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005700\nname: polytene chromosome\nnamespace: cellular_component\ndef: \"A type of chromosome in a polyploid cell, formed when multiple copies of homologous chromosomes are aligned side by side to give a giant chromosome in which distinct chromosome bands are readily visible.\" [ISBN:0198506732]\nxref: Wikipedia:Polytene_chromosome\nis_a: GO:0005694 ! chromosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005700",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58649-58656",
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
  "excerpt": "[Term]\nid: GO:0005829\nname: cytosol\nnamespace: cellular_component\ndef: \"The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes.\" [GOC:hjd, GOC:jl]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nxref: NIF_Subcellular:sao101633890\nxref: Wikipedia:Cytosol\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005829",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59936-59953",
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
  "excerpt": "[Term]\nid: GO:0005834\nname: heterotrimeric G-protein complex\nnamespace: cellular_component\ndef: \"Any of a family of heterotrimeric GTP-binding and hydrolyzing proteins; they belong to a superfamily of GTPases that includes monomeric proteins such as EF-Tu and RAS. Heterotrimeric G-proteins consist of three subunits; the alpha subunit contains the guanine nucleotide binding site and possesses GTPase activity; the beta and gamma subunits are tightly associated and function as a beta-gamma heterodimer; extrinsic plasma membrane proteins (cytoplasmic face) that function as a complex to transduce signals from G protein-coupled receptors to an effector protein.\" [ISBN:0198547684]\ncomment: See also the molecular function term 'G protein-coupled receptor activity ; GO:0004930'.\nsynonym: \"heterotrimeric G-protein GTPase activity\" RELATED []\nsynonym: \"heterotrimeric G-protein GTPase, alpha-subunit\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, beta-subunit\" NARROW []\nsynonym: \"heterotrimeric G-protein GTPase, gamma-subunit\" NARROW []\nis_a: GO:0098797 ! plasma membrane protein complex\nis_a: GO:1905360 ! GTPase complex\nrelationship: part_of GO:0031234 ! extrinsic component of cytoplasmic side of plasma membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005834",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 59981-59994",
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
  "excerpt": "[Term]\nid: GO:0010008\nname: endosome membrane\nnamespace: cellular_component\ndef: \"The lipid bilayer surrounding an endosome.\" [GOC:mah]\nsynonym: \"endosomal membrane\" EXACT [NIF_Subcellular:sao978443756]\nxref: NIF_Subcellular:sao978443756\nis_a: GO:0030659 ! cytoplasmic vesicle membrane\nis_a: GO:0098588 ! bounding membrane of organelle\nrelationship: part_of GO:0005768 ! endosome\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010008",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 101976-101986",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 104. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
