# EC_number_0177

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0177.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 5.3.3.21

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. 5.3.1.16
B. 3.1.26.3
C. 3.4.21.90
D. 5.3.3.21
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

> The matched-sequence UniProt annotation assigns EC 5.3.3.21 and names the corresponding dienoyl-CoA isomerase activity. The catalytic-activity evidence is transferred from a homolog, so this supports the key as an annotation but is not direct experimental evidence for this exact protein in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact, soluble enzyme sequence whose full-length pattern can be compared with known dienoyl-CoA isomerase homologs; family-level sequence recognition provides a plausible route to EC 5.3.3.21. That enzyme-family inference distinguishes D from the nuclease and protease choices, and from the alternative isomerase class in A. The inference is probabilistic rather than a direct assay.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence-homology/family inference can meaningfully favor the dienoyl-CoA isomerase option without relying on the exact protein's database record. The reviewer-only annotation supports the key but is not needed to make the distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The listed alternatives describe substantially different enzyme activities, and the sequence-family inference favors one option; no second choice is comparably supported.


### Important caveats

- The reviewer-only source records match the supplied sequence, but their catalytic-activity evidence is transferred from a homolog rather than presented as a direct biochemical measurement of this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, soluble enzyme sequence whose full-length pattern can be compared with known dienoyl-CoA isomerase homologs; family-level sequence recognition provides a plausible route to EC 5.3.3.21. That enzyme-family inference distinguishes D from the nuclease and protease choices, and from the alternative isomerase class in A. The inference is probabilistic rather than a direct assay.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-homology/family inference can meaningfully favor the dienoyl-CoA isomerase option without relying on the exact protein's database record. The reviewer-only annotation supports the key but is not needed to make the distinction."
  },
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 5.3.3.21 and names the corresponding dienoyl-CoA isomerase activity. The catalytic-activity evidence is transferred from a homolog, so this supports the key as an annotation but is not direct experimental evidence for this exact protein in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only source records match the supplied sequence, but their catalytic-activity evidence is transferred from a homolog rather than presented as a direct biochemical measurement of this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe substantially different enzyme activities, and the sequence-family inference favors one option; no second choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 5.3.3.21 and names the corresponding dienoyl-CoA isomerase activity. The catalytic-activity evidence is transferred from a homolog, so this supports the key as an annotation but is not direct experimental evidence for this exact protein in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact, soluble enzyme sequence whose full-length pattern can be compared with known dienoyl-CoA isomerase homologs; family-level sequence recognition provides a plausible route to EC 5.3.3.21. That enzyme-family inference distinguishes D from the nuclease and protease choices, and from the alternative isomerase class in A. The inference is probabilistic rather than a direct assay.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence-homology/family inference can meaningfully favor the dienoyl-CoA isomerase option without relying on the exact protein's database record. The reviewer-only annotation supports the key but is not needed to make the distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed alternatives describe substantially different enzyme activities, and the sequence-family inference favors one option; no second choice is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only source records match the supplied sequence, but their catalytic-activity evidence is transferred from a homolog rather than presented as a direct biochemical measurement of this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NCP4 (DCI1_PYRO7) annotates this protein with EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase). The EC number is linked to evidence code ECO:0000305|PubMed:36774535 for the recommended name, while the catalytic activity annotation is transferred by similarity (ECO:0000250) from yeast Q08558. The sequence matches the benchmark input exactly. This is a standard UniProt annotation combining direct evidence for the protein name with similarity-based transfer for the catalytic reaction, which is scientifically reasonable.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 280-aa sequence contains motifs characteristic of the 2-enoyl-CoA hydratase/isomerase superfamily: 'GLNGPVVGL', 'GLSAALVSF', and 'GLVAEGG' patterns are hallmarks of this well-studied superfamily (shared by crotonase, 2-enoyl-CoA hydratases, and dienoyl-CoA isomerases across fungi, plants, and animals). These motifs indicate a CoA-binding enzyme involved in fatty acid beta-oxidation, which immediately eliminates hydrolases B (3.1.26.3, ribonuclease) and C (3.4.21.90, serine protease) since no catalytic triad (GDSGGP-type) or RNase motifs are present. Between the remaining isomerase options, EC 5.3.1.16 (A) belongs to the aldose-ketose interconverting cycloisomerase class with no CoA connection, while EC 5.3.3.21 (D) is specifically a dienoyl-CoA isomerase that transposes C=C bonds in CoA thioesters. The CoA-binding superfamily motifs and the peroxisomal fatty-acid-oxidation context strongly favor D over A. Since D is the only 5.3.3.x option among the choices, family-level recognition of the hydratase/isomerase superfamily motifs suffices to select it.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the 2-enoyl-CoA hydratase/isomerase superfamily motifs (GLNGP, GLSA, GLVA patterns) and their association with CoA thioester substrates in fatty acid oxidation can eliminate the hydrolase options (B, C) and the non-CoA isomerase (A), arriving at D. This relies on well-established, transferable family-level sequence knowledge shared across many homologs, not on recalling this specific protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span distinct enzyme classes (hydrolases vs. isomerases) and within isomerases, distinct subclasses (5.3.1 vs. 5.3.3). The superfamily motifs in the sequence clearly point to a CoA-related isomerase, making D the uniquely defensible choice among the offered alternatives.


### Important caveats

- The catalytic activity EC annotation in UniProt is transferred by similarity (ECO:0000250) from yeast Q08558 rather than derived from direct enzymatic assay on this exact fungal protein; the protein name and biological role are supported by direct evidence (PubMed:36774535).
- The superfamily motifs (GLNGP, GLSA, GLVA) are shared broadly across the 2-enoyl-CoA hydratase/isomerase superfamily, so they confirm the enzyme belongs to this superfamily but do not uniquely specify EC 5.3.3.21 within the superfamily; the elimination of other offered choices is what makes D the correct selection.
- The UniProt entry was first publicly released in June 2025, which is relatively recent; the author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 280-aa sequence contains motifs characteristic of the 2-enoyl-CoA hydratase/isomerase superfamily: 'GLNGPVVGL', 'GLSAALVSF', and 'GLVAEGG' patterns are hallmarks of this well-studied superfamily (shared by crotonase, 2-enoyl-CoA hydratases, and dienoyl-CoA isomerases across fungi, plants, and animals). These motifs indicate a CoA-binding enzyme involved in fatty acid beta-oxidation, which immediately eliminates hydrolases B (3.1.26.3, ribonuclease) and C (3.4.21.90, serine protease) since no catalytic triad (GDSGGP-type) or RNase motifs are present. Between the remaining isomerase options, EC 5.3.1.16 (A) belongs to the aldose-ketose interconverting cycloisomerase class with no CoA connection, while EC 5.3.3.21 (D) is specifically a dienoyl-CoA isomerase that transposes C=C bonds in CoA thioesters. The CoA-binding superfamily motifs and the peroxisomal fatty-acid-oxidation context strongly favor D over A. Since D is the only 5.3.3.x option among the choices, family-level recognition of the hydratase/isomerase superfamily motifs suffices to select it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the 2-enoyl-CoA hydratase/isomerase superfamily motifs (GLNGP, GLSA, GLVA patterns) and their association with CoA thioester substrates in fatty acid oxidation can eliminate the hydrolase options (B, C) and the non-CoA isomerase (A), arriving at D. This relies on well-established, transferable family-level sequence knowledge shared across many homologs, not on recalling this specific protein's database record."
  },
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) annotates this protein with EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase). The EC number is linked to evidence code ECO:0000305|PubMed:36774535 for the recommended name, while the catalytic activity annotation is transferred by similarity (ECO:0000250) from yeast Q08558. The sequence matches the benchmark input exactly. This is a standard UniProt annotation combining direct evidence for the protein name with similarity-based transfer for the catalytic reaction, which is scientifically reasonable."
  },
  "important_caveats": [
    "The catalytic activity EC annotation in UniProt is transferred by similarity (ECO:0000250) from yeast Q08558 rather than derived from direct enzymatic assay on this exact fungal protein; the protein name and biological role are supported by direct evidence (PubMed:36774535).",
    "The superfamily motifs (GLNGP, GLSA, GLVA) are shared broadly across the 2-enoyl-CoA hydratase/isomerase superfamily, so they confirm the enzyme belongs to this superfamily but do not uniquely specify EC 5.3.3.21 within the superfamily; the elimination of other offered choices is what makes D the correct selection.",
    "The UniProt entry was first publicly released in June 2025, which is relatively recent; the author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes (hydrolases vs. isomerases) and within isomerases, distinct subclasses (5.3.1 vs. 5.3.3). The superfamily motifs in the sequence clearly point to a CoA-related isomerase, making D the uniquely defensible choice among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0177",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) annotates this protein with EC 5.3.3.21 (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase). The EC number is linked to evidence code ECO:0000305|PubMed:36774535 for the recommended name, while the catalytic activity annotation is transferred by similarity (ECO:0000250) from yeast Q08558. The sequence matches the benchmark input exactly. This is a standard UniProt annotation combining direct evidence for the protein name with similarity-based transfer for the catalytic reaction, which is scientifically reasonable.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 280-aa sequence contains motifs characteristic of the 2-enoyl-CoA hydratase/isomerase superfamily: 'GLNGPVVGL', 'GLSAALVSF', and 'GLVAEGG' patterns are hallmarks of this well-studied superfamily (shared by crotonase, 2-enoyl-CoA hydratases, and dienoyl-CoA isomerases across fungi, plants, and animals). These motifs indicate a CoA-binding enzyme involved in fatty acid beta-oxidation, which immediately eliminates hydrolases B (3.1.26.3, ribonuclease) and C (3.4.21.90, serine protease) since no catalytic triad (GDSGGP-type) or RNase motifs are present. Between the remaining isomerase options, EC 5.3.1.16 (A) belongs to the aldose-ketose interconverting cycloisomerase class with no CoA connection, while EC 5.3.3.21 (D) is specifically a dienoyl-CoA isomerase that transposes C=C bonds in CoA thioesters. The CoA-binding superfamily motifs and the peroxisomal fatty-acid-oxidation context strongly favor D over A. Since D is the only 5.3.3.x option among the choices, family-level recognition of the hydratase/isomerase superfamily motifs suffices to select it.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the 2-enoyl-CoA hydratase/isomerase superfamily motifs (GLNGP, GLSA, GLVA patterns) and their association with CoA thioester substrates in fatty acid oxidation can eliminate the hydrolase options (B, C) and the non-CoA isomerase (A), arriving at D. This relies on well-established, transferable family-level sequence knowledge shared across many homologs, not on recalling this specific protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span distinct enzyme classes (hydrolases vs. isomerases) and within isomerases, distinct subclasses (5.3.1 vs. 5.3.3). The superfamily motifs in the sequence clearly point to a CoA-related isomerase, making D the uniquely defensible choice among the offered alternatives."
  },
  "important_caveats": [
    "The catalytic activity EC annotation in UniProt is transferred by similarity (ECO:0000250) from yeast Q08558 rather than derived from direct enzymatic assay on this exact fungal protein; the protein name and biological role are supported by direct evidence (PubMed:36774535).",
    "The superfamily motifs (GLNGP, GLSA, GLVA) are shared broadly across the 2-enoyl-CoA hydratase/isomerase superfamily, so they confirm the enzyme belongs to this superfamily but do not uniquely specify EC 5.3.3.21 within the superfamily; the elimination of other offered choices is what makes D the correct selection.",
    "The UniProt entry was first publicly released in June 2025, which is relatively recent; the author's source snapshot is unknown."
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
  "benchmark_sequence_length": 280,
  "benchmark_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "current_entry_audit": {
    "entryVersion": 51,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 280,
  "current_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
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
  "requested_accession": "G4NCP4",
  "selected_historical_entry_version": 50,
  "selected_historical_record_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "selected_historical_source_sequence_length": 280,
  "selected_historical_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "selected_historical_version": {
    "accession": "G4NCP4",
    "database": "Swiss-Prot",
    "entryVersion": 50,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "DCI1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4NCP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":51,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"value\":\"Peroxisomal di-isomerase DCI1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"5.3.3.21\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:45241\"}}],\"reaction\":{\"ecNumber\":\"5.3.3.21\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"name\":\"a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:45240\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85110\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:85111\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang T.\",\"Wang X.\",\"Li X.\",\"Li Y.N.\",\"Li Y.\",\"Wu S.\",\"Xu L.\",\"Zhou R.\",\"Yang J.\",\"Li G.\",\"Liu X.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36774535\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.xplc.2023.100561\"}],\"citationType\":\"journal article\",\"firstPage\":\"100561\",\"id\":\"36774535\",\"journal\":\"Plant Commun.\",\"lastPage\":\"100561\",\"publicationDate\":\"2023\",\"title\":\"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to facilitate fatty acid oxidation for infectious growth of the rice blast fungus.\",\"volume\":\"4\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H1",
  "excerpt": "ID   DCI1_PYRO7              Reviewed;         280 AA.\nAC   G4NCP4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 50.\nDE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};\nDE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};\nDE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};\nGN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};\nDE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};\nDE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=36774535; DOI=10.1016/j.xplc.2023.100561;\nRA   Zhang T., Wang X., Li X., Li Y.N., Li Y., Wu S., Xu L., Zhou R., Yang J.,\nRA   Li G., Liu X., Zheng X., Zhang Z., Zhang H.;\nRT   \"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to\nRT   facilitate fatty acid oxidation for infectious growth of the rice blast\nRT   fungus.\";\nRL   Plant Commun. 4:100561-100561(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA;\nCC         Xref=Rhea:RHEA:45240, ChEBI:CHEBI:85110, ChEBI:CHEBI:85111;\nCC         EC=5.3.3.21; Evidence={ECO:0000250|UniProtKB:Q08558};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:45241;\nCC         Evidence={ECO:0000250|UniProtKB:Q08558};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 177. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
