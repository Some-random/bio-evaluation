# GO_molecular_function_0065

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0065.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — nutrient reservoir activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIVIMKAGFLFLASLCLLVQAVPNKVADKTYVTRQKNIYELFWHVDQPTVYHPELYQKARTFNLVENLDNYNDKEAVNEFMQLLKHGMLPRGQVFTMMNKEMRHQAVVLFRLLYSAKTFDVFYNTAVWARFNVNEQMYLYALSVAVIHRPDTKLMKLPPMYEVMPHLYFNDEVMQKAYNIAMGDTADMKKTYNNIDYYLLAANYTGWYLTKHNVPEQRLNYFTEDVGLNHFYFMLNHNYPPFMLSNSLNFPQIRGEFYFFLHKQVLNRYYLERLSNDMGEVSYVSLDHPIPTGYYPTMRFRNGLAFPQRETGATVPLHMQKYVQMIHDLHTRISTAIDLGYVVDSYGNHVKLYTKQGLNVLGNIVQGNGDSVNVQLYGQLDLLVRKVLGFGYESNVKYQVVPSALQMWSTSLRDPVFFSIYKTILDYYHKYKENLPKYTTEELNFPGVSIESVTVDKLITYFDHFESMLNNGVSIQSHAKAKNTMIKARQYRLNHKPFTYHIVVNSDKNVKGMVRIFLGPKYDEFGHEVDLVHNYMNFMQMDEFVVNLKSGSNTIERNSHESVFVVPDEVPSDVLYNRLVVSEDGSETFKYSSQPYGFPERLLLPKGKKEGMPYNVLVVVSPFDDSNVVQIDSPVWGRHIYDGRAMGFPLDKPVDPLLLVLSNIHVKEVLVHHREMEELNVAL

[Multiple Choices]
A. UDP-glucose 6-dehydrogenase activity
B. quercetin 3-O-glucosyltransferase activity
C. nutrient reservoir activity
D. hydrolase activity, acting on ester bonds
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record describes this protein as a storage protein that supplies nutrients and annotates it with GO:0045735, nutrient reservoir activity. The GO annotation carries IDA evidence, and the function comment cites experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal signal peptide followed by a large globular protein, a pattern compatible with a secreted storage protein. Its length and overall sequence also make a hexamerin-like storage-protein family inference plausible. This distinguishes C from the offered specific catalytic activities: the sequence does not show an obvious signature for UDP-glucose dehydrogenase, quercetin glucosyltransferase, or an ester hydrolase. This is a probabilistic family/sequence inference, not a functional proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about secreted hexamerin-like storage proteins and the contrast with the offered enzyme activities provides a meaningful basis for choosing C without relying on the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, nutrient reservoir activity is the one consistent with a non-catalytic storage-protein inference; the alternatives name specific enzyme activities.


### Important caveats

- The sequence alone does not establish the protein's organism or exact family assignment; the answerability argument is probabilistic.
- The reviewer-only sequence-matched annotation supports the key but was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide followed by a large globular protein, a pattern compatible with a secreted storage protein. Its length and overall sequence also make a hexamerin-like storage-protein family inference plausible. This distinguishes C from the offered specific catalytic activities: the sequence does not show an obvious signature for UDP-glucose dehydrogenase, quercetin glucosyltransferase, or an ester hydrolase. This is a probabilistic family/sequence inference, not a functional proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about secreted hexamerin-like storage proteins and the contrast with the offered enzyme activities provides a meaningful basis for choosing C without relying on the exact protein's recorded annotation."
  },
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a storage protein that supplies nutrients and annotates it with GO:0045735, nutrient reservoir activity. The GO annotation carries IDA evidence, and the function comment cites experimental evidence."
  },
  "important_caveats": [
    "The sequence alone does not establish the protein's organism or exact family assignment; the answerability argument is probabilistic.",
    "The reviewer-only sequence-matched annotation supports the key but was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, nutrient reservoir activity is the one consistent with a non-catalytic storage-protein inference; the alternatives name specific enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes this protein as a storage protein that supplies nutrients and annotates it with GO:0045735, nutrient reservoir activity. The GO annotation carries IDA evidence, and the function comment cites experimental evidence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide followed by a large globular protein, a pattern compatible with a secreted storage protein. Its length and overall sequence also make a hexamerin-like storage-protein family inference plausible. This distinguishes C from the offered specific catalytic activities: the sequence does not show an obvious signature for UDP-glucose dehydrogenase, quercetin glucosyltransferase, or an ester hydrolase. This is a probabilistic family/sequence inference, not a functional proof.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about secreted hexamerin-like storage proteins and the contrast with the offered enzyme activities provides a meaningful basis for choosing C without relying on the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, nutrient reservoir activity is the one consistent with a non-catalytic storage-protein inference; the alternatives name specific enzyme activities."
  },
  "important_caveats": [
    "The sequence alone does not establish the protein's organism or exact family assignment; the answerability argument is probabilistic.",
    "The reviewer-only sequence-matched annotation supports the key but was not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 'nutrient reservoir activity' with evidence code IDA (Inferred from Direct Assay), supported by PubMed:16055147 and PubMed:26466725. The FUNCTION comment explicitly states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition is 'Functions in the storage of nutritious substrates,' with synonyms including 'storage protein' and 'storage protein of fat body (sensu Insecta).' The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is fully supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 683-residue sequence encodes a large secreted protein (~70 kDa mature form after signal peptide cleavage) with no identifiable catalytic motifs for any of the three enzymatic options. (A) UDP-glucose 6-dehydrogenase requires a Rossmann-fold NAD(P)-binding domain and specific catalytic residues — absent. (B) Quercetin 3-O-glucosyltransferase requires a plant/animal glycosyltransferase PSPG box or similar sugar-donor binding motif — absent. (D) Hydrolase acting on ester bonds requires a catalytic triad (e.g., Ser-His-Asp/Asp) or a lipase/esterase GxSxG nucleophile elbow — absent. The only remaining option, (C) nutrient reservoir activity, is a non-catalytic GO term (GO:0045735, synonyms: 'storage protein', 'storage protein of fat body sensu Insecta') that describes a protein whose molecular function is to store nutrients. Transferable knowledge from other insect storage proteins (hexamerins, arylphorins, vitellogenins) establishes that large (~70-80 kDa) secreted proteins lacking catalytic domains, often rich in aromatic residues, function as nutrient reservoirs. The sequence's aromatic-rich composition (numerous F, Y, W residues), its size, secretory signal peptide, and complete absence of enzymatic machinery are all consistent with this family. By elimination of the three catalytic options and positive match to the storage-protein paradigm, C is the defensible answer.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can distinguish the answer by (1) scanning the sequence for catalytic motifs required by options A, B, and D and finding none, and (2) recognizing that the protein's size, secretory nature, aromatic-rich composition, and lack of domains match the well-characterized insect storage-protein family (hexamerins/arylphorins), for which 'nutrient reservoir activity' is the canonical GO molecular function. This inference relies on general knowledge of catalytic domain architecture and the storage-protein family, not on recalling the specific UniProt entry for this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D each require specific catalytic machinery (Rossmann fold, PSPG box, catalytic triad) that is absent from the sequence. Option C is the only non-catalytic molecular function and is the sole option consistent with a large secreted protein lacking any recognizable enzymatic domain. No ambiguity among the four choices.


### Important caveats

- The model cannot determine from the sequence alone that this is an insect protein or specifically a hexamerin; the strongest transferable argument is the elimination of all three catalytic options by absence of required motifs, combined with the general profile matching large secreted storage proteins.
- The GO term 'nutrient reservoir activity' (GO:0045735) is relatively uncommon and may not be immediately recognized by all models, but its definition ('Functions in the storage of nutritious substrates') and synonyms ('storage protein') make it inferable by elimination.
- The reviewer-only evidence confirms the annotation is IDA (direct assay), but the model must rely on sequence-based reasoning and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 683-residue sequence encodes a large secreted protein (~70 kDa mature form after signal peptide cleavage) with no identifiable catalytic motifs for any of the three enzymatic options. (A) UDP-glucose 6-dehydrogenase requires a Rossmann-fold NAD(P)-binding domain and specific catalytic residues — absent. (B) Quercetin 3-O-glucosyltransferase requires a plant/animal glycosyltransferase PSPG box or similar sugar-donor binding motif — absent. (D) Hydrolase acting on ester bonds requires a catalytic triad (e.g., Ser-His-Asp/Asp) or a lipase/esterase GxSxG nucleophile elbow — absent. The only remaining option, (C) nutrient reservoir activity, is a non-catalytic GO term (GO:0045735, synonyms: 'storage protein', 'storage protein of fat body sensu Insecta') that describes a protein whose molecular function is to store nutrients. Transferable knowledge from other insect storage proteins (hexamerins, arylphorins, vitellogenins) establishes that large (~70-80 kDa) secreted proteins lacking catalytic domains, often rich in aromatic residues, function as nutrient reservoirs. The sequence's aromatic-rich composition (numerous F, Y, W residues), its size, secretory signal peptide, and complete absence of enzymatic machinery are all consistent with this family. By elimination of the three catalytic options and positive match to the storage-protein paradigm, C is the defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by (1) scanning the sequence for catalytic motifs required by options A, B, and D and finding none, and (2) recognizing that the protein's size, secretory nature, aromatic-rich composition, and lack of domains match the well-characterized insect storage-protein family (hexamerins/arylphorins), for which 'nutrient reservoir activity' is the canonical GO molecular function. This inference relies on general knowledge of catalytic domain architecture and the storage-protein family, not on recalling the specific UniProt entry for this sequence."
  },
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 'nutrient reservoir activity' with evidence code IDA (Inferred from Direct Assay), supported by PubMed:16055147 and PubMed:26466725. The FUNCTION comment explicitly states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition is 'Functions in the storage of nutritious substrates,' with synonyms including 'storage protein' and 'storage protein of fat body (sensu Insecta).' The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is fully supported by experimental evidence."
  },
  "important_caveats": [
    "The model cannot determine from the sequence alone that this is an insect protein or specifically a hexamerin; the strongest transferable argument is the elimination of all three catalytic options by absence of required motifs, combined with the general profile matching large secreted storage proteins.",
    "The GO term 'nutrient reservoir activity' (GO:0045735) is relatively uncommon and may not be immediately recognized by all models, but its definition ('Functions in the storage of nutritious substrates') and synonyms ('storage protein') make it inferable by elimination.",
    "The reviewer-only evidence confirms the annotation is IDA (direct assay), but the model must rely on sequence-based reasoning and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D each require specific catalytic machinery (Rossmann fold, PSPG box, catalytic triad) that is absent from the sequence. Option C is the only non-catalytic molecular function and is the sole option consistent with a large secreted protein lacking any recognizable enzymatic domain. No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6J4Q1 (Hexamerin 70b, Apis mellifera) is annotated with GO:0045735 'nutrient reservoir activity' with evidence code IDA (Inferred from Direct Assay), supported by PubMed:16055147 and PubMed:26466725. The FUNCTION comment explicitly states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' The GO term definition is 'Functions in the storage of nutritious substrates,' with synonyms including 'storage protein' and 'storage protein of fat body (sensu Insecta).' The sequence matches the benchmark input exactly (SHA-256 confirmed). The expected answer C is fully supported by experimental evidence.",
    "evidence_ids": ["C5", "C6", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 683-residue sequence encodes a large secreted protein (~70 kDa mature form after signal peptide cleavage) with no identifiable catalytic motifs for any of the three enzymatic options. (A) UDP-glucose 6-dehydrogenase requires a Rossmann-fold NAD(P)-binding domain and specific catalytic residues — absent. (B) Quercetin 3-O-glucosyltransferase requires a plant/animal glycosyltransferase PSPG box or similar sugar-donor binding motif — absent. (D) Hydrolase acting on ester bonds requires a catalytic triad (e.g., Ser-His-Asp/Asp) or a lipase/esterase GxSxG nucleophile elbow — absent. The only remaining option, (C) nutrient reservoir activity, is a non-catalytic GO term (GO:0045735, synonyms: 'storage protein', 'storage protein of fat body sensu Insecta') that describes a protein whose molecular function is to store nutrients. Transferable knowledge from other insect storage proteins (hexamerins, arylphorins, vitellogenins) establishes that large (~70-80 kDa) secreted proteins lacking catalytic domains, often rich in aromatic residues, function as nutrient reservoirs. The sequence's aromatic-rich composition (numerous F, Y, W residues), its size, secretory signal peptide, and complete absence of enzymatic machinery are all consistent with this family. By elimination of the three catalytic options and positive match to the storage-protein paradigm, C is the defensible answer.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can distinguish the answer by (1) scanning the sequence for catalytic motifs required by options A, B, and D and finding none, and (2) recognizing that the protein's size, secretory nature, aromatic-rich composition, and lack of domains match the well-characterized insect storage-protein family (hexamerins/arylphorins), for which 'nutrient reservoir activity' is the canonical GO molecular function. This inference relies on general knowledge of catalytic domain architecture and the storage-protein family, not on recalling the specific UniProt entry for this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D each require specific catalytic machinery (Rossmann fold, PSPG box, catalytic triad) that is absent from the sequence. Option C is the only non-catalytic molecular function and is the sole option consistent with a large secreted protein lacking any recognizable enzymatic domain. No ambiguity among the four choices."
  },
  "important_caveats": [
    "The model cannot determine from the sequence alone that this is an insect protein or specifically a hexamerin; the strongest transferable argument is the elimination of all three catalytic options by absence of required motifs, combined with the general profile matching large secreted storage proteins.",
    "The GO term 'nutrient reservoir activity' (GO:0045735) is relatively uncommon and may not be immediately recognized by all models, but its definition ('Functions in the storage of nutritious substrates') and synonyms ('storage protein') make it inferable by elimination.",
    "The reviewer-only evidence confirms the annotation is IDA (direct assay), but the model must rely on sequence-based reasoning and family-level knowledge."
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
  "benchmark_sequence_length": 683,
  "benchmark_sequence_sha256": "f4b048de8ee619ce77fda9672606f89d5d12ce8f67699d144b1a6c73f4676898",
  "current_entry_audit": {
    "entryVersion": 127,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 683,
  "current_source_sequence_sha256": "f4b048de8ee619ce77fda9672606f89d5d12ce8f67699d144b1a6c73f4676898",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 125,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q6J4Q1",
  "selected_historical_entry_version": 125,
  "selected_historical_record_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "selected_historical_source_sequence_length": 683,
  "selected_historical_source_sequence_sha256": "f4b048de8ee619ce77fda9672606f89d5d12ce8f67699d144b1a6c73f4676898",
  "selected_historical_version": {
    "accession": "Q6J4Q1",
    "database": "Swiss-Prot",
    "entryVersion": 125,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HEX7B_APIME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q6J4Q1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":127,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Honeybee\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000005203\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Hymenoptera\",\"Apocrita\",\"Aculeata\",\"Apoidea\",\"Anthophila\",\"Apidae\",\"Apis\"],\"scientificName\":\"Apis mellifera\",\"taxonId\":7460}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9692239\",\"source\":\"PubMed\"}],\"value\":\"Hexamerin 70b\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16055147\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26466725\",\"source\":\"PubMed\"}],\"value\":\"Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"16055147\",\"source\":\"PubMed\"}],\"id\":\"GO:0045735\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:nutrient reservoir activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Cunha A.D.\",\"Nascimento A.M.\",\"Guidugli K.R.\",\"Simoes Z.L.\",\"Bitondi M.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16055147\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jinsphys.2005.06.004\"}],\"citationType\":\"journal article\",\"firstPage\":\"1135\",\"id\":\"16055147\",\"journal\":\"J. Insect Physiol.\",\"lastPage\":\"1147\",\"publicationDate\":\"2005\",\"title\":\"Molecular cloning and expression of a hexamerin cDNA from the honey bee, Apis mellifera.\",\"volume\":\"51\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAT11850.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"DEVELOPMENTAL STAGE\",\"INDUCTION BY JUVENILE HORMONE AND ECDYSTERONE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Danty E.\",\"Arnold G.\",\"Burmester T.\",\"Huet J.C.\",\"Huet D.\",\"Pernollet J.C.\",\"Masson C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9692239\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0965-1748(98)00011-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"387\",\"id\":\"9692239\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"397\",\"publicationDate\":\"1998\",\"title\":\"Identification and developmental profiles of hexamerins in antenna and hemolymph of the honeybee, Apis mellifera.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"NP_001011600.1\",\"source\":\"RefSeq\"}],\"referenceNumber\":6,\"referencePositions\":[\"PROTEIN SEQUENCE OF 22-36\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6J4Q1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Martins J.R.\",\"Bitondi M.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26466725\"},{\"database\":\"DOI\",\"id\":\"10.3390/insects3041039\"}],\"citationType\":\"journal article\",\"firstPage\":\"1039\",\"id\":\"26466725\",\"journal\":\"Insects\",\"lastPage\":\"1055\",\"publicationDate\":\"2012\",\"title\":\"Nuclear Immunolocalization of Hexamerins in the Fat Body of Metamorphosing Honey Bees.\",\"volume\":\"3\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:31:33.250244+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c1c0760fdb20004483effb46d2067e52a914320172dbb09e0a7d752bacac092",
  "url": "https://rest.uniprot.org/uniprotkb/Q6J4Q1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H1",
  "excerpt": "ID   HEX7B_APIME             Reviewed;         683 AA.\nAC   Q6J4Q1; A0A7M6UKD0; A0A8B6WYY8; A0A8U0WQ75; Q9Y1C3;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 125.\nDE   RecName: Full=Hexamerin 70b {ECO:0000303|PubMed:9692239};\nDE   Flags: Precursor;\nGN   Name=Hex70b {ECO:0000303|PubMed:9692239,\nGN   ECO:0000312|RefSeq:NP_001011600.1};\nGN   Synonyms=406117 {ECO:0000312|EnsemblMetazoa:NP_001011600};\nOS   Apis mellifera (Honeybee).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;\nOC   Anthophila; Apidae; Apis.\nOX   NCBI_TaxID=7460 {ECO:0000312|Proteomes:UP000005203};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAT11850.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, DEVELOPMENTAL STAGE, AND INDUCTION BY\nRP   JUVENILE HORMONE AND ECDYSTERONE.\nRX   PubMed=16055147; DOI=10.1016/j.jinsphys.2005.06.004;\nRA   Cunha A.D., Nascimento A.M., Guidugli K.R., Simoes Z.L., Bitondi M.M.;\nRT   \"Molecular cloning and expression of a hexamerin cDNA from the honey bee,\nRT   Apis mellifera.\";\nRL   J. Insect Physiol. 51:1135-1147(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H3",
  "excerpt": "RN   [6] {ECO:0000312|RefSeq:NP_001011600.1}\nRP   PROTEIN SEQUENCE OF 22-36, DEVELOPMENTAL STAGE, AND PROTEOLYTIC CLEAVAGE.\nRX   PubMed=9692239; DOI=10.1016/s0965-1748(98)00011-3;\nRA   Danty E., Arnold G., Burmester T., Huet J.C., Huet D., Pernollet J.C.,\nRA   Masson C.;\nRT   \"Identification and developmental profiles of hexamerins in antenna and\nRT   hemolymph of the honeybee, Apis mellifera.\";\nRL   Insect Biochem. Mol. Biol. 28:387-397(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H4",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, TISSUE SPECIFICITY, AND DEVELOPMENTAL\nRP   STAGE.\nRX   PubMed=26466725; DOI=10.3390/insects3041039;\nRA   Martins J.R., Bitondi M.M.;\nRT   \"Nuclear Immunolocalization of Hexamerins in the Fat Body of Metamorphosing\nRT   Honey Bees.\";\nRL   Insects 3:1039-1055(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Storage protein produced during nutritional abundance, which\nCC       may function as a nutrient supply to compensate for lack of dietary\nCC       proteins during metamorphosis, egg production and diapause.\nCC       {ECO:0000269|PubMed:16055147, ECO:0000305|PubMed:26466725}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125)

```json
{
  "entry_version": 125,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0045735; F:nutrient reservoir activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:39.845057+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-160",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eafa09edc6509c05dd80048826da7fccdeb431f6e1785eeaedaf3b2ef5191130",
  "url": "https://rest.uniprot.org/unisave/Q6J4Q1?format=txt&versions=125"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003979\nname: UDP-glucose 6-dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: H2O + 2 NAD+ + UDP-alpha-D-glucose = 3 H+ + 2 NADH + UDP-alpha-D-glucuronate.\" [EC:1.1.1.22, RHEA:23596]\nxref: EC:1.1.1.22\nxref: KEGG_REACTION:R00286\nxref: MetaCyc:UGD-RXN\nxref: Reactome:R-HSA-173597 \"UDP-glucose is oxidised to UDP-glucuronate\"\nxref: RHEA:23596\nis_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor\nproperty_value: skos:exactMatch EC:1.1.1.22\nproperty_value: skos:exactMatch RHEA:23596\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003979",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 32563-32576",
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
  "excerpt": "[Term]\nid: GO:0016788\nname: hydrolase activity, acting on ester bonds\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of any ester bond.\" [GOC:jl]\nsubset: goslim_chembl\nsynonym: \"esterase activity\" EXACT []\nxref: EC:3.1.-.-\nxref: Reactome:R-HSA-162729 \"uPAR-acyl-GPI + H2O -> uPAR + long-chain fatty acid\"\nxref: Reactome:R-HSA-9023617 \"Butyrylcholinesterase hydrolyzes acyl Ghrelin\"\nxref: Reactome:R-HSA-9023619 \"Platelet-activating factor acetylhydrolase (PLA2G7) hydrolyzes acyl Ghrelin\"\nxref: Reactome:R-HSA-9749609 \"BCHE hydrolyzes ASA-\"\nis_a: GO:0016787 ! hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016788",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130194-130208",
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
  "excerpt": "[Term]\nid: GO:0045735\nname: nutrient reservoir activity\nnamespace: molecular_function\ndef: \"Functions in the storage of nutritious substrates.\" [GOC:ai]\ncomment: Note that this term can be used in place of the obsolete terms 'storage protein ; GO:0005187' and 'storage protein of fat body (sensu Insecta) ; GO:0008041'.\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_prokaryote\nsynonym: \"storage protein\" RELATED []\nsynonym: \"storage protein of fat body\" RELATED []\nsynonym: \"yolk protein\" RELATED []\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045735",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 268007-268020",
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
  "excerpt": "[Term]\nid: GO:0080043\nname: quercetin 3-O-glucosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a glucosyl group from UDP-glucose to the 3-hydroxy group of a quercetin molecule.\" [PMID:15352060]\nis_a: GO:0035251 ! UDP-glucosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0080043",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 392452-392458",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
