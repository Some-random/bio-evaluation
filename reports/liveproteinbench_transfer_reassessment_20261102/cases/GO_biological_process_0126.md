# GO_biological_process_0126

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0126.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — transcription by RNA polymerase II

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNYNAKRVMRQNSVCVGSNDMAASPIMIGPAPPSAPSTPQLQTTEDIKPLLVQRQVILLQSGSIPTNPSPQQINLAGHNVAGGASGSNVANVLIPDDAPVSLLTEIADIMRSFGDSDQPRTGSVKLVEQILQQQLRGIFNEASLVAMRRKQNPCPSQADFEFLMRNHPVKIARMRKHLKDMRILKRFLSIRTGRPQDFMDDLEQQEEDEELAIDVYELHDEDRMRRLFRADRISQILTGQQYLEFNEARKTSFYCRHGEKIKNKFRRFLDLPADLRIPTPTMNILAYLAHETIAAIVDYSILTRLNSDNRATEPYSRVTSAGGSPAMMHVCPEVTQGRGMEVVKPISVPEIHEAMRRFRQMSSRKIGRYRNSCDIDFRRSFLAI

[Multiple Choices]
A. ribosome biogenesis
B. transcription by RNA polymerase II
C. protein quality control for misfolded or incompletely synthesized proteins
D. glycolytic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the reviewed protein record. That record identifies the protein as a SAGA complex subunit and describes SAGA-mediated transcriptional activation, with cited experimental evidence; it also assigns transcription by RNA polymerase II, though that GO annotation is computational (IEA:InterPro). This supports B as the best offered process.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A family-level inference that this sequence is an Spt3-like SAGA subunit points to transcriptional regulation: SAGA is a eukaryotic transcription-regulatory complex that helps activate transcription, including through chromatin modification. That meaningfully favors B over ribosome biogenesis, protein quality control, or glycolysis. The inference relies on transferable recognition of the protein family and SAGA’s general role, not on recalling this exact protein’s annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered choices contrast distinct processes, and transferable family knowledge gives a credible basis for selecting transcription by RNA polymerase II. The precise target’s annotation is not necessary to distinguish B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other options describe processes not indicated by the Spt3/SAGA family inference; no competing offered option is comparably supported.


### Important caveats

- The GO assignment for transcription by RNA polymerase II is computationally inferred, while the source record’s SAGA transcription-activation function cites experimental evidence.
- The sequence was matched to the reviewer-only source record; that identity and annotation were not original inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A family-level inference that this sequence is an Spt3-like SAGA subunit points to transcriptional regulation: SAGA is a eukaryotic transcription-regulatory complex that helps activate transcription, including through chromatin modification. That meaningfully favors B over ribosome biogenesis, protein quality control, or glycolysis. The inference relies on transferable recognition of the protein family and SAGA’s general role, not on recalling this exact protein’s annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered choices contrast distinct processes, and transferable family knowledge gives a credible basis for selecting transcription by RNA polymerase II. The precise target’s annotation is not necessary to distinguish B."
  },
  "case_id": "GO_biological_process_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record. That record identifies the protein as a SAGA complex subunit and describes SAGA-mediated transcriptional activation, with cited experimental evidence; it also assigns transcription by RNA polymerase II, though that GO annotation is computational (IEA:InterPro). This supports B as the best offered process."
  },
  "important_caveats": [
    "The GO assignment for transcription by RNA polymerase II is computationally inferred, while the source record’s SAGA transcription-activation function cites experimental evidence.",
    "The sequence was matched to the reviewer-only source record; that identity and annotation were not original inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe processes not indicated by the Spt3/SAGA family inference; no competing offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the reviewed protein record. That record identifies the protein as a SAGA complex subunit and describes SAGA-mediated transcriptional activation, with cited experimental evidence; it also assigns transcription by RNA polymerase II, though that GO annotation is computational (IEA:InterPro). This supports B as the best offered process.",
    "evidence_ids": ["C1", "C4", "C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A family-level inference that this sequence is an Spt3-like SAGA subunit points to transcriptional regulation: SAGA is a eukaryotic transcription-regulatory complex that helps activate transcription, including through chromatin modification. That meaningfully favors B over ribosome biogenesis, protein quality control, or glycolysis. The inference relies on transferable recognition of the protein family and SAGA’s general role, not on recalling this exact protein’s annotation.",
    "missing_item_specific_fact": "",
    "reason": "The offered choices contrast distinct processes, and transferable family knowledge gives a credible basis for selecting transcription by RNA polymerase II. The precise target’s annotation is not necessary to distinguish B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other options describe processes not indicated by the Spt3/SAGA family inference; no competing offered option is comparably supported."
  },
  "important_caveats": [
    "The GO assignment for transcription by RNA polymerase II is computationally inferred, while the source record’s SAGA transcription-activation function cites experimental evidence.",
    "The sequence was matched to the reviewer-only source record; that identity and annotation were not original inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Spt3 (Q9VGE2), a core subunit of the Drosophila SAGA/ADA transcription coactivator complex. Multiple experimental studies (PubMed:12697829, 16980620, 18188155, 21764853, 24493646, 30559249, 34807910) confirm its role in chromatin remodeling and histone acetylation/deubiquitination to activate transcription. The UniProt entry carries GO:0006366 (transcription by RNA polymerase II) via IEA:InterPro and GO:0045893 (positive regulation of DNA-templated transcription) via NAS:ComplexPortal. The SAGA complex is a well-established Pol II coactivator, and Spt3 specifically contacts TBP to facilitate transcription initiation. The answer B is well-supported by both experimental and computational annotation evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H9](#evidence-h9), [H10](#evidence-h10), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Spt3 is a highly conserved protein family found across eukaryotes (yeast SPT3, human SPT3, and homologs in numerous organisms). All known Spt3-family members are core subunits of the SAGA/ADA coactivator complex, which is universally and exclusively associated with RNA polymerase II transcription. The sequence shows features consistent with the Spt3 family: approximately 384 residues, a TBP-interacting domain region with conserved motifs, and no catalytic or structural domains characteristic of glycolytic enzymes (no Rossmann fold, no sugar-phosphate binding residues), ribosome biogenesis factors (no RNA-binding or helicase domains), or protein quality control machinery (no chaperone, protease, or E3 ligase domains). A knowledgeable model recognizing the Spt3 family pattern—through conserved sequence motifs, overall architecture, or family-level similarity to yeast/human Spt3—can confidently assign the protein to the SAGA/ADA complex and thereby to Pol II transcription. The other three options (ribosome biogenesis, protein quality control, glycolysis) have no mechanistic or family-level connection to Spt3 or the SAGA complex in any characterized organism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Spt3 family is one of the most well-characterized transcription coactivator subunits across eukaryotes. Recognizing the protein as a Spt3-family member through sequence features (conserved TBP-interacting region, overall length and composition, absence of enzymatic domains) and applying the universal family-level association (Spt3 → SAGA/ADA → Pol II transcription) provides a concrete, transferable inference that cleanly distinguishes option B from A, C, and D. This does not require knowing the specific Drosophila Spt3 annotation; it relies on the well-established functional identity of the Spt3 protein family learned from yeast, human, and other homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B (transcription by RNA polymerase II) is the only choice consistent with Spt3/SAGA complex function. The other options—ribosome biogenesis, protein quality control, and glycolysis—have no known mechanistic connection to Spt3-family proteins in any organism. The distractors are clearly non-overlapping biological processes with distinct protein families and domain architectures absent from this sequence.


### Important caveats

- The GO:0006366 annotation in UniProt carries IEA:InterPro evidence (computational transfer from InterPro), while the stronger functional evidence (ECO:0000269, experimental) supports the broader GO:0045893 (positive regulation of DNA-templated transcription). The specific assignment to Pol II rather than Pol I or Pol III is well-supported by the SAGA complex literature but is annotated at the IEA level in this entry.
- The reviewer-only evidence identifies the protein as Q9VGE2 (SPT3_DROME) from Drosophila melanogaster. This identification was not available to the evaluated model; the model must rely on sequence features and family-level knowledge.
- The Spt3 family recognition argument assumes the model can identify Spt3-like sequence features from the raw 384-aa sequence. While the family is well-conserved, the strength of recognition from a Drosophila sequence without prior database lookup depends on the model's training data coverage of Spt3 homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Spt3 is a highly conserved protein family found across eukaryotes (yeast SPT3, human SPT3, and homologs in numerous organisms). All known Spt3-family members are core subunits of the SAGA/ADA coactivator complex, which is universally and exclusively associated with RNA polymerase II transcription. The sequence shows features consistent with the Spt3 family: approximately 384 residues, a TBP-interacting domain region with conserved motifs, and no catalytic or structural domains characteristic of glycolytic enzymes (no Rossmann fold, no sugar-phosphate binding residues), ribosome biogenesis factors (no RNA-binding or helicase domains), or protein quality control machinery (no chaperone, protease, or E3 ligase domains). A knowledgeable model recognizing the Spt3 family pattern—through conserved sequence motifs, overall architecture, or family-level similarity to yeast/human Spt3—can confidently assign the protein to the SAGA/ADA complex and thereby to Pol II transcription. The other three options (ribosome biogenesis, protein quality control, glycolysis) have no mechanistic or family-level connection to Spt3 or the SAGA complex in any characterized organism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Spt3 family is one of the most well-characterized transcription coactivator subunits across eukaryotes. Recognizing the protein as a Spt3-family member through sequence features (conserved TBP-interacting region, overall length and composition, absence of enzymatic domains) and applying the universal family-level association (Spt3 → SAGA/ADA → Pol II transcription) provides a concrete, transferable inference that cleanly distinguishes option B from A, C, and D. This does not require knowing the specific Drosophila Spt3 annotation; it relies on the well-established functional identity of the Spt3 protein family learned from yeast, human, and other homologs."
  },
  "case_id": "GO_biological_process_0126",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H9",
      "H10",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is Spt3 (Q9VGE2), a core subunit of the Drosophila SAGA/ADA transcription coactivator complex. Multiple experimental studies (PubMed:12697829, 16980620, 18188155, 21764853, 24493646, 30559249, 34807910) confirm its role in chromatin remodeling and histone acetylation/deubiquitination to activate transcription. The UniProt entry carries GO:0006366 (transcription by RNA polymerase II) via IEA:InterPro and GO:0045893 (positive regulation of DNA-templated transcription) via NAS:ComplexPortal. The SAGA complex is a well-established Pol II coactivator, and Spt3 specifically contacts TBP to facilitate transcription initiation. The answer B is well-supported by both experimental and computational annotation evidence."
  },
  "important_caveats": [
    "The GO:0006366 annotation in UniProt carries IEA:InterPro evidence (computational transfer from InterPro), while the stronger functional evidence (ECO:0000269, experimental) supports the broader GO:0045893 (positive regulation of DNA-templated transcription). The specific assignment to Pol II rather than Pol I or Pol III is well-supported by the SAGA complex literature but is annotated at the IEA level in this entry.",
    "The reviewer-only evidence identifies the protein as Q9VGE2 (SPT3_DROME) from Drosophila melanogaster. This identification was not available to the evaluated model; the model must rely on sequence features and family-level knowledge.",
    "The Spt3 family recognition argument assumes the model can identify Spt3-like sequence features from the raw 384-aa sequence. While the family is well-conserved, the strength of recognition from a Drosophila sequence without prior database lookup depends on the model's training data coverage of Spt3 homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (transcription by RNA polymerase II) is the only choice consistent with Spt3/SAGA complex function. The other options—ribosome biogenesis, protein quality control, and glycolysis—have no known mechanistic connection to Spt3-family proteins in any organism. The distractors are clearly non-overlapping biological processes with distinct protein families and domain architectures absent from this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0126",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Spt3 (Q9VGE2), a core subunit of the Drosophila SAGA/ADA transcription coactivator complex. Multiple experimental studies (PubMed:12697829, 16980620, 18188155, 21764853, 24493646, 30559249, 34807910) confirm its role in chromatin remodeling and histone acetylation/deubiquitination to activate transcription. The UniProt entry carries GO:0006366 (transcription by RNA polymerase II) via IEA:InterPro and GO:0045893 (positive regulation of DNA-templated transcription) via NAS:ComplexPortal. The SAGA complex is a well-established Pol II coactivator, and Spt3 specifically contacts TBP to facilitate transcription initiation. The answer B is well-supported by both experimental and computational annotation evidence.",
    "evidence_ids": ["C5", "C6", "C7", "H9", "H10", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Spt3 is a highly conserved protein family found across eukaryotes (yeast SPT3, human SPT3, and homologs in numerous organisms). All known Spt3-family members are core subunits of the SAGA/ADA coactivator complex, which is universally and exclusively associated with RNA polymerase II transcription. The sequence shows features consistent with the Spt3 family: approximately 384 residues, a TBP-interacting domain region with conserved motifs, and no catalytic or structural domains characteristic of glycolytic enzymes (no Rossmann fold, no sugar-phosphate binding residues), ribosome biogenesis factors (no RNA-binding or helicase domains), or protein quality control machinery (no chaperone, protease, or E3 ligase domains). A knowledgeable model recognizing the Spt3 family pattern—through conserved sequence motifs, overall architecture, or family-level similarity to yeast/human Spt3—can confidently assign the protein to the SAGA/ADA complex and thereby to Pol II transcription. The other three options (ribosome biogenesis, protein quality control, glycolysis) have no mechanistic or family-level connection to Spt3 or the SAGA complex in any characterized organism.",
    "missing_item_specific_fact": "",
    "reason": "The Spt3 family is one of the most well-characterized transcription coactivator subunits across eukaryotes. Recognizing the protein as a Spt3-family member through sequence features (conserved TBP-interacting region, overall length and composition, absence of enzymatic domains) and applying the universal family-level association (Spt3 → SAGA/ADA → Pol II transcription) provides a concrete, transferable inference that cleanly distinguishes option B from A, C, and D. This does not require knowing the specific Drosophila Spt3 annotation; it relies on the well-established functional identity of the Spt3 protein family learned from yeast, human, and other homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (transcription by RNA polymerase II) is the only choice consistent with Spt3/SAGA complex function. The other options—ribosome biogenesis, protein quality control, and glycolysis—have no known mechanistic connection to Spt3-family proteins in any organism. The distractors are clearly non-overlapping biological processes with distinct protein families and domain architectures absent from this sequence."
  },
  "important_caveats": [
    "The GO:0006366 annotation in UniProt carries IEA:InterPro evidence (computational transfer from InterPro), while the stronger functional evidence (ECO:0000269, experimental) supports the broader GO:0045893 (positive regulation of DNA-templated transcription). The specific assignment to Pol II rather than Pol I or Pol III is well-supported by the SAGA complex literature but is annotated at the IEA level in this entry.",
    "The reviewer-only evidence identifies the protein as Q9VGE2 (SPT3_DROME) from Drosophila melanogaster. This identification was not available to the evaluated model; the model must rely on sequence features and family-level knowledge.",
    "The Spt3 family recognition argument assumes the model can identify Spt3-like sequence features from the raw 384-aa sequence. While the family is well-conserved, the strength of recognition from a Drosophila sequence without prior database lookup depends on the model's training data coverage of Spt3 homologs."
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
  "benchmark_sequence_length": 384,
  "benchmark_sequence_sha256": "e0389cd258ac924119b552c4edc0539fb5d9070cc7b7059e0964469018c63e5f",
  "current_entry_audit": {
    "entryVersion": 199,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 384,
  "current_source_sequence_sha256": "e0389cd258ac924119b552c4edc0539fb5d9070cc7b7059e0964469018c63e5f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 197,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VGE2",
  "selected_historical_entry_version": 197,
  "selected_historical_record_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "selected_historical_source_sequence_length": 384,
  "selected_historical_source_sequence_sha256": "e0389cd258ac924119b552c4edc0539fb5d9070cc7b7059e0964469018c63e5f",
  "selected_historical_version": {
    "accession": "Q9VGE2",
    "database": "Swiss-Prot",
    "entryVersion": 197,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "SPT3_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VGE2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":199,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Suppressor of Ty protein 3 homolog\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"SAGA complex subunit Spt3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12697829\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16980620\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18188155\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21764853\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"24493646\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30559249\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34807910\",\"source\":\"PubMed\"}],\"value\":\"Component of the transcription regulatory complex SAGA, a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination (PubMed:12697829, PubMed:16980620, PubMed:18188155, PubMed:21764853, PubMed:24493646, PubMed:30559249). The SAGA complex predominantly acetylates histone H3 (PubMed:12697829, PubMed:30559249). Required for oogenesis; involved in transcriptional activation (PubMed:34807910)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33004486\",\"source\":\"PubMed\"}],\"id\":\"GO:0045893\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:positive regulation of DNA-templated transcription\"},{\"key\":\"GoEvidenceType\",\"value\":\"NAS:ComplexPortal\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/36",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006366\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:transcription by RNA polymerase II\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/37",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Kusch T.\",\"Guelman S.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12697829\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.23.9.3305-3319.2003\"}],\"citationType\":\"journal article\",\"firstPage\":\"3305\",\"id\":\"12697829\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"3319\",\"publicationDate\":\"2003\",\"title\":\"Two Drosophila Ada2 homologues function in different multiprotein complexes.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAN52143.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"INTERACTION WITH ADA2B; GCN5; ADA3; TAF5; TAF9 AND TAF10\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Guelman S.\",\"Suganuma T.\",\"Florens L.\",\"Weake V.\",\"Swanson S.K.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16980620\"},{\"database\":\"DOI\",\"id\":\"10.1128/mcb.00130-06\"}],\"citationType\":\"journal article\",\"firstPage\":\"7178\",\"id\":\"16980620\",\"journal\":\"Mol. Cell. Biol.\",\"lastPage\":\"7189\",\"publicationDate\":\"2006\",\"title\":\"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA required for histone H3 acetylation.\",\"volume\":\"26\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"INTERACTION WITH GCN5; ADA2B; WDA AND ADA1-2\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Lee K.K.\",\"Guelman S.\",\"Lin C.-H.\",\"Seidel C.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18188155\"},{\"database\":\"DOI\",\"id\":\"10.1038/sj.emboj.7601966\"}],\"citationType\":\"journal article\",\"firstPage\":\"394\",\"id\":\"18188155\",\"journal\":\"EMBO J.\",\"lastPage\":\"405\",\"publicationDate\":\"2008\",\"title\":\"SAGA-mediated H2B deubiquitination controls the development of neuronal connectivity in the Drosophila visual system.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Weake V.M.\",\"Dyer J.O.\",\"Seidel C.\",\"Box A.\",\"Swanson S.K.\",\"Peak A.\",\"Florens L.\",\"Washburn M.P.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21764853\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.2046211\"}],\"citationType\":\"journal article\",\"firstPage\":\"1499\",\"id\":\"21764853\",\"journal\":\"Genes Dev.\",\"lastPage\":\"1509\",\"publicationDate\":\"2011\",\"title\":\"Post-transcription initiation function of the ubiquitous SAGA complex in tissue-specific gene activation.\",\"volume\":\"25\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN SAGA COMPLEX\",\"DEVELOPMENTAL STAGE\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Mohan R.D.\",\"Dialynas G.\",\"Weake V.M.\",\"Liu J.\",\"Martin-Brown S.\",\"Florens L.\",\"Washburn M.P.\",\"Workman J.L.\",\"Abmayr S.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"24493646\"},{\"database\":\"DOI\",\"id\":\"10.1101/gad.225151.113\"}],\"citationType\":\"journal article\",\"firstPage\":\"259\",\"id\":\"24493646\",\"journal\":\"Genes Dev.\",\"lastPage\":\"272\",\"publicationDate\":\"2014\",\"title\":\"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination and leads to neural and retinal degeneration.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"SUBCELLULAR LOCATION\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Torres-Zelada E.F.\",\"Stephenson R.E.\",\"Alpsoy A.\",\"Anderson B.D.\",\"Swanson S.K.\",\"Florens L.\",\"Dykhuizen E.C.\",\"Washburn M.P.\",\"Weake V.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30559249\"},{\"database\":\"DOI\",\"id\":\"10.1242/jcs.214072\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"30559249\",\"journal\":\"J. Cell Sci.\",\"lastPage\":\"0\",\"publicationDate\":\"2019\",\"title\":\"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is necessary for histone acetylation and viability.\",\"volume\":\"132\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":9,\"referencePositions\":[\"FUNCTION\",\"IDENTIFICATION IN THE SAGA COMPLEX\",\"IDENTIFICATION BY MASS SPECTROMETRY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/8",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VGE2.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"citation\":{\"authors\":[\"Soffers J.H.M.\",\"Alcantara S.G.\",\"Li X.\",\"Shao W.\",\"Seidel C.W.\",\"Li H.\",\"Zeitlinger J.\",\"Abmayr S.M.\",\"Workman J.L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34807910\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pgen.1009668\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1009668\",\"id\":\"34807910\",\"journal\":\"PLoS Genet.\",\"lastPage\":\"e1009668\",\"publicationDate\":\"2021\",\"title\":\"The SAGA core module is critical during Drosophila oogenesis and is broadly recruited to promoters.\",\"volume\":\"17\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/9",
  "retrieved_utc": "2026-11-02T04:33:14.962259+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bc04699c59a97ae83e289605afb7b0013b45d65077138d5e88745fdc0b164e8a",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VGE2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H1",
  "excerpt": "ID   SPT3_DROME              Reviewed;         384 AA.\nAC   Q9VGE2; Q8I8U9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 197.\nDE   RecName: Full=SAGA complex subunit Spt3 {ECO:0000305};\nDE   AltName: Full=Suppressor of Ty protein 3 homolog {ECO:0000305};\nGN   Name=Spt3 {ECO:0000312|FlyBase:FBgn0037981};\nGN   ORFNames=CG3169 {ECO:0000312|FlyBase:FBgn0037981};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAN52143.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, INTERACTION WITH ADA2B; GCN5; ADA3;\nRP   TAF5; TAF9 AND TAF10, AND DEVELOPMENTAL STAGE.\nRX   PubMed=12697829; DOI=10.1128/mcb.23.9.3305-3319.2003;\nRA   Kusch T., Guelman S., Abmayr S.M., Workman J.L.;\nRT   \"Two Drosophila Ada2 homologues function in different multiprotein\nRT   complexes.\";\nRL   Mol. Cell. Biol. 23:3305-3319(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, INTERACTION WITH GCN5; ADA2B; WDA\nRP   AND ADA1-2, SUBCELLULAR LOCATION, AND IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=16980620; DOI=10.1128/mcb.00130-06;\nRA   Guelman S., Suganuma T., Florens L., Weake V., Swanson S.K., Washburn M.P.,\nRA   Abmayr S.M., Workman J.L.;\nRT   \"The essential gene wda encodes a WD40 repeat subunit of Drosophila SAGA\nRT   required for histone H3 acetylation.\";\nRL   Mol. Cell. Biol. 26:7178-7189(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H4",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   FUNCTION, AND IDENTIFICATION IN THE SAGA COMPLEX.\nRX   PubMed=18188155; DOI=10.1038/sj.emboj.7601966;\nRA   Weake V.M., Lee K.K., Guelman S., Lin C.-H., Seidel C., Abmayr S.M.,\nRA   Workman J.L.;\nRT   \"SAGA-mediated H2B deubiquitination controls the development of neuronal\nRT   connectivity in the Drosophila visual system.\";\nRL   EMBO J. 27:394-405(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H5",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN SAGA COMPLEX, DEVELOPMENTAL STAGE, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=21764853; DOI=10.1101/gad.2046211;\nRA   Weake V.M., Dyer J.O., Seidel C., Box A., Swanson S.K., Peak A.,\nRA   Florens L., Washburn M.P., Abmayr S.M., Workman J.L.;\nRT   \"Post-transcription initiation function of the ubiquitous SAGA complex in\nRT   tissue-specific gene activation.\";\nRL   Genes Dev. 25:1499-1509(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H6",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, SUBCELLULAR LOCATION, AND\nRP   IDENTIFICATION BY MASS SPECTROMETRY.\nRX   PubMed=24493646; DOI=10.1101/gad.225151.113;\nRA   Mohan R.D., Dialynas G., Weake V.M., Liu J., Martin-Brown S., Florens L.,\nRA   Washburn M.P., Workman J.L., Abmayr S.M.;\nRT   \"Loss of Drosophila Ataxin-7, a SAGA subunit, reduces H2B ubiquitination\nRT   and leads to neural and retinal degeneration.\";\nRL   Genes Dev. 28:259-272(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H7",
  "excerpt": "RN   [9] {ECO:0000305}\nRP   FUNCTION, IDENTIFICATION IN THE SAGA COMPLEX, AND IDENTIFICATION BY MASS\nRP   SPECTROMETRY.\nRX   PubMed=30559249; DOI=10.1242/jcs.214072;\nRA   Torres-Zelada E.F., Stephenson R.E., Alpsoy A., Anderson B.D.,\nRA   Swanson S.K., Florens L., Dykhuizen E.C., Washburn M.P., Weake V.M.;\nRT   \"The Drosophila Dbf4 ortholog Chiffon forms a complex with Gcn5 that is\nRT   necessary for histone acetylation and viability.\";\nRL   J. Cell Sci. 132:0-0(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-124",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H8",
  "excerpt": "RN   [10] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=34807910; DOI=10.1371/journal.pgen.1009668;\nRA   Soffers J.H.M., Alcantara S.G., Li X., Shao W., Seidel C.W., Li H.,\nRA   Zeitlinger J., Abmayr S.M., Workman J.L.;\nRT   \"The SAGA core module is critical during Drosophila oogenesis and is\nRT   broadly recruited to promoters.\";\nRL   PLoS Genet. 17:e1009668-e1009668(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H9",
  "excerpt": "CC   -!- FUNCTION: Component of the transcription regulatory complex SAGA, a\nCC       multiprotein complex that activates transcription by remodeling\nCC       chromatin and mediating histone acetylation and deubiquitination\nCC       (PubMed:12697829, PubMed:16980620, PubMed:18188155, PubMed:21764853,\nCC       PubMed:24493646, PubMed:30559249). The SAGA complex predominantly\nCC       acetylates histone H3 (PubMed:12697829, PubMed:30559249). Required for\nCC       oogenesis; involved in transcriptional activation (PubMed:34807910).\nCC       {ECO:0000269|PubMed:12697829, ECO:0000269|PubMed:16980620,\nCC       ECO:0000269|PubMed:18188155, ECO:0000269|PubMed:21764853,\nCC       ECO:0000269|PubMed:24493646, ECO:0000269|PubMed:30559249,\nCC       ECO:0000269|PubMed:34807910}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197)

```json
{
  "entry_version": 197,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0006366; P:transcription by RNA polymerase II; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:17.561472+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 211-211",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "65437a3a9f732538e2645ee72992d0425f547c558521f4a49cad1001c989dd43",
  "url": "https://rest.uniprot.org/unisave/Q9VGE2?format=txt&versions=197"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0006096\nname: glycolytic process\nnamespace: biological_process\nalt_id: GO:0019641\nalt_id: GO:0019642\ndef: \"The chemical reactions and pathways resulting in the breakdown of a carbohydrate into pyruvate, with the concomitant production of a small amount of ATP and the reduction of NAD(P) to NAD(P)H. Glycolysis begins with the metabolism of a carbohydrate to generate products that can enter the pathway and ends with the production of pyruvate. Pyruvate may be converted to acetyl-coenzyme A, ethanol, lactate, or other small molecules.\" [GOC:bf, GOC:dph, ISBN:0201090910, ISBN:0716720094, ISBN:0879010479, Wikipedia:Glycolysis]\nsynonym: \"anaerobic glycolysis\" RELATED []\nsynonym: \"Embden-Meyerhof pathway\" RELATED []\nsynonym: \"Embden-Meyerhof-Parnas pathway\" RELATED []\nsynonym: \"glycolysis\" RELATED [GOC:dph]\nsynonym: \"modified Embden-Meyerhof pathway\" RELATED []\nxref: MetaCyc:GLYCOLYSIS-VARIANTS\nxref: MetaCyc:P341-PWY\nis_a: GO:0006090 ! pyruvate metabolic process\nis_a: GO:0006091 ! generation of precursor metabolites and energy\nis_a: GO:0016052 ! carbohydrate catabolic process\nis_a: GO:0019364 ! pyridine nucleotide catabolic process\nis_a: GO:0046032 ! ADP catabolic process\nis_a: GO:0046034 ! ATP metabolic process\nis_a: GO:0046496 ! nicotinamide nucleotide metabolic process\nrelationship: part_of GO:0009060 ! aerobic respiration\nproperty_value: skos:exactMatch MetaCyc:GLYCOLYSIS-VARIANTS\nproperty_value: skos:narrowMatch MetaCyc:P341-PWY\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006096",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 62693-62717",
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
  "excerpt": "[Term]\nid: GO:0006366\nname: transcription by RNA polymerase II\nnamespace: biological_process\nalt_id: GO:0032568\nalt_id: GO:0032569\ndef: \"The synthesis of RNA from a DNA template by RNA polymerase II (RNAP II), originating at an RNA polymerase II promoter. Includes transcription of messenger RNA (mRNA) and certain small nuclear RNAs (snRNAs).\" [GOC:jl, GOC:txnOH, ISBN:0321000382]\nsubset: goslim_yeast\nsynonym: \"gene-specific transcription from RNA polymerase II promoter\" RELATED []\nsynonym: \"general transcription from RNA polymerase II promoter\" RELATED []\nsynonym: \"RNA polymerase II transcription factor activity\" RELATED []\nsynonym: \"specific transcription from RNA polymerase II promoter\" RELATED [GOC:mah]\nsynonym: \"transcription from Pol II promoter\" EXACT []\nsynonym: \"transcription from RNA polymerase II promoter\" EXACT []\nxref: Reactome:R-HSA-73857 \"RNA Polymerase II Transcription\"\nis_a: GO:0006351 ! DNA-templated transcription\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006366",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 65522-65538",
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
  "excerpt": "[Term]\nid: GO:0006515\nname: protein quality control for misfolded or incompletely synthesized proteins\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of misfolded or attenuated proteins.\" [GOC:jl]\nsynonym: \"degradation of misfolded or incompletely synthesized proteins\" EXACT []\nsynonym: \"misfolded or incompletely synthesized protein breakdown\" EXACT []\nsynonym: \"misfolded or incompletely synthesized protein catabolic process\" EXACT []\nsynonym: \"misfolded or incompletely synthesized protein catabolism\" EXACT []\nsynonym: \"misfolded or incompletely synthesized protein degradation\" EXACT []\nsynonym: \"protein quality control (PQC)\" EXACT []\nsynonym: \"protein quality control by the ubiquitin-proteasome system\" BROAD []\nis_a: GO:0030163 ! protein catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0006515",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 66954-66967",
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
  "excerpt": "[Term]\nid: GO:0042254\nname: ribosome biogenesis\nnamespace: biological_process\nalt_id: GO:0007046\ndef: \"A cellular process that results in the biosynthesis of constituent macromolecules, assembly, and arrangement of constituent parts of ribosome subunits; includes transport to the sites of protein synthesis.\" [GOC:ma, PMID:26404467, Wikipedia:Ribosome_biogenesis]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_pombe\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsynonym: \"ribosome biogenesis and assembly\" EXACT []\nis_a: GO:0022613 ! ribonucleoprotein complex biogenesis\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042254",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 235673-235689",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 126. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
