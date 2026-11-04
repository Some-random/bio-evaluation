# GO_molecular_function_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0028.txt)

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
MLSKVVLLVALAAICGAQGASYAGRHTADMDFLHKQKKIFDLLLYVRQADLSDAEWYDVGRNYDMESNMDMYKDKNVVQKFLWWYKQGMFLSRNAIFTPLNSEQKYEVRMLFELLYNAKDFQTFYKTAAWARLRMNSGMFTTAFSIAVLYRPDTKYMKFPAIYEIYPNYFFDSSVIEEAQNLKMSRGSSVVTGMNNIETYIVNTNYSSKNMREYNDPEYKLDYFMEDVELNAYYYYMREMLPYWMSSSQYHMPKEIRGQLYYFLHKQLMTRYFLERMSNDLGKTAEFDWNKPINSGFYSTIMYSNGVTFPQRNRFSSLPYYKYKYLNVINALEMRLMDAIDSGYLIDEYGKKIDIYTPEGLNMLGNVIEGSSDSINTKFYGMYDILARDILGYNFDFQNKNNLIPSALQSYSTSMRDPAFYMLYQNILSYFLRYKKLQPQYSQSELQMPGVKFESVNIDKLYTYFDKCDTLINNAVAVENFKGGMYLRLKARRACMNYERFTYKININSDKETKGMMRIFLGPAFDEIKHDMVYLQKYFYLFMEMDRFAVTLRPGSNSIERQSSESPFTTSTIMPSDIFYDKLNKAIGGSEPFTYSEKMLGFPERLILPRGKPEGMRYKMFFFLSSMDESNTKSYEIPLYGKMTLDDKVFGFPLDRPMWAWNFTIPNMYFKDVFIYNRPNEESMNY

[Multiple Choices]
A. 2-oxoglutarate-dependent dioxygenase activity
B. nicotinate-nucleotide adenylyltransferase activity
C. nutrient reservoir activity
D. mRNA N-acetyltransferase activity
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

> The sequence-matched UniProt record describes the protein as a storage protein that may supply nutrients, directly supporting nutrient reservoir activity. The GO assignment is annotated IEA, so it is not itself proof of an experimental activity measurement.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 686-residue sequence begins with a plausible secretion signal and is a large protein without an evident catalytic signature for the offered enzyme activities. Transferable knowledge that insect hexamerin-like proteins are secreted storage proteins makes nutrient reservoir activity a credible choice over the two enzyme activities and mRNA N-acetyltransferase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable family-level knowledge provide a meaningful basis for choosing the storage-protein function; recalling this exact protein's annotation is not necessary. This remains a probabilistic sequence-based inference rather than direct proof of function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, nutrient reservoir activity is the coherent storage-protein function; no other option is comparably supported.


### Important caveats

- The supplied source annotation matches the sequence, but the cited functional annotation is curated and the GO term is marked IEA; these should not be overstated as direct experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 686-residue sequence begins with a plausible secretion signal and is a large protein without an evident catalytic signature for the offered enzyme activities. Transferable knowledge that insect hexamerin-like proteins are secreted storage proteins makes nutrient reservoir activity a credible choice over the two enzyme activities and mRNA N-acetyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable family-level knowledge provide a meaningful basis for choosing the storage-protein function; recalling this exact protein's annotation is not necessary. This remains a probabilistic sequence-based inference rather than direct proof of function."
  },
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as a storage protein that may supply nutrients, directly supporting nutrient reservoir activity. The GO assignment is annotated IEA, so it is not itself proof of an experimental activity measurement."
  },
  "important_caveats": [
    "The supplied source annotation matches the sequence, but the cited functional annotation is curated and the GO term is marked IEA; these should not be overstated as direct experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, nutrient reservoir activity is the coherent storage-protein function; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record describes the protein as a storage protein that may supply nutrients, directly supporting nutrient reservoir activity. The GO assignment is annotated IEA, so it is not itself proof of an experimental activity measurement.",
    "evidence_ids": ["H5", "H6", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 686-residue sequence begins with a plausible secretion signal and is a large protein without an evident catalytic signature for the offered enzyme activities. Transferable knowledge that insect hexamerin-like proteins are secreted storage proteins makes nutrient reservoir activity a credible choice over the two enzyme activities and mRNA N-acetyltransferase activity.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable family-level knowledge provide a meaningful basis for choosing the storage-protein function; recalling this exact protein's annotation is not necessary. This remains a probabilistic sequence-based inference rather than direct proof of function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, nutrient reservoir activity is the coherent storage-protein function; no other option is comparably supported."
  },
  "important_caveats": [
    "The supplied source annotation matches the sequence, but the cited functional annotation is curated and the GO term is marked IEA; these should not be overstated as direct experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (Hexamerin 70c, an arylphorin-type hexamerin) with GO:0045735 (nutrient reservoir activity) via IEA:UniProtKB-KW. The function comment (ECO:0000305, curator inference from PubMed:26466725) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' This directly matches the definition of nutrient reservoir activity (GO:0045735: 'Functions in the storage of nutritious substrates'). The GO annotation itself is keyword-based (IEA), but the underlying functional description is supported by literature evidence.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [H6](#evidence-h6), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can use both positive and negative sequence-based reasoning. Positive: The ~686 AA length, N-terminal signal peptide (MLSKVVLLVALAAICGAQGA...), and notably high aromatic residue density (abundant F, Y, W throughout) are hallmarks of arylphorin-type hexamerins, a well-known class of insect storage proteins. Negative: The three enzymatic alternatives (A: 2-oxoglutarate-dependent dioxygenase, B: nicotinate-nucleotide adenylyltransferase, D: mRNA N-acetyltransferase) all require specific catalytic motifs and structural folds (e.g., the His-X-Asp/Glu...His facial triad for Fe(II)/2OG dioxygenases; GNAT-fold motifs for acetyltransferases; specific transferase catalytic residues for adenylyltransferases). None of these motifs are evident in the sequence. The elimination of all three enzymatic options, combined with the positive features consistent with a secreted, aromatic-rich storage protein, meaningfully distinguishes option C. This reasoning relies on general knowledge of hexamerin family composition, the requirement of catalytic motifs for enzymatic GO terms, and the fact that nutrient reservoir activity is the only non-catalytic option among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of (1) absence of recognizable catalytic motifs needed for options A, B, and D, (2) positive sequence features (length, signal peptide, high aromatic content) consistent with hexamerin/storage protein family, and (3) the fact that C is the only non-enzymatic option, provides a credible transferable reasoning path. Recognizing hexamerins purely from sequence without BLAST is moderate-confidence, but the negative elimination of enzymatic alternatives is strong and sufficient to distinguish C among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three enzymatic options (A, B, D) require specific catalytic machinery absent from the sequence, while C (nutrient reservoir) is the only non-catalytic function. No ambiguity among options is identified given the sequence features.


### Important caveats

- The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via keyword, not direct experimental assignment of the GO term. The functional description is supported by curator inference from literature (ECO:0000305).
- Positive identification of hexamerin family membership from sequence alone (without BLAST or database lookup) relies on statistical/compositional features and is moderate-confidence; the stronger argument is the negative elimination of catalytic alternatives.
- The model does not receive organism context from the original input; recognition of insect hexamerin features relies on general knowledge of the protein family rather than organism-specific annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can use both positive and negative sequence-based reasoning. Positive: The ~686 AA length, N-terminal signal peptide (MLSKVVLLVALAAICGAQGA...), and notably high aromatic residue density (abundant F, Y, W throughout) are hallmarks of arylphorin-type hexamerins, a well-known class of insect storage proteins. Negative: The three enzymatic alternatives (A: 2-oxoglutarate-dependent dioxygenase, B: nicotinate-nucleotide adenylyltransferase, D: mRNA N-acetyltransferase) all require specific catalytic motifs and structural folds (e.g., the His-X-Asp/Glu...His facial triad for Fe(II)/2OG dioxygenases; GNAT-fold motifs for acetyltransferases; specific transferase catalytic residues for adenylyltransferases). None of these motifs are evident in the sequence. The elimination of all three enzymatic options, combined with the positive features consistent with a secreted, aromatic-rich storage protein, meaningfully distinguishes option C. This reasoning relies on general knowledge of hexamerin family composition, the requirement of catalytic motifs for enzymatic GO terms, and the fact that nutrient reservoir activity is the only non-catalytic option among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) absence of recognizable catalytic motifs needed for options A, B, and D, (2) positive sequence features (length, signal peptide, high aromatic content) consistent with hexamerin/storage protein family, and (3) the fact that C is the only non-enzymatic option, provides a credible transferable reasoning path. Recognizing hexamerins purely from sequence without BLAST is moderate-confidence, but the negative elimination of enzymatic alternatives is strong and sufficient to distinguish C among the four offered choices."
  },
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "H6",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Hexamerin 70c, an arylphorin-type hexamerin) with GO:0045735 (nutrient reservoir activity) via IEA:UniProtKB-KW. The function comment (ECO:0000305, curator inference from PubMed:26466725) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' This directly matches the definition of nutrient reservoir activity (GO:0045735: 'Functions in the storage of nutritious substrates'). The GO annotation itself is keyword-based (IEA), but the underlying functional description is supported by literature evidence."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via keyword, not direct experimental assignment of the GO term. The functional description is supported by curator inference from literature (ECO:0000305).",
    "Positive identification of hexamerin family membership from sequence alone (without BLAST or database lookup) relies on statistical/compositional features and is moderate-confidence; the stronger argument is the negative elimination of catalytic alternatives.",
    "The model does not receive organism context from the original input; recognition of insect hexamerin features relies on general knowledge of the protein family rather than organism-specific annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three enzymatic options (A, B, D) require specific catalytic machinery absent from the sequence, while C (nutrient reservoir) is the only non-catalytic function. No ambiguity among options is identified given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Hexamerin 70c, an arylphorin-type hexamerin) with GO:0045735 (nutrient reservoir activity) via IEA:UniProtKB-KW. The function comment (ECO:0000305, curator inference from PubMed:26466725) states: 'Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause.' This directly matches the definition of nutrient reservoir activity (GO:0045735: 'Functions in the storage of nutritious substrates'). The GO annotation itself is keyword-based (IEA), but the underlying functional description is supported by literature evidence.",
    "evidence_ids": ["C5", "H5", "H6", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can use both positive and negative sequence-based reasoning. Positive: The ~686 AA length, N-terminal signal peptide (MLSKVVLLVALAAICGAQGA...), and notably high aromatic residue density (abundant F, Y, W throughout) are hallmarks of arylphorin-type hexamerins, a well-known class of insect storage proteins. Negative: The three enzymatic alternatives (A: 2-oxoglutarate-dependent dioxygenase, B: nicotinate-nucleotide adenylyltransferase, D: mRNA N-acetyltransferase) all require specific catalytic motifs and structural folds (e.g., the His-X-Asp/Glu...His facial triad for Fe(II)/2OG dioxygenases; GNAT-fold motifs for acetyltransferases; specific transferase catalytic residues for adenylyltransferases). None of these motifs are evident in the sequence. The elimination of all three enzymatic options, combined with the positive features consistent with a secreted, aromatic-rich storage protein, meaningfully distinguishes option C. This reasoning relies on general knowledge of hexamerin family composition, the requirement of catalytic motifs for enzymatic GO terms, and the fact that nutrient reservoir activity is the only non-catalytic option among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "The combination of (1) absence of recognizable catalytic motifs needed for options A, B, and D, (2) positive sequence features (length, signal peptide, high aromatic content) consistent with hexamerin/storage protein family, and (3) the fact that C is the only non-enzymatic option, provides a credible transferable reasoning path. Recognizing hexamerins purely from sequence without BLAST is moderate-confidence, but the negative elimination of enzymatic alternatives is strong and sufficient to distinguish C among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three enzymatic options (A, B, D) require specific catalytic machinery absent from the sequence, while C (nutrient reservoir) is the only non-catalytic function. No ambiguity among options is identified given the sequence features."
  },
  "important_caveats": [
    "The GO annotation in UniProt is IEA (Inferred from Electronic Annotation) via keyword, not direct experimental assignment of the GO term. The functional description is supported by curator inference from literature (ECO:0000305).",
    "Positive identification of hexamerin family membership from sequence alone (without BLAST or database lookup) relies on statistical/compositional features and is moderate-confidence; the stronger argument is the negative elimination of catalytic alternatives.",
    "The model does not receive organism context from the original input; recognition of insect hexamerin features relies on general knowledge of the protein family rather than organism-specific annotation."
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
  "benchmark_sequence_length": 686,
  "benchmark_sequence_sha256": "e99f815c225123fa881654bcd2a375eda966a82ada02a8e1d32d4b9aee231181",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-06-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 686,
  "current_source_sequence_sha256": "e99f815c225123fa881654bcd2a375eda966a82ada02a8e1d32d4b9aee231181",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8U1C2Y4",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "selected_historical_source_sequence_length": 686,
  "selected_historical_source_sequence_sha256": "e99f815c225123fa881654bcd2a375eda966a82ada02a8e1d32d4b9aee231181",
  "selected_historical_version": {
    "accession": "A0A8U1C2Y4",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HEX7C_APIME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8U1C2Y4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-06-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Honeybee\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000005203\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Hymenoptera\",\"Apocrita\",\"Aculeata\",\"Apoidea\",\"Anthophila\",\"Apidae\",\"Apis\"],\"scientificName\":\"Apis mellifera\",\"taxonId\":7460}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34309096\",\"source\":\"PubMed\"}],\"value\":\"Arylphorin Hex70c\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9692239\",\"source\":\"PubMed\"}],\"value\":\"Hexamerin 70c\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"26466725\",\"source\":\"PubMed\"}],\"value\":\"Storage protein produced during nutritional abundance, which may function as a nutrient supply to compensate for lack of dietary proteins during metamorphosis, egg production and diapause\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Danty E.\",\"Arnold G.\",\"Burmester T.\",\"Huet J.C.\",\"Huet D.\",\"Pernollet J.C.\",\"Masson C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9692239\"},{\"database\":\"DOI\",\"id\":\"10.1016/s0965-1748(98)00011-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"387\",\"id\":\"9692239\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"397\",\"publicationDate\":\"1998\",\"title\":\"Identification and developmental profiles of hexamerins in antenna and hemolymph of the honeybee, Apis mellifera.\",\"volume\":\"28\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":6,\"referencePositions\":[\"PROTEIN SEQUENCE OF 20-34\",\"DEVELOPMENTAL STAGE\",\"PROTEOLYTIC CLEAVAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Martins J.R.\",\"Bitondi M.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26466725\"},{\"database\":\"DOI\",\"id\":\"10.3390/insects3041039\"}],\"citationType\":\"journal article\",\"firstPage\":\"1039\",\"id\":\"26466725\",\"journal\":\"Insects\",\"lastPage\":\"1055\",\"publicationDate\":\"2012\",\"title\":\"Nuclear Immunolocalization of Hexamerins in the Fat Body of Metamorphosing Honey Bees.\",\"volume\":\"3\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":8,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/7",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Vieira J.\",\"Freitas F.C.P.\",\"Cristino A.S.\",\"Moda L.M.R.\",\"Martins J.R.\",\"Bitondi M.M.G.\",\"Simoes Z.L.P.\",\"Barchuk A.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34309096\"},{\"database\":\"DOI\",\"id\":\"10.1111/imb.12728\"}],\"citationType\":\"journal article\",\"firstPage\":\"594\",\"id\":\"34309096\",\"journal\":\"Insect Mol. Biol.\",\"lastPage\":\"604\",\"publicationDate\":\"2021\",\"title\":\"miRNA-34 and miRNA-210 target hexamerin genes enhancing their differential expression during early brain development of honeybee (Apis mellifera) castes.\",\"volume\":\"30\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":9,\"referencePositions\":[\"DEVELOPMENTAL STAGE\",\"INDUCTION BY MIRNA\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/8",
  "retrieved_utc": "2026-11-02T04:26:05.694578+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f226ca0b06a4020321d4624eb4e083173eb57e52374d87432967d135d8879bed",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8U1C2Y4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   HEX7C_APIME             Reviewed;         686 AA.\nAC   A0A8U1C2Y4; A0A8B6WZ79; A5YV87; A6YLP8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-JUN-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Hexamerin 70c {ECO:0000303|PubMed:9692239};\nDE   AltName: Full=Arylphorin Hex70c {ECO:0000303|PubMed:34309096};\nDE   Flags: Precursor;\nGN   Name=Hex70c {ECO:0000303|PubMed:9692239,\nGN   ECO:0000312|RefSeq:NP_001092187.1};\nGN   Synonyms=409354 {ECO:0000312|EnsemblMetazoa:NP_001092187};\nOS   Apis mellifera (Honeybee).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;\nOC   Anthophila; Apidae; Apis.\nOX   NCBI_TaxID=7460 {ECO:0000312|Proteomes:UP000005203, ECO:0000312|Proteomes:UP001105180};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [6] {ECO:0000305}\nRP   PROTEIN SEQUENCE OF 20-34, DEVELOPMENTAL STAGE, AND PROTEOLYTIC CLEAVAGE.\nRX   PubMed=9692239; DOI=10.1016/s0965-1748(98)00011-3;\nRA   Danty E., Arnold G., Burmester T., Huet J.C., Huet D., Pernollet J.C.,\nRA   Masson C.;\nRT   \"Identification and developmental profiles of hexamerins in antenna and\nRT   hemolymph of the honeybee, Apis mellifera.\";\nRL   Insect Biochem. Mol. Biol. 28:387-397(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "RN   [8] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, TISSUE SPECIFICITY, AND DEVELOPMENTAL\nRP   STAGE.\nRX   PubMed=26466725; DOI=10.3390/insects3041039;\nRA   Martins J.R., Bitondi M.M.;\nRT   \"Nuclear Immunolocalization of Hexamerins in the Fat Body of Metamorphosing\nRT   Honey Bees.\";\nRL   Insects 3:1039-1055(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 76-83",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "RN   [9] {ECO:0000305}\nRP   DEVELOPMENTAL STAGE, AND INDUCTION BY MIRNA.\nRX   PubMed=34309096; DOI=10.1111/imb.12728;\nRA   Vieira J., Freitas F.C.P., Cristino A.S., Moda L.M.R., Martins J.R.,\nRA   Bitondi M.M.G., Simoes Z.L.P., Barchuk A.R.;\nRT   \"miRNA-34 and miRNA-210 target hexamerin genes enhancing their differential\nRT   expression during early brain development of honeybee (Apis mellifera)\nRT   castes.\";\nRL   Insect Mol. Biol. 30:594-604(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Storage protein produced during nutritional abundance, which\nCC       may function as a nutrient supply to compensate for lack of dietary\nCC       proteins during metamorphosis, egg production and diapause.\nCC       {ECO:0000305|PubMed:26466725}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0045735; F:nutrient reservoir activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:07.744095+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5b78371342b563bd895a42c33846d29247ccb53979102fb9ae0e54ce91fe4d52",
  "url": "https://rest.uniprot.org/unisave/A0A8U1C2Y4?format=txt&versions=13"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004515\nname: nicotinate-nucleotide adenylyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: nicotinate beta-D-ribonucleotide + ATP + H+ = deamido-NAD+ + diphosphate.\" [RHEA:22860]\nsynonym: \"ATP:nicotinate-nucleotide adenylyltransferase activity\" EXACT []\nsynonym: \"ATP:nicotinate-ribonucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) diphosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD(+) pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamido-NAD+ pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"deamidonicotinamide adenine dinucleotide pyrophosphorylase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"NaMN-ATase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinate mononucleotide adenylyltransferase activity\" RELATED [EC:2.7.7.18]\nsynonym: \"nicotinic acid mononucleotide adenylyltransferase\" NARROW []\nxref: EC:2.7.7.18\nxref: MetaCyc:NICONUCADENYLYLTRAN-RXN\nxref: Reactome:R-HSA-197235 \"NMNAT2 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200474 \"NMNAT3 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: Reactome:R-HSA-200512 \"NMNAT1 transfers an adenylyl group from ATP to NAMN to yield NAAD\"\nxref: RHEA:22860\nis_a: GO:0070566 ! adenylyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.7.18\nproperty_value: skos:exactMatch MetaCyc:NICONUCADENYLYLTRAN-RXN\nproperty_value: skos:exactMatch RHEA:22860\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004515",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 43770-43794",
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
  "excerpt": "[Term]\nid: GO:0016706\nname: 2-oxoglutarate-dependent dioxygenase activity\nnamespace: molecular_function\nalt_id: GO:0010302\ndef: \"Catalysis of the reaction: A + 2-oxoglutarate + O2 = B + succinate + CO2. This is an oxidation-reduction (redox) reaction in which hydrogen or electrons are transferred from 2-oxoglutarate and one other donor, and one atom of oxygen is incorporated into each donor.\" [GOC:mah]\nsynonym: \"2-oxoglutarate dioxygenase activity\" EXACT []\nsynonym: \"oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor, and incorporation of one atom each of oxygen into both donors\" EXACT []\nxref: EC:1.14.11.-\nxref: Reactome:R-HSA-1234164 \"Cytosolic HIF1AN (FIH1) hydroxylates asparagine residues of Hypoxia-inducible Factor Alpha (HIF1A,HIF2A)\"\nxref: Reactome:R-HSA-6783455 \"TYW5 hydroxylates yW-72 yielding OHyW-72 at nucleotide 37 of tRNA(Phe)\"\nis_a: GO:0016705 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen\nis_a: GO:0051213 ! dioxygenase activity\nproperty_value: skos:exactMatch EC:1.14.11.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016706",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129228-129242",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
