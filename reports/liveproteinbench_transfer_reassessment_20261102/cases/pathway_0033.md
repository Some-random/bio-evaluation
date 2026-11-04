# pathway_0033

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0033.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Steroid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGLSHSGEIVYIHPSSPVDLFTTCASLPTKPPPSFSDMPSPLFLVSGFLGVCVAYAVANIIRQLLFPNAKEPPVVFHWFPWLGSALTYGKDPYKFLFAARAKYGDVFTFVLLGRNVTVHLGVAGNDFVFNGKETHMNAEEIYGPLCNPVFGEGVVYDCPNSKLMEQKKFVKFGLTTDALKAHVRLIEHEVVNYIKSSRDFKGPSGVINVPPVMAQITIFTAAIALQGPEVRSKLTNEFASLYHDLDGGFSPINFVLPHAPFPHNIKRDRAQLKMRKIYEAIIAERRAGKIPPTTDMISHLMQCSYKNGRPIPDSEISNMMITILMAGQHNSSNIASWIMLHLANEPQLCEELYQEQLDQLADEHGNLPELELHTVEKLKLHSSVVKETLRMHNAIHSIMRLVKQPLPVPNTSWTVPPGHAVLASPGVSANSNEYFLNPTKWDPHRWDDRVIEEDDESEMVDYGYGRTSRGTKSAYLPFGGGRHRCIGEKFAYLNLEVITAVMVRNFRFKNVDGRVDVPGTDYSTMFSRPLEPAEICWERR

[Multiple Choices]
A. Polyketide biosynthesis. .
B. Steroid biosynthesis
C. Protein modification
D. L-isoleucine biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The matched-sequence annotation identifies the protein as a sterol 14-alpha demethylase and places it in steroid/sterol biosynthesis. The pathway annotation is supported by similarity transfer, so it is not by itself direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal segment consistent with a membrane-associated cytochrome P450 and a C-terminal cysteine-containing P450 heme-binding signature. Transferable knowledge of the CYP51 family links sterol 14-alpha demethylases to sterol/steroid biosynthesis, distinguishing choice B from polyketide biosynthesis, protein modification, and L-isoleucine biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence features meaningfully distinguishes the offered pathway choices; it does not require knowing this exact protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Sterol biosynthesis is appropriately captured by the offered steroid biosynthesis choice; no other option is comparably supported.


### Important caveats

- The supplied sequence is not named or contextualized in the original input; the inference depends on recognizing transferable P450/CYP51 sequence features.
- The cited pathway annotation is similarity-based, and the reviewer-only evidence does not independently establish direct experimental validation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with a membrane-associated cytochrome P450 and a C-terminal cysteine-containing P450 heme-binding signature. Transferable knowledge of the CYP51 family links sterol 14-alpha demethylases to sterol/steroid biosynthesis, distinguishing choice B from polyketide biosynthesis, protein modification, and L-isoleucine biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features meaningfully distinguishes the offered pathway choices; it does not require knowing this exact protein's database annotation."
  },
  "case_id": "pathway_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence annotation identifies the protein as a sterol 14-alpha demethylase and places it in steroid/sterol biosynthesis. The pathway annotation is supported by similarity transfer, so it is not by itself direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied sequence is not named or contextualized in the original input; the inference depends on recognizing transferable P450/CYP51 sequence features.",
    "The cited pathway annotation is similarity-based, and the reviewer-only evidence does not independently establish direct experimental validation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Sterol biosynthesis is appropriately captured by the offered steroid biosynthesis choice; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence annotation identifies the protein as a sterol 14-alpha demethylase and places it in steroid/sterol biosynthesis. The pathway annotation is supported by similarity transfer, so it is not by itself direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with a membrane-associated cytochrome P450 and a C-terminal cysteine-containing P450 heme-binding signature. Transferable knowledge of the CYP51 family links sterol 14-alpha demethylases to sterol/steroid biosynthesis, distinguishing choice B from polyketide biosynthesis, protein modification, and L-isoleucine biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence features meaningfully distinguishes the offered pathway choices; it does not require knowing this exact protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Sterol biosynthesis is appropriately captured by the offered steroid biosynthesis choice; no other option is comparably supported."
  },
  "important_caveats": [
    "The supplied sequence is not named or contextualized in the original input; the inference depends on recognizing transferable P450/CYP51 sequence features.",
    "The cited pathway annotation is similarity-based, and the reviewer-only evidence does not independently establish direct experimental validation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB annotates P0DXV0 as Sterol 14-alpha demethylase (CYP51, EC 1.14.14.154) with pathway annotation 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250, similarity to Q4WNT5). The protein is also called 'Ergosterol biosynthesis protein' and 'Lanomycin biosynthesis cluster protein 1,' consistent with steroid/sterol biosynthesis. The answer B is supported by the database annotation, though the pathway assignment is by similarity transfer rather than direct experimental proof of the full pathway context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding motif: 'FGEGVVYDCP' in the central region, where the conserved Cys serves as the heme iron axial ligand, preceded by the FGxG pattern typical of the P450 I-helix. The ~540-aa length with an N-terminal hydrophobic membrane-anchoring segment is characteristic of fungal microsomal P450s. Among the four offered pathways, only steroid biosynthesis is classically and prominently P450-dependent (CYP51/sterol 14α-demethylase in fungi, CYP17/CYP21 in animals). Polyketide biosynthesis uses large multi-domain PKS enzymes (typically >1000 aa), protein modification involves kinases/ubiquitin ligases/etc., and L-isoleucine biosynthesis uses amino acid biosynthetic enzymes (threonine deaminase, dihydroxy-acid dehydratase, etc.)—none of which are P450s. Thus, identifying the P450 signature from the sequence and recalling the well-established link between P450s and steroid biosynthesis meaningfully distinguishes option B from the other three.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 heme-binding motif is extractable from the raw sequence. The association of P450 enzymes (particularly CYP51) with sterol/steroid biosynthesis is standard biochemistry knowledge transferable across all eukaryotic systems. The other three options are mechanistically incompatible with a P450 enzyme. A knowledgeable model can reach B without needing the specific UniProt record for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The P450 signature clearly eliminates options A (polyketide synthases are large multi-domain), C (protein modification enzymes are not P450s), and D (amino acid biosynthesis does not use P450s). Only steroid biosynthesis is a well-known P450-dependent pathway, making B the uniquely defensible choice.


### Important caveats

- The UniProt pathway annotation uses ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is by homology transfer rather than direct experimental demonstration for this exact protein.
- The protein is also annotated as 'Lanomycin biosynthesis cluster protein 1,' which could in principle suggest a polyketide-adjacent role, but the primary enzymatic function (sterol 14α-demethylase) and the pathway annotation both point to steroid biosynthesis.
- The P450 motif in this fungal sequence is somewhat degenerate (FGEGVVYDCP vs. canonical FGxGxRxCxG), but the heme-ligating Cys and overall P450 architecture remain identifiable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif: 'FGEGVVYDCP' in the central region, where the conserved Cys serves as the heme iron axial ligand, preceded by the FGxG pattern typical of the P450 I-helix. The ~540-aa length with an N-terminal hydrophobic membrane-anchoring segment is characteristic of fungal microsomal P450s. Among the four offered pathways, only steroid biosynthesis is classically and prominently P450-dependent (CYP51/sterol 14α-demethylase in fungi, CYP17/CYP21 in animals). Polyketide biosynthesis uses large multi-domain PKS enzymes (typically >1000 aa), protein modification involves kinases/ubiquitin ligases/etc., and L-isoleucine biosynthesis uses amino acid biosynthetic enzymes (threonine deaminase, dihydroxy-acid dehydratase, etc.)—none of which are P450s. Thus, identifying the P450 signature from the sequence and recalling the well-established link between P450s and steroid biosynthesis meaningfully distinguishes option B from the other three.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif is extractable from the raw sequence. The association of P450 enzymes (particularly CYP51) with sterol/steroid biosynthesis is standard biochemistry knowledge transferable across all eukaryotic systems. The other three options are mechanistically incompatible with a P450 enzyme. A knowledgeable model can reach B without needing the specific UniProt record for this exact protein."
  },
  "case_id": "pathway_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProtKB annotates P0DXV0 as Sterol 14-alpha demethylase (CYP51, EC 1.14.14.154) with pathway annotation 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250, similarity to Q4WNT5). The protein is also called 'Ergosterol biosynthesis protein' and 'Lanomycin biosynthesis cluster protein 1,' consistent with steroid/sterol biosynthesis. The answer B is supported by the database annotation, though the pathway assignment is by similarity transfer rather than direct experimental proof of the full pathway context."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is by homology transfer rather than direct experimental demonstration for this exact protein.",
    "The protein is also annotated as 'Lanomycin biosynthesis cluster protein 1,' which could in principle suggest a polyketide-adjacent role, but the primary enzymatic function (sterol 14α-demethylase) and the pathway annotation both point to steroid biosynthesis.",
    "The P450 motif in this fungal sequence is somewhat degenerate (FGEGVVYDCP vs. canonical FGxGxRxCxG), but the heme-ligating Cys and overall P450 architecture remain identifiable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 signature clearly eliminates options A (polyketide synthases are large multi-domain), C (protein modification enzymes are not P450s), and D (amino acid biosynthesis does not use P450s). Only steroid biosynthesis is a well-known P450-dependent pathway, making B the uniquely defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB annotates P0DXV0 as Sterol 14-alpha demethylase (CYP51, EC 1.14.14.154) with pathway annotation 'Steroid biosynthesis; sterol biosynthesis' (ECO:0000250, similarity to Q4WNT5). The protein is also called 'Ergosterol biosynthesis protein' and 'Lanomycin biosynthesis cluster protein 1,' consistent with steroid/sterol biosynthesis. The answer B is supported by the database annotation, though the pathway assignment is by similarity transfer rather than direct experimental proof of the full pathway context.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding motif: 'FGEGVVYDCP' in the central region, where the conserved Cys serves as the heme iron axial ligand, preceded by the FGxG pattern typical of the P450 I-helix. The ~540-aa length with an N-terminal hydrophobic membrane-anchoring segment is characteristic of fungal microsomal P450s. Among the four offered pathways, only steroid biosynthesis is classically and prominently P450-dependent (CYP51/sterol 14α-demethylase in fungi, CYP17/CYP21 in animals). Polyketide biosynthesis uses large multi-domain PKS enzymes (typically >1000 aa), protein modification involves kinases/ubiquitin ligases/etc., and L-isoleucine biosynthesis uses amino acid biosynthetic enzymes (threonine deaminase, dihydroxy-acid dehydratase, etc.)—none of which are P450s. Thus, identifying the P450 signature from the sequence and recalling the well-established link between P450s and steroid biosynthesis meaningfully distinguishes option B from the other three.",
    "missing_item_specific_fact": "",
    "reason": "The P450 heme-binding motif is extractable from the raw sequence. The association of P450 enzymes (particularly CYP51) with sterol/steroid biosynthesis is standard biochemistry knowledge transferable across all eukaryotic systems. The other three options are mechanistically incompatible with a P450 enzyme. A knowledgeable model can reach B without needing the specific UniProt record for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The P450 signature clearly eliminates options A (polyketide synthases are large multi-domain), C (protein modification enzymes are not P450s), and D (amino acid biosynthesis does not use P450s). Only steroid biosynthesis is a well-known P450-dependent pathway, making B the uniquely defensible choice."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is by homology transfer rather than direct experimental demonstration for this exact protein.",
    "The protein is also annotated as 'Lanomycin biosynthesis cluster protein 1,' which could in principle suggest a polyketide-adjacent role, but the primary enzymatic function (sterol 14α-demethylase) and the pathway annotation both point to steroid biosynthesis.",
    "The P450 motif in this fungal sequence is somewhat degenerate (FGEGVVYDCP vs. canonical FGxGxRxCxG), but the heme-ligating Cys and overall P450 architecture remain identifiable."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXV0",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "7892b58432fcc729eff0e7866dfac47e6055a778388a0efd41daa5ff7eb4bdd5",
  "selected_historical_version": {
    "accession": "P0DXV0",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LAN1_PYRDE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXV0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Helminthosporium dematioideum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Pleosporomycetidae\",\"Pleosporales\",\"Pleosporineae\",\"Pleosporaceae\",\"Pyrenophora\"],\"scientificName\":\"Pyrenophora dematioidea\",\"taxonId\":139229}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Lanomycin biosynthesis cluster protein 1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4WNT5\",\"source\":\"UniProtKB\"}],\"value\":\"Steroid biosynthesis; sterol biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/14",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TTI-1096\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:42.875207+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2b160263904b8131f1c8a75b02b0f4aff9b666aad2d76208024c4b4be635743d",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   LAN1_PYRDE              Reviewed;         540 AA.\nAC   P0DXV0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Sterol 14-alpha demethylase {ECO:0000303|PubMed:33857369};\nDE            EC=1.14.14.154 {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Cytochrome P450 monooxygenase {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Ergosterol biosynthesis protein {ECO:0000303|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 1 {ECO:0000303|PubMed:33857369};\nGN   Name=ORF1 {ECO:0000303|PubMed:33857369};\nOS   Pyrenophora dematioidea (Helminthosporium dematioideum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;\nOC   Pyrenophora.\nOX   NCBI_TaxID=139229;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=TTI-1096;\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Steroid biosynthesis; sterol biosynthesis.\nCC       {ECO:0000250|UniProtKB:Q4WNT5}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:45.056058+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 158-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e154cd9089aa6b8a42d60528a7ce84bec0c5a19fc8f6e92dd2125bb46b055be2",
  "url": "https://rest.uniprot.org/unisave/P0DXV0?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
