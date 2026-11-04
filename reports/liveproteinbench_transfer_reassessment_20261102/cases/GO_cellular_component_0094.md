# GO_cellular_component_0094

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0094.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MARLSSIVFIICLLLCNNAISDEVIESPSSGGTLSGGGSGTDTVTGTQDGKGKSEGKGNEGGQTDQKGKENPENGQNSDSTGDSSLGSTGSNGSQPAPTTPKEPEPTTPKEPESATPKASEPVTPQKTAETASGKQVSPTPSENPPSKDTPKPESSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPPQVNNITDMESYLMKNYDGVKVIGLCGVYFRVQFSPHLLLYGLTTFSIIQIEPFFEGVRIDFEHQHPIRNKCAPGKAFAFISYVKDNILILKWKVFAPPSDLFANDEVSKQILSAVSVTSDAESSVVDVRKYRLPQLDRPFTSIQVYKANPKQGLLETKNYILKNAIPEKCSKISMNCFLNGNVNIENCFKCTLLVQNAKPTDECFQYLPSDMKNNLNEIKVTAQSDEDSKENDLIESIEILLNSFYKADKKAKKLSLITMDDFDDVLRAELFNYCKLLKELDTKKTLENAELGNEIDIFNNLLRLLKTNEEESKHNLYKKLRNTAICLKDVNKWAEKKRGLILPEEVTQDQMAIGQNEEPYDEDPDDRVDLLELFDDNQNENIVDKDGIIDMSIAIKYAKLKSPYFNSSKYCNYEYCDRWQDKTSCISNIDVEEQGNCSLCWLFASKLHLETIRCMRGYGHNRSSALYVANCSKRTAEEICNDGSNPLEFLKILEKNKFLPLESNYPYLWKNVSGKCPNPQNDWTNLWGNTKLLYNNMFGQFIKHRGYIVYSSRFFAKNMNVFIDIIKREIRNKGSVIAYIKTQGVIDYDFNGRYISNICGHNHPDHAVNIIGYGNYISESGEKRSYWLIRNSWGYYWGHEGNFKVDVLGPDNCVHNVIHTAIVFKIDMEPDSDSNNNNAIKNRDQLIDEDNKSYFPQLSSNFYHSLYYNNYEGYEAKNDDENDQNYGNLDVSGQSENHQNDPKNPQPQANSTVTQLGVCPAENQRTADSNPNAQSTPSPNTTVTDTVNSNTANSNTANSNTASANAASIEKKIQILHVLKHIEKYKMTRGFVKYDNLNDTKNDYTCARSYSYDPKNHNECKQFCEENWERCKNHYSPGYCLTTLSGKNKCLFCYV

[Multiple Choices]
A. peptidoglycan-based cell wall
B. plasma membrane
C. perinuclear region of cytoplasm
D. kinetoplast
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

> The exact-sequence-matched record annotates plasma membrane, and also describes cell-membrane localization transferred from a homolog. This supports B, though the GO annotation is computational and the membrane evidence is homolog-based rather than direct experimental localization for this protein.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a clear hydrophobic signal-peptide-like segment, consistent with entry into the secretory pathway. Among the offered choices, plasma membrane is a plausible destination for such a eukaryotic secretory protein; peptidoglycan-based walls and kinetoplasts are poor fits, and the sequence offers no obvious basis for perinuclear localization. This is a probabilistic inference, not proof of plasma-membrane residence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about signal peptides and eukaryotic secretory trafficking provides a meaningful basis for preferring B among these choices. The sequence does not show an obvious later transmembrane anchor, so the inference is limited and does not establish membrane association over secretion to another compartment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence could also be consistent with secretion to locations not offered, but among the listed options there is no comparably supported alternative to plasma membrane.


### Important caveats

- The source record also lists parasitophorous-vacuole and secreted localizations, which are not answer choices.
- The membrane-localization evidence is transferred from a homolog; the GO plasma-membrane annotation is IEA, not direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like segment, consistent with entry into the secretory pathway. Among the offered choices, plasma membrane is a plausible destination for such a eukaryotic secretory protein; peptidoglycan-based walls and kinetoplasts are poor fits, and the sequence offers no obvious basis for perinuclear localization. This is a probabilistic inference, not proof of plasma-membrane residence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about signal peptides and eukaryotic secretory trafficking provides a meaningful basis for preferring B among these choices. The sequence does not show an obvious later transmembrane anchor, so the inference is limited and does not establish membrane association over secretion to another compartment."
  },
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact-sequence-matched record annotates plasma membrane, and also describes cell-membrane localization transferred from a homolog. This supports B, though the GO annotation is computational and the membrane evidence is homolog-based rather than direct experimental localization for this protein."
  },
  "important_caveats": [
    "The source record also lists parasitophorous-vacuole and secreted localizations, which are not answer choices.",
    "The membrane-localization evidence is transferred from a homolog; the GO plasma-membrane annotation is IEA, not direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence could also be consistent with secretion to locations not offered, but among the listed options there is no comparably supported alternative to plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-sequence-matched record annotates plasma membrane, and also describes cell-membrane localization transferred from a homolog. This supports B, though the GO annotation is computational and the membrane evidence is homolog-based rather than direct experimental localization for this protein.",
    "evidence_ids": ["C5", "C8", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a clear hydrophobic signal-peptide-like segment, consistent with entry into the secretory pathway. Among the offered choices, plasma membrane is a plausible destination for such a eukaryotic secretory protein; peptidoglycan-based walls and kinetoplasts are poor fits, and the sequence offers no obvious basis for perinuclear localization. This is a probabilistic inference, not proof of plasma-membrane residence.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about signal peptides and eukaryotic secretory trafficking provides a meaningful basis for preferring B among these choices. The sequence does not show an obvious later transmembrane anchor, so the inference is limited and does not establish membrane association over secretion to another compartment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence could also be consistent with secretion to locations not offered, but among the listed options there is no comparably supported alternative to plasma membrane."
  },
  "important_caveats": [
    "The source record also lists parasitophorous-vacuole and secreted localizations, which are not answer choices.",
    "The membrane-localization evidence is transferred from a homolog; the GO plasma-membrane annotation is IEA, not direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A509AC44) lists 'Cell membrane' (peripheral membrane protein) as the first subcellular location, and GO:0005886 (plasma membrane) is annotated via IEA:UniProtKB-SubCell. However, the membrane annotation carries evidence code ECO:0000250 (similarity to Q9TY95, SERA5 from P. falciparum), while the only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm.' The protein is also annotated as 'Secreted' and in the 'Parasitophorous vacuole.' The plasma membrane annotation is present in the database but is computational/similarity-based rather than experimentally verified for this specific protein. The expected answer is supported by the recorded annotation, though with a caveat about evidence quality.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MARLSSIVFIICLLLCNNA' is a classic hydrophobic signal peptide (16+ hydrophobic residues followed by a small-residue cleavage region), indicating the protein is a secreted/membrane-associated precursor. The extensive serine-rich repeats in the middle region ('GTQDGKGKSEGKGNEGG...SSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPP...') are a hallmark of the SERA (Serine Repeat Antigen) protein family in Plasmodium, which are known from P. falciparum homologs (SERA5, SERA6) to be secreted and associate with membranes (parasitophorous vacuole membrane, host cell membrane). This eliminates C (perinuclear cytoplasm — no NLS, no nuclear retention features, signal peptide directs secretion) and D (kinetoplast — Plasmodium is an Apicomplexan, not a Kinetoplastid; kinetoplasts exist only in Trypanosoma/Leishmania). Option A (peptidoglycan cell wall) is eliminated because Plasmodium is a eukaryotic parasite with no peptidoglycan. Among the remaining options, a secreted, membrane-associated protein with a signal peptide and no transmembrane anchor (peripheral membrane protein) best matches 'plasma membrane' (B).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use: (1) the visible hydrophobic N-terminal signal peptide to infer secretion/membrane association; (2) serine-rich repeat pattern to recognize the SERA family; (3) knowledge that SERA homologs (SERA5, SERA6 in P. falciparum) are secreted and membrane-associated; (4) basic taxonomy knowledge that Apicomplexa lack peptidoglycan and kinetoplasts. These transferable features meaningfully distinguish B from A, C, and D without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the UniProt entry annotates multiple locations (cell membrane, parasitophorous vacuole, secreted, host cytoplasm), among the four offered choices only B (plasma membrane) is compatible with the sequence features (signal peptide, SERA family, eukaryotic organism). Options A, C, and D are effectively excluded by basic biological reasoning. No ambiguity among the offered alternatives.


### Important caveats

- The plasma membrane annotation in UniProt is based on similarity (ECO:0000250) to Q9TY95 (P. falciparum SERA5), not on direct experimental evidence for PbSERA3.
- The only experimental evidence (PubMed:18419771) supports 'Host cytoplasm' localization, which is not among the offered choices.
- The protein is annotated as a 'Precursor' and 'Secreted,' meaning its mature form may reside in the parasitophorous vacuole or host cytoplasm rather than the parasite's own plasma membrane.
- The GO:0005886 annotation is IEA (inferred from electronic annotation), not an independent experimental or manual curation assignment.
- The reviewer-only accession identification was derived from dataset metadata not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MARLSSIVFIICLLLCNNA' is a classic hydrophobic signal peptide (16+ hydrophobic residues followed by a small-residue cleavage region), indicating the protein is a secreted/membrane-associated precursor. The extensive serine-rich repeats in the middle region ('GTQDGKGKSEGKGNEGG...SSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPP...') are a hallmark of the SERA (Serine Repeat Antigen) protein family in Plasmodium, which are known from P. falciparum homologs (SERA5, SERA6) to be secreted and associate with membranes (parasitophorous vacuole membrane, host cell membrane). This eliminates C (perinuclear cytoplasm — no NLS, no nuclear retention features, signal peptide directs secretion) and D (kinetoplast — Plasmodium is an Apicomplexan, not a Kinetoplastid; kinetoplasts exist only in Trypanosoma/Leishmania). Option A (peptidoglycan cell wall) is eliminated because Plasmodium is a eukaryotic parasite with no peptidoglycan. Among the remaining options, a secreted, membrane-associated protein with a signal peptide and no transmembrane anchor (peripheral membrane protein) best matches 'plasma membrane' (B).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (1) the visible hydrophobic N-terminal signal peptide to infer secretion/membrane association; (2) serine-rich repeat pattern to recognize the SERA family; (3) knowledge that SERA homologs (SERA5, SERA6 in P. falciparum) are secreted and membrane-associated; (4) basic taxonomy knowledge that Apicomplexa lack peptidoglycan and kinetoplasts. These transferable features meaningfully distinguish B from A, C, and D without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A509AC44) lists 'Cell membrane' (peripheral membrane protein) as the first subcellular location, and GO:0005886 (plasma membrane) is annotated via IEA:UniProtKB-SubCell. However, the membrane annotation carries evidence code ECO:0000250 (similarity to Q9TY95, SERA5 from P. falciparum), while the only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm.' The protein is also annotated as 'Secreted' and in the 'Parasitophorous vacuole.' The plasma membrane annotation is present in the database but is computational/similarity-based rather than experimentally verified for this specific protein. The expected answer is supported by the recorded annotation, though with a caveat about evidence quality."
  },
  "important_caveats": [
    "The plasma membrane annotation in UniProt is based on similarity (ECO:0000250) to Q9TY95 (P. falciparum SERA5), not on direct experimental evidence for PbSERA3.",
    "The only experimental evidence (PubMed:18419771) supports 'Host cytoplasm' localization, which is not among the offered choices.",
    "The protein is annotated as a 'Precursor' and 'Secreted,' meaning its mature form may reside in the parasitophorous vacuole or host cytoplasm rather than the parasite's own plasma membrane.",
    "The GO:0005886 annotation is IEA (inferred from electronic annotation), not an independent experimental or manual curation assignment.",
    "The reviewer-only accession identification was derived from dataset metadata not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the UniProt entry annotates multiple locations (cell membrane, parasitophorous vacuole, secreted, host cytoplasm), among the four offered choices only B (plasma membrane) is compatible with the sequence features (signal peptide, SERA family, eukaryotic organism). Options A, C, and D are effectively excluded by basic biological reasoning. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A509AC44) lists 'Cell membrane' (peripheral membrane protein) as the first subcellular location, and GO:0005886 (plasma membrane) is annotated via IEA:UniProtKB-SubCell. However, the membrane annotation carries evidence code ECO:0000250 (similarity to Q9TY95, SERA5 from P. falciparum), while the only experimental evidence (ECO:0000269, PubMed:18419771) supports 'Host cytoplasm.' The protein is also annotated as 'Secreted' and in the 'Parasitophorous vacuole.' The plasma membrane annotation is present in the database but is computational/similarity-based rather than experimentally verified for this specific protein. The expected answer is supported by the recorded annotation, though with a caveat about evidence quality.",
    "evidence_ids": ["C5", "C8", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MARLSSIVFIICLLLCNNA' is a classic hydrophobic signal peptide (16+ hydrophobic residues followed by a small-residue cleavage region), indicating the protein is a secreted/membrane-associated precursor. The extensive serine-rich repeats in the middle region ('GTQDGKGKSEGKGNEGG...SSSEKKVNSALATPPAPEVSKAQEGAGLATQKEQTPSKRAKRSPPP...') are a hallmark of the SERA (Serine Repeat Antigen) protein family in Plasmodium, which are known from P. falciparum homologs (SERA5, SERA6) to be secreted and associate with membranes (parasitophorous vacuole membrane, host cell membrane). This eliminates C (perinuclear cytoplasm — no NLS, no nuclear retention features, signal peptide directs secretion) and D (kinetoplast — Plasmodium is an Apicomplexan, not a Kinetoplastid; kinetoplasts exist only in Trypanosoma/Leishmania). Option A (peptidoglycan cell wall) is eliminated because Plasmodium is a eukaryotic parasite with no peptidoglycan. Among the remaining options, a secreted, membrane-associated protein with a signal peptide and no transmembrane anchor (peripheral membrane protein) best matches 'plasma membrane' (B).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use: (1) the visible hydrophobic N-terminal signal peptide to infer secretion/membrane association; (2) serine-rich repeat pattern to recognize the SERA family; (3) knowledge that SERA homologs (SERA5, SERA6 in P. falciparum) are secreted and membrane-associated; (4) basic taxonomy knowledge that Apicomplexa lack peptidoglycan and kinetoplasts. These transferable features meaningfully distinguish B from A, C, and D without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the UniProt entry annotates multiple locations (cell membrane, parasitophorous vacuole, secreted, host cytoplasm), among the four offered choices only B (plasma membrane) is compatible with the sequence features (signal peptide, SERA family, eukaryotic organism). Options A, C, and D are effectively excluded by basic biological reasoning. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The plasma membrane annotation in UniProt is based on similarity (ECO:0000250) to Q9TY95 (P. falciparum SERA5), not on direct experimental evidence for PbSERA3.",
    "The only experimental evidence (PubMed:18419771) supports 'Host cytoplasm' localization, which is not among the offered choices.",
    "The protein is annotated as a 'Precursor' and 'Secreted,' meaning its mature form may reside in the parasitophorous vacuole or host cytoplasm rather than the parasite's own plasma membrane.",
    "The GO:0005886 annotation is IEA (inferred from electronic annotation), not an independent experimental or manual curation assignment.",
    "The reviewer-only accession identification was derived from dataset metadata not available to the evaluated model."
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
  "benchmark_sequence_length": 1096,
  "benchmark_sequence_sha256": "b856f5c38016a9a095d324206f8bcc88f9baeee6e49705c1896ece85300d9e8d",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1096,
  "current_source_sequence_sha256": "b856f5c38016a9a095d324206f8bcc88f9baeee6e49705c1896ece85300d9e8d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A509AC44",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "selected_historical_source_sequence_length": 1096,
  "selected_historical_source_sequence_sha256": "b856f5c38016a9a095d324206f8bcc88f9baeee6e49705c1896ece85300d9e8d",
  "selected_historical_version": {
    "accession": "A0A509AC44",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SERA3_PLABA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A509AC44\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30941868\",\"source\":\"PubMed\"}],\"value\":\"Serine repeat antigen 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18419771\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30941868\",\"source\":\"PubMed\"}],\"value\":\"PbSERA3\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Serine-repeat antigen protein 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9TY95\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9TY95\",\"source\":\"UniProtKB\"}],\"id\":\"SL-9903\",\"value\":\"Peripheral membrane protein\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9TY95\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0194\",\"value\":\"Parasitophorous vacuole\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9TY95\",\"source\":\"UniProtKB\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18419771\",\"source\":\"PubMed\"}],\"id\":\"SL-0381\",\"value\":\"Host cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030430\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:host cell cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0020003\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:symbiont-containing vacuole\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/13",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Schmidt-Christensen A.\",\"Sturm A.\",\"Horstmann S.\",\"Heussler V.T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18419771\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1462-5822.2008.01162.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"1723\",\"id\":\"18419771\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"1734\",\"publicationDate\":\"2008\",\"title\":\"Expression and processing of Plasmodium berghei SERA3 during liver stages.\",\"volume\":\"10\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":2,\"referencePositions\":[\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AC44.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Pace T.\",\"Grasso F.\",\"Camarda G.\",\"Suarez C.\",\"Blackman M.J.\",\"Ponzi M.\",\"Olivieri A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30941868\"},{\"database\":\"DOI\",\"id\":\"10.1111/cmi.13028\"}],\"citationType\":\"journal article\",\"firstPage\":\"e13028\",\"id\":\"30941868\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"e13028\",\"publicationDate\":\"2019\",\"title\":\"The Plasmodium berghei serine protease PbSUB1 plays an important role in male gamete egress.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:25:23.524185+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5e2610179c828f1eae297c66cc9692929fd91c2cd3c8a5fe426e60611e991fc3",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AC44.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   SERA3_PLABA             Reviewed;        1096 AA.\nAC   A0A509AC44;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Serine-repeat antigen protein 3 {ECO:0000305};\nDE   AltName: Full=Serine repeat antigen 3 {ECO:0000303|PubMed:30941868};\nDE            Short=PbSERA3 {ECO:0000303|PubMed:18419771, ECO:0000303|PubMed:30941868};\nDE   Flags: Precursor;\nGN   Name=SERA3 {ECO:0000305};\nGN   ORFNames=PBANKA_0304900 {ECO:0000312|EMBL:VUC54088.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   SUBCELLULAR LOCATION, AND DEVELOPMENTAL STAGE.\nRX   PubMed=18419771; DOI=10.1111/j.1462-5822.2008.01162.x;\nRA   Schmidt-Christensen A., Sturm A., Horstmann S., Heussler V.T.;\nRT   \"Expression and processing of Plasmodium berghei SERA3 during liver\nRT   stages.\";\nRL   Cell. Microbiol. 10:1723-1734(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, DEVELOPMENTAL STAGE, AND PROTEOLYTIC CLEAVAGE.\nRX   PubMed=30941868; DOI=10.1111/cmi.13028;\nRA   Pace T., Grasso F., Camarda G., Suarez C., Blackman M.J., Ponzi M.,\nRA   Olivieri A.;\nRT   \"The Plasmodium berghei serine protease PbSUB1 plays an important role in\nRT   male gamete egress.\";\nRL   Cell. Microbiol. 21:e13028-e13028(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9TY95};\nCC       Peripheral membrane protein {ECO:0000250|UniProtKB:Q9TY95}.\nCC       Parasitophorous vacuole {ECO:0000250|UniProtKB:Q9TY95}. Secreted\nCC       {ECO:0000250|UniProtKB:Q9TY95}. Host cytoplasm\nCC       {ECO:0000269|PubMed:18419771}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 87-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0030430; C:host cell cytoplasm; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 88-88",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0020003; C:symbiont-containing vacuole; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:26.529482+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "35f5b1184dbbd72476667152faab01cf50de2eb2d7c9f1faf6721d3157b18971",
  "url": "https://rest.uniprot.org/unisave/A0A509AC44?format=txt&versions=26"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0009274\nname: peptidoglycan-based cell wall\nnamespace: cellular_component\ndef: \"A protective structure outside the cytoplasmic membrane composed of peptidoglycan (also known as murein), a molecule made up of a glycan (sugar) backbone of repetitively alternating N-acetylglucosamine and N-acetylmuramic acid with short, attached, cross-linked peptide chains containing unusual amino acids. An example of this component is found in Escherichia coli.\" [GOC:mlg, ISBN:0815108893]\nsynonym: \"envelope\" BROAD []\nsynonym: \"murein sacculus\" RELATED []\nsynonym: \"peptidoglycan\" NARROW []\nis_a: GO:0005618 ! cell wall\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009274",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 94735-94744",
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
  "excerpt": "[Term]\nid: GO:0020023\nname: kinetoplast\nnamespace: cellular_component\ndef: \"A sub-structure within the large single mitochondrion of kinetoplastid parasites and which is closely associated with the flagellar pocket and basal body of the flagellum.\" [GOC:mb]\nxref: Wikipedia:Kinetoplast\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005739 ! mitochondrion\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020023",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155291-155299",
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
  "excerpt": "[Term]\nid: GO:0048471\nname: perinuclear region of cytoplasm\nnamespace: cellular_component\ndef: \"Cytoplasm situated near, or occurring around, the nucleus.\" [GOC:jid]\ncomment: Note that this term should not be confused with the cellular component term 'nuclear membrane lumen ; GO:0005641', which has the synonym 'perinuclear space'.\nis_a: GO:0110165 ! cellular anatomical structure\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0048471",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 303515-303523",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
