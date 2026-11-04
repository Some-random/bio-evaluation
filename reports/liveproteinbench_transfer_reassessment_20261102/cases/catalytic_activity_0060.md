# catalytic_activity_0060

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0060.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA

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
A. FMN + L-glutamine + ATP = 3-amino-1,5-dihydropyridine-2,6-dione + FMNH2 + AMP + diphosphate
B. spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)
D. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence matches the protein in both the historical and current UniProt records. Both records annotate the reaction in D, but the catalytic-activity evidence is transferred by similarity from another UniProt protein, so this supports the key without establishing a direct assay of this exact protein.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as consistent with the soluble enoyl-CoA isomerase/dienoyl-CoA isomerase family, using family-level sequence and fold patterns learned from homologous fatty-acid beta-oxidation enzymes. That family rearranges double bonds in unsaturated fatty-acid CoA intermediates, making D a meaningful fit over the FMN/glutamine reaction, ferredoxin-dependent carotenoid reaction, and lipid-linked glycan transfer reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The alternatives represent substantially different enzyme families and chemistries. Family-level recognition from the sequence can distinguish the CoA-intermediate isomerization reaction without recalling this exact protein's database entry; it need not prove every detail of the annotated reaction independently.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered reaction is comparably consistent with the sequence's inferred CoA-metabolism enzyme family.


### Important caveats

- The supplied annotation evidence supports D by similarity transfer; it is not direct experimental confirmation of this exact protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as consistent with the soluble enoyl-CoA isomerase/dienoyl-CoA isomerase family, using family-level sequence and fold patterns learned from homologous fatty-acid beta-oxidation enzymes. That family rearranges double bonds in unsaturated fatty-acid CoA intermediates, making D a meaningful fit over the FMN/glutamine reaction, ferredoxin-dependent carotenoid reaction, and lipid-linked glycan transfer reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The alternatives represent substantially different enzyme families and chemistries. Family-level recognition from the sequence can distinguish the CoA-intermediate isomerization reaction without recalling this exact protein's database entry; it need not prove every detail of the annotated reaction independently."
  },
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the protein in both the historical and current UniProt records. Both records annotate the reaction in D, but the catalytic-activity evidence is transferred by similarity from another UniProt protein, so this supports the key without establishing a direct assay of this exact protein."
  },
  "important_caveats": [
    "The supplied annotation evidence supports D by similarity transfer; it is not direct experimental confirmation of this exact protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably consistent with the sequence's inferred CoA-metabolism enzyme family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the protein in both the historical and current UniProt records. Both records annotate the reaction in D, but the catalytic-activity evidence is transferred by similarity from another UniProt protein, so this supports the key without establishing a direct assay of this exact protein.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as consistent with the soluble enoyl-CoA isomerase/dienoyl-CoA isomerase family, using family-level sequence and fold patterns learned from homologous fatty-acid beta-oxidation enzymes. That family rearranges double bonds in unsaturated fatty-acid CoA intermediates, making D a meaningful fit over the FMN/glutamine reaction, ferredoxin-dependent carotenoid reaction, and lipid-linked glycan transfer reaction.",
    "missing_item_specific_fact": "",
    "reason": "The alternatives represent substantially different enzyme families and chemistries. Family-level recognition from the sequence can distinguish the CoA-intermediate isomerization reaction without recalling this exact protein's database entry; it need not prove every detail of the annotated reaction independently."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered reaction is comparably consistent with the sequence's inferred CoA-metabolism enzyme family."
  },
  "important_caveats": [
    "The supplied annotation evidence supports D by similarity transfer; it is not direct experimental confirmation of this exact protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NCP4 (DCI1_PYRO7) annotates the catalytic activity as 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' with EC 5.3.3.21, exactly matching option D. The annotation evidence code is ECO:0000250 (similarity to Q08558, yeast DCI1) for the catalytic activity, with the EC number assigned via ECO:0000305 based on PubMed:36774535. The sequence matches the source entry exactly (280 aa, SHA-256 confirmed). While the direct experimental characterization is transferred from the yeast homolog rather than performed on this exact fungal protein, the annotation is well-supported by the database record.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the 'TAKGR' motif within the region 'VYVTLLTAKGRFFSAGADVSTIRDP', which is a well-known signature of the enoyl-CoA hydratase/isomerase superfamily (including crotonase, dienoyl-CoA isomerase, and related enzymes). Among the four choices, only D (dienoyl-CoA isomerase, EC 5.3.3.21) belongs to this superfamily. Option A (FMN-dependent glutamine amidotransferase) would require flavin-binding motifs (e.g., 'GxGxxG' Rossmann fold for FMN) absent here. Option B (spheroidene desaturase/oxygenase) would require a carotenoid oxygenase fold with the conserved 8-His/Fe-binding motif, absent here. Option C (dolichol-linked mannosyltransferase) would require glycosyltransferase motifs (e.g., PSPG box), absent here. The overall ~280-aa length and hydrophobic character are also consistent with peroxisomal fatty-acid-oxidation enzymes of this superfamily. Thus, family-level motif recognition (TAKGR) plus elimination of mechanistically incompatible alternatives distinguishes D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model recognizing the TAKGR motif as diagnostic of the enoyl-CoA hydratase/isomerase superfamily can eliminate A (flavoprotein), B (carotenoid oxygenase), and C (glycosyltransferase) based on the absence of their respective sequence signatures, leaving D as the only option within the recognized family. This is legitimate transfer from knowledge of crotonase, yeast DCI1, and other superfamily members.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes (flavoprotein, carotenoid oxygenase, glycosyltransferase, CoA-thioester isomerase) with distinct sequence signatures. The TAKGR motif in the query sequence uniquely aligns with the enoyl-CoA hydratase/isomerase superfamily, making D the only mechanistically consistent choice.


### Important caveats

- The UniProt annotation for this protein's catalytic activity is based on similarity (ECO:0000250) to yeast DCI1 (Q08558), not on direct in vitro characterization of the Pyricularia enzyme itself.
- The TAKGR motif is shared broadly across the enoyl-CoA hydratase/isomerase superfamily; distinguishing dienoyl-CoA isomerase specifically from, say, crotonase within that superfamily would require finer analysis, but among the four offered choices only D falls in this superfamily.
- The protein is annotated as peroxisomal, consistent with its role in unsaturated fatty acid beta-oxidation, but the peroxisomal targeting signal is not a canonical PTS1 (SKL) at the C-terminus.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the 'TAKGR' motif within the region 'VYVTLLTAKGRFFSAGADVSTIRDP', which is a well-known signature of the enoyl-CoA hydratase/isomerase superfamily (including crotonase, dienoyl-CoA isomerase, and related enzymes). Among the four choices, only D (dienoyl-CoA isomerase, EC 5.3.3.21) belongs to this superfamily. Option A (FMN-dependent glutamine amidotransferase) would require flavin-binding motifs (e.g., 'GxGxxG' Rossmann fold for FMN) absent here. Option B (spheroidene desaturase/oxygenase) would require a carotenoid oxygenase fold with the conserved 8-His/Fe-binding motif, absent here. Option C (dolichol-linked mannosyltransferase) would require glycosyltransferase motifs (e.g., PSPG box), absent here. The overall ~280-aa length and hydrophobic character are also consistent with peroxisomal fatty-acid-oxidation enzymes of this superfamily. Thus, family-level motif recognition (TAKGR) plus elimination of mechanistically incompatible alternatives distinguishes D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the TAKGR motif as diagnostic of the enoyl-CoA hydratase/isomerase superfamily can eliminate A (flavoprotein), B (carotenoid oxygenase), and C (glycosyltransferase) based on the absence of their respective sequence signatures, leaving D as the only option within the recognized family. This is legitimate transfer from knowledge of crotonase, yeast DCI1, and other superfamily members."
  },
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "C1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) annotates the catalytic activity as 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' with EC 5.3.3.21, exactly matching option D. The annotation evidence code is ECO:0000250 (similarity to Q08558, yeast DCI1) for the catalytic activity, with the EC number assigned via ECO:0000305 based on PubMed:36774535. The sequence matches the source entry exactly (280 aa, SHA-256 confirmed). While the direct experimental characterization is transferred from the yeast homolog rather than performed on this exact fungal protein, the annotation is well-supported by the database record."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's catalytic activity is based on similarity (ECO:0000250) to yeast DCI1 (Q08558), not on direct in vitro characterization of the Pyricularia enzyme itself.",
    "The TAKGR motif is shared broadly across the enoyl-CoA hydratase/isomerase superfamily; distinguishing dienoyl-CoA isomerase specifically from, say, crotonase within that superfamily would require finer analysis, but among the four offered choices only D falls in this superfamily.",
    "The protein is annotated as peroxisomal, consistent with its role in unsaturated fatty acid beta-oxidation, but the peroxisomal targeting signal is not a canonical PTS1 (SKL) at the C-terminus."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (flavoprotein, carotenoid oxygenase, glycosyltransferase, CoA-thioester isomerase) with distinct sequence signatures. The TAKGR motif in the query sequence uniquely aligns with the enoyl-CoA hydratase/isomerase superfamily, making D the only mechanistically consistent choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) annotates the catalytic activity as 'a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA' with EC 5.3.3.21, exactly matching option D. The annotation evidence code is ECO:0000250 (similarity to Q08558, yeast DCI1) for the catalytic activity, with the EC number assigned via ECO:0000305 based on PubMed:36774535. The sequence matches the source entry exactly (280 aa, SHA-256 confirmed). While the direct experimental characterization is transferred from the yeast homolog rather than performed on this exact fungal protein, the annotation is well-supported by the database record.",
    "evidence_ids": ["C4", "C5", "H4", "C1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the 'TAKGR' motif within the region 'VYVTLLTAKGRFFSAGADVSTIRDP', which is a well-known signature of the enoyl-CoA hydratase/isomerase superfamily (including crotonase, dienoyl-CoA isomerase, and related enzymes). Among the four choices, only D (dienoyl-CoA isomerase, EC 5.3.3.21) belongs to this superfamily. Option A (FMN-dependent glutamine amidotransferase) would require flavin-binding motifs (e.g., 'GxGxxG' Rossmann fold for FMN) absent here. Option B (spheroidene desaturase/oxygenase) would require a carotenoid oxygenase fold with the conserved 8-His/Fe-binding motif, absent here. Option C (dolichol-linked mannosyltransferase) would require glycosyltransferase motifs (e.g., PSPG box), absent here. The overall ~280-aa length and hydrophobic character are also consistent with peroxisomal fatty-acid-oxidation enzymes of this superfamily. Thus, family-level motif recognition (TAKGR) plus elimination of mechanistically incompatible alternatives distinguishes D.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model recognizing the TAKGR motif as diagnostic of the enoyl-CoA hydratase/isomerase superfamily can eliminate A (flavoprotein), B (carotenoid oxygenase), and C (glycosyltransferase) based on the absence of their respective sequence signatures, leaving D as the only option within the recognized family. This is legitimate transfer from knowledge of crotonase, yeast DCI1, and other superfamily members."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes (flavoprotein, carotenoid oxygenase, glycosyltransferase, CoA-thioester isomerase) with distinct sequence signatures. The TAKGR motif in the query sequence uniquely aligns with the enoyl-CoA hydratase/isomerase superfamily, making D the only mechanistically consistent choice."
  },
  "important_caveats": [
    "The UniProt annotation for this protein's catalytic activity is based on similarity (ECO:0000250) to yeast DCI1 (Q08558), not on direct in vitro characterization of the Pyricularia enzyme itself.",
    "The TAKGR motif is shared broadly across the enoyl-CoA hydratase/isomerase superfamily; distinguishing dienoyl-CoA isomerase specifically from, say, crotonase within that superfamily would require finer analysis, but among the four offered choices only D falls in this superfamily.",
    "The protein is annotated as peroxisomal, consistent with its role in unsaturated fatty acid beta-oxidation, but the peroxisomal targeting signal is not a canonical PTS1 (SKL) at the C-terminus."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
