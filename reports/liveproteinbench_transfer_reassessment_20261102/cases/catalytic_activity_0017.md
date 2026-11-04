# catalytic_activity_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0017.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL

[Multiple Choices]
A. norajmaline + S-adenosyl-L-methionine = ajmaline + S-adenosyl-L-homocysteine + H(+)
B. D-ribose 5-phosphate + uracil = psi-UMP + H2O
C. 3,5-dioxohexanoate + acetyl-CoA = acetoacetyl-CoA + acetoacetate
D. beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)
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

> The matched sequence is annotated with the reaction in option D. The annotation cites both computational evidence and experimental evidence codes, including PubMed-linked evidence; this supports the key while not implying that every source was independently re-evaluated here.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence’s catalytic core, including glycine- and polar-residue-rich regions such as VVGGIISPTHD and VITRAGSNPGK, is compatible with the NMNAT/nicotinamide-nucleotide adenylyltransferase family. Transferable family knowledge predicts ATP-dependent conversion of nicotinamide mononucleotide to NAD, matching D. The other options describe distinct alkaloid methylation, uracil salvage, and acetoacetate-related chemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the characteristic NMNAT reaction meaningfully distinguish D among these alternatives without needing the exact protein’s database entry. This is a credible inference, not a guarantee from the sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D matches the expected NMNAT family chemistry among the offered reactions.


### Important caveats

- The sequence-family inference is not an independent experimental demonstration of this exact protein’s activity.
- Reviewer evidence confirms a sequence match to the cited record; its annotations include both computational and experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence’s catalytic core, including glycine- and polar-residue-rich regions such as VVGGIISPTHD and VITRAGSNPGK, is compatible with the NMNAT/nicotinamide-nucleotide adenylyltransferase family. Transferable family knowledge predicts ATP-dependent conversion of nicotinamide mononucleotide to NAD, matching D. The other options describe distinct alkaloid methylation, uracil salvage, and acetoacetate-related chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the characteristic NMNAT reaction meaningfully distinguish D among these alternatives without needing the exact protein’s database entry. This is a credible inference, not a guarantee from the sequence alone."
  },
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in option D. The annotation cites both computational evidence and experimental evidence codes, including PubMed-linked evidence; this supports the key while not implying that every source was independently re-evaluated here."
  },
  "important_caveats": [
    "The sequence-family inference is not an independent experimental demonstration of this exact protein’s activity.",
    "Reviewer evidence confirms a sequence match to the cited record; its annotations include both computational and experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the expected NMNAT family chemistry among the offered reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated with the reaction in option D. The annotation cites both computational evidence and experimental evidence codes, including PubMed-linked evidence; this supports the key while not implying that every source was independently re-evaluated here.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence’s catalytic core, including glycine- and polar-residue-rich regions such as VVGGIISPTHD and VITRAGSNPGK, is compatible with the NMNAT/nicotinamide-nucleotide adenylyltransferase family. Transferable family knowledge predicts ATP-dependent conversion of nicotinamide mononucleotide to NAD, matching D. The other options describe distinct alkaloid methylation, uracil salvage, and acetoacetate-related chemistry.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the characteristic NMNAT reaction meaningfully distinguish D among these alternatives without needing the exact protein’s database entry. This is a credible inference, not a guarantee from the sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D matches the expected NMNAT family chemistry among the offered reactions."
  },
  "important_caveats": [
    "The sequence-family inference is not an independent experimental demonstration of this exact protein’s activity.",
    "Reviewer evidence confirms a sequence match to the cited record; its annotations include both computational and experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VC03 (NMNA_DROME) for the exact 389-aa sequence annotates the protein as Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1) with the catalytic reaction 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)'. This annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the reaction experimentally. The sequence match is exact (SHA-256 identical).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a highly diagnostic 'GGGGG' motif (INSGGGGGDDGENTHLPG, around residues 128-134), which is a well-known family-level signature of NMNAT (nicotinamide mononucleotide adenylyltransferase) enzymes across eukaryotes. NMNAT proteins are nucleotidyltransferases (EC 2.7.7.x) that transfer an adenylyl group from ATP to NMN, releasing diphosphate (PPi) and forming NAD+. The protein length (~389 aa) is consistent with the NMNAT family. Among the four choices: (A) is a SAM-dependent methyltransferase (EC 2.1.x) requiring a VLDLGCG-type SAM-binding motif absent here; (B) is a pyrophosphorylase for pseudouridine synthesis, mechanistically unrelated; (C) is a thiolase (EC 2.3.x) involving CoA chemistry; (D) matches the nucleotidyltransferase mechanism (ATP→PPi) and the NMNAT substrate/product pair. The GGGGG motif, the overall length, and the nucleotidyltransferase chemistry visible in choice D collectively allow a knowledgeable model to distinguish D from the other three options using family-level transfer from human/yeast NMNAT homologs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGGGG motif is a recognized NMNAT family signature transferable from well-studied homologs (human NMNAT1-3, yeast Nma1/2). Combined with the protein length and the mechanistic logic of the choices (nucleotidyltransferase vs. methyltransferase vs. thiolase vs. pyrophosphorylase), a model with general protein-family knowledge can meaningfully discriminate D without needing to recall the specific Drosophila NMNAT record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct enzyme classes (methyltransferase, pyrophosphorylase, thiolase, nucleotidyltransferase). The GGGGG motif and family-level features point specifically to NMNAT/nucleotidyltransferase chemistry (choice D). No other option is defensible given the sequence features.


### Important caveats

- The GGGGG motif, while strongly associated with NMNAT, is not absolutely exclusive to this family; however, in the context of the four mechanistically distinct choices, it provides sufficient discrimination.
- The UniProt annotation includes both EC 2.7.7.1 (NMNAT) and EC 2.7.7.18 (NaMNAT), but choice D corresponds to the primary NMNAT reaction (EC 2.7.7.1), which is the experimentally confirmed main activity.
- The reviewer-only evidence confirms experimental validation of the catalytic activity via three independent publications, strengthening the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a highly diagnostic 'GGGGG' motif (INSGGGGGDDGENTHLPG, around residues 128-134), which is a well-known family-level signature of NMNAT (nicotinamide mononucleotide adenylyltransferase) enzymes across eukaryotes. NMNAT proteins are nucleotidyltransferases (EC 2.7.7.x) that transfer an adenylyl group from ATP to NMN, releasing diphosphate (PPi) and forming NAD+. The protein length (~389 aa) is consistent with the NMNAT family. Among the four choices: (A) is a SAM-dependent methyltransferase (EC 2.1.x) requiring a VLDLGCG-type SAM-binding motif absent here; (B) is a pyrophosphorylase for pseudouridine synthesis, mechanistically unrelated; (C) is a thiolase (EC 2.3.x) involving CoA chemistry; (D) matches the nucleotidyltransferase mechanism (ATP→PPi) and the NMNAT substrate/product pair. The GGGGG motif, the overall length, and the nucleotidyltransferase chemistry visible in choice D collectively allow a knowledgeable model to distinguish D from the other three options using family-level transfer from human/yeast NMNAT homologs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGGGG motif is a recognized NMNAT family signature transferable from well-studied homologs (human NMNAT1-3, yeast Nma1/2). Combined with the protein length and the mechanistic logic of the choices (nucleotidyltransferase vs. methyltransferase vs. thiolase vs. pyrophosphorylase), a model with general protein-family knowledge can meaningfully discriminate D without needing to recall the specific Drosophila NMNAT record."
  },
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "C9",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) for the exact 389-aa sequence annotates the protein as Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1) with the catalytic reaction 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)'. This annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the reaction experimentally. The sequence match is exact (SHA-256 identical)."
  },
  "important_caveats": [
    "The GGGGG motif, while strongly associated with NMNAT, is not absolutely exclusive to this family; however, in the context of the four mechanistically distinct choices, it provides sufficient discrimination.",
    "The UniProt annotation includes both EC 2.7.7.1 (NMNAT) and EC 2.7.7.18 (NaMNAT), but choice D corresponds to the primary NMNAT reaction (EC 2.7.7.1), which is the experimentally confirmed main activity.",
    "The reviewer-only evidence confirms experimental validation of the catalytic activity via three independent publications, strengthening the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, pyrophosphorylase, thiolase, nucleotidyltransferase). The GGGGG motif and family-level features point specifically to NMNAT/nucleotidyltransferase chemistry (choice D). No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VC03 (NMNA_DROME) for the exact 389-aa sequence annotates the protein as Nicotinamide-nucleotide adenylyltransferase (EC 2.7.7.1) with the catalytic reaction 'beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)'. This annotation is supported by multiple experimental evidence codes (ECO:0000269 from PubMed 17132048, 19403820, 26616331) confirming the reaction experimentally. The sequence match is exact (SHA-256 identical).",
    "evidence_ids": ["C4", "C5", "C7", "C8", "C9", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a highly diagnostic 'GGGGG' motif (INSGGGGGDDGENTHLPG, around residues 128-134), which is a well-known family-level signature of NMNAT (nicotinamide mononucleotide adenylyltransferase) enzymes across eukaryotes. NMNAT proteins are nucleotidyltransferases (EC 2.7.7.x) that transfer an adenylyl group from ATP to NMN, releasing diphosphate (PPi) and forming NAD+. The protein length (~389 aa) is consistent with the NMNAT family. Among the four choices: (A) is a SAM-dependent methyltransferase (EC 2.1.x) requiring a VLDLGCG-type SAM-binding motif absent here; (B) is a pyrophosphorylase for pseudouridine synthesis, mechanistically unrelated; (C) is a thiolase (EC 2.3.x) involving CoA chemistry; (D) matches the nucleotidyltransferase mechanism (ATP→PPi) and the NMNAT substrate/product pair. The GGGGG motif, the overall length, and the nucleotidyltransferase chemistry visible in choice D collectively allow a knowledgeable model to distinguish D from the other three options using family-level transfer from human/yeast NMNAT homologs.",
    "missing_item_specific_fact": "",
    "reason": "The GGGGG motif is a recognized NMNAT family signature transferable from well-studied homologs (human NMNAT1-3, yeast Nma1/2). Combined with the protein length and the mechanistic logic of the choices (nucleotidyltransferase vs. methyltransferase vs. thiolase vs. pyrophosphorylase), a model with general protein-family knowledge can meaningfully discriminate D without needing to recall the specific Drosophila NMNAT record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct enzyme classes (methyltransferase, pyrophosphorylase, thiolase, nucleotidyltransferase). The GGGGG motif and family-level features point specifically to NMNAT/nucleotidyltransferase chemistry (choice D). No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The GGGGG motif, while strongly associated with NMNAT, is not absolutely exclusive to this family; however, in the context of the four mechanistically distinct choices, it provides sufficient discrimination.",
    "The UniProt annotation includes both EC 2.7.7.1 (NMNAT) and EC 2.7.7.18 (NaMNAT), but choice D corresponds to the primary NMNAT reaction (EC 2.7.7.1), which is the experimentally confirmed main activity.",
    "The reviewer-only evidence confirms experimental validation of the catalytic activity via three independent publications, strengthening the key."
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
  "benchmark_sequence_length": 389,
  "benchmark_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_entry_audit": {
    "entryVersion": 189,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 4
  },
  "current_record_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 389,
  "current_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 187,
      "exact_sequence_comparison": "matched",
      "sequence_version": 4
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VC03",
  "selected_historical_entry_version": 187,
  "selected_historical_record_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "selected_historical_source_sequence_length": 389,
  "selected_historical_source_sequence_sha256": "2efa1c2bc1a66f4b43ee288abe72b63c899666ed652a586405e1f75a160908c9",
  "selected_historical_version": {
    "accession": "Q9VC03",
    "database": "Swiss-Prot",
    "entryVersion": 187,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMNA_DROME",
    "sequenceVersion": 4
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VC03\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":189,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":4}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"Nicotinamide mononucleotide adenylyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039254\",\"source\":\"FlyBase\"}],\"value\":\"dNmnat\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"2.7.7.18\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"value\":\"Nicotinamide-nucleotide adenylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:21361\"}}],\"reaction\":{\"ecNumber\":\"2.7.7.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"17132048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19403820\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26616331\",\"source\":\"PubMed\"}],\"name\":\"beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate + NAD(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:21360\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:14649\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.7.18\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"RU362021\",\"source\":\"RuleBase\"}],\"name\":\"nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22860\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57502\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58437\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhai R.G.\",\"Cao Y.\",\"Hiesinger P.R.\",\"Zhou Y.\",\"Mehta S.Q.\",\"Schulze K.L.\",\"Verstreken P.\",\"Bellen H.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17132048\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pbio.0040416\"}],\"citationType\":\"journal article\",\"firstPage\":\"e416\",\"id\":\"17132048\",\"journal\":\"PLoS Biol.\",\"lastPage\":\"e416\",\"publicationDate\":\"2006\",\"title\":\"Drosophila NMNAT maintains neural integrity independent of its NAD synthesis activity.\",\"volume\":\"4\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasaki Y.\",\"Vohra B.P.\",\"Lund F.E.\",\"Milbrandt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19403820\"},{\"database\":\"DOI\",\"id\":\"10.1523/jneurosci.5469-08.2009\"}],\"citationType\":\"journal article\",\"firstPage\":\"5525\",\"id\":\"19403820\",\"journal\":\"J. Neurosci.\",\"lastPage\":\"5535\",\"publicationDate\":\"2009\",\"title\":\"Nicotinamide mononucleotide adenylyl transferase-mediated axonal protection requires enzymatic activity but not increased levels of neuronal nicotinamide adenine dinucleotide.\",\"volume\":\"29\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":7,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VC03.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Ruan K.\",\"Zhu Y.\",\"Li C.\",\"Brazill J.M.\",\"Zhai R.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26616331\"},{\"database\":\"DOI\",\"id\":\"10.1038/ncomms10057\"}],\"citationType\":\"journal article\",\"firstPage\":\"10057\",\"id\":\"26616331\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"10057\",\"publicationDate\":\"2015\",\"title\":\"Alternative splicing of Drosophila Nmnat functions as a switch to enhance neuroprotection under stress.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":10,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"ALTERNATIVE SPLICING\",\"INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS\",\"NUCLEAR LOCALIZATION SIGNAL\",\"MUTAGENESIS OF LYS-380\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/9",
  "retrieved_utc": "2026-11-02T04:33:14.289195+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d978581da8c66968e83a443420aa4c96e4f84a192e306c71ec35e48fbca8bc0d",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VC03.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H1",
  "excerpt": "ID   NMNA_DROME              Reviewed;         389 AA.\nAC   Q9VC03; A0A0B4KHH7; Q7KS06; Q8T405;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 4.\nDT   28-JAN-2026, entry version 187.\nDE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\nGN   Name=Nmnat {ECO:0000303|PubMed:17132048, ECO:0000312|FlyBase:FBgn0039254};\nGN   ORFNames=CG13645 {ECO:0000312|FlyBase:FBgn0039254};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Nicotinamide-nucleotide adenylyltransferase {ECO:0000255|RuleBase:RU362021};\nDE            EC=2.7.7.1 {ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048, ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nDE            EC=2.7.7.18 {ECO:0000255|RuleBase:RU362021};\nDE   AltName: Full=Nicotinamide mononucleotide adenylyltransferase {ECO:0000312|FlyBase:FBgn0039254};\nDE            Short=dNmnat {ECO:0000312|FlyBase:FBgn0039254};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H3",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   DISRUPTION PHENOTYPE, AND MUTAGENESIS OF HIS-61; TRP-129 AND ARG-255.\nRX   PubMed=17132048; DOI=10.1371/journal.pbio.0040416;\nRA   Zhai R.G., Cao Y., Hiesinger P.R., Zhou Y., Mehta S.Q., Schulze K.L.,\nRA   Verstreken P., Bellen H.J.;\nRT   \"Drosophila NMNAT maintains neural integrity independent of its NAD\nRT   synthesis activity.\";\nRL   PLoS Biol. 4:e416-e416(2006).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H4",
  "excerpt": "RN   [7] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, AND SUBCELLULAR LOCATION.\nRX   PubMed=19403820; DOI=10.1523/jneurosci.5469-08.2009;\nRA   Sasaki Y., Vohra B.P., Lund F.E., Milbrandt J.;\nRT   \"Nicotinamide mononucleotide adenylyl transferase-mediated axonal\nRT   protection requires enzymatic activity but not increased levels of neuronal\nRT   nicotinamide adenine dinucleotide.\";\nRL   J. Neurosci. 29:5525-5535(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H5",
  "excerpt": "RN   [10] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, ALTERNATIVE SPLICING,\nRP   INDUCTION BY HEAT SHOCK AND PROTEOTOXIC STRESS, NUCLEAR LOCALISAION SIGNAL,\nRP   AND MUTAGENESIS OF LYS-380.\nRX   PubMed=26616331; DOI=10.1038/ncomms10057;\nRA   Ruan K., Zhu Y., Li C., Brazill J.M., Zhai R.G.;\nRT   \"Alternative splicing of Drosophila Nmnat functions as a switch to enhance\nRT   neuroprotection under stress.\";\nRL   Nat. Commun. 6:10057-10057(2015).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 125-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=beta-nicotinamide D-ribonucleotide + ATP + H(+) = diphosphate\nCC         + NAD(+); Xref=Rhea:RHEA:21360, ChEBI:CHEBI:14649, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57540; EC=2.7.7.1;\nCC         Evidence={ECO:0000255|RuleBase:RU362021, ECO:0000269|PubMed:17132048,\nCC         ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:21361;\nCC         Evidence={ECO:0000269|PubMed:19403820, ECO:0000269|PubMed:26616331};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187)

```json
{
  "entry_version": 187,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+)\nCC         + diphosphate; Xref=Rhea:RHEA:22860, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:33019, ChEBI:CHEBI:57502,\nCC         ChEBI:CHEBI:58437; EC=2.7.7.18;\nCC         Evidence={ECO:0000255|RuleBase:RU362021};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:19.400018+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 4,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6ad887d1c4ec6196ee0ca40854a590e26d7f3512e90bc2ef9725f7251181e6eb",
  "url": "https://rest.uniprot.org/unisave/Q9VC03?format=txt&versions=187"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
