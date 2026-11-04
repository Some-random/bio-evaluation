# active_site_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0084.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 931 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMRRPPSQGRWSASHQKLLLAFAFILIPWLQLADAQQQPQQPQIRIHSQRGDAPLDKVADDANTRWYATHAAPDVHPEAKFDTVNRKQKQQSTASPQQHQKYRRAPYDYASKDKAQNRYAQHPIRESEKPNYVKVPNDASALATLAPAQPVRAPHTSRHHWPSSSAASGLASPQNARSLEDWEVEDFVLLATVDGDLYASDRKTGRHLWHLEVDQPVVETKHYRTNNSVLDDDYRPVDHYIWAVEPSRDGGLYVWIPDSGAGLVRTGFTMKHLVEELAPYAGDEPPVVYTGDKKTTMVTLDAATGRVLKWFGSSGSQVNEAESCLRPNAFDDRDTTECSSMGTITLGRTEYTVGIQRRDGRPIATLKYAEWGPNTFDSDLYQQYHASLDNHYITSQHDGRIYAFDKSQAENDLPLYTHKFSSPVARVFDVCRPWDANAGSNPELVVLPQPPIPALDESTVKMRSNSIFLNQTESGDWYALSGRAYPLILDAPVAQISRDDLWDMAHAFDSINPNKLSKALVGTHFLNPVKSTGYHQPPTLPAGALDEYYEDLENASNNAHAVTNTVPEEPTIITKVKALPQSAANSVIDFVSNPILIIFLIGSLIYNEKKLRRSYHRFRTHGTIKDVYPFFVIESEAGDESGDDKDGVFPSSPSPRSQPQDQNAEDHLSRHKVERNAGDQDKVKDNRSLHDVSDTLEPSNKTVEKTADVVKQVDVAGPDAPSTDSNGAAPEKKKKAHRGRRGGVKHRKGRPTDGSQSHENDPALTTVDEAVSNAKKLGDRPSLEPDVMTIYNDMQAVTGSVISMGNIEVDTDVELGMGSNGTVVFAGRFDGRDVAVKRMTIQFYDIATRETKLLRESDDHPNVIRYYSQVQRGDFLYIALERCAASLADVIEKPYAFGELAKAGQKDLPGVLYQITNGISHLHSLRIVHRDLKPQNILVNLDKDGRPRLLVSDFGLCKKLEDRQSSFGATTGRAAGTSGWRAPELLLDDDGQNPAAIDSSTHSGSHTILVGDPNSLSNGGRATRAIDIFSLGLVFFYVLTNGSHPFDCGDRYMREVNIRKGNYNLDPLDALGDFAYEAKDLIASMLQASPKARPDSREVMAHPFFWSPKKRLAFLCDVSDSLEKEVRDPPSPALVELERHAPEVIKGDFLKVLTRDFVESLGKQRKYTGNKLLDLLRALRNKRNHYEDMSDSLKRSVGSLPDGYLAYWTVKFPMLLLTCWNVVYNLEWEKTDRFREYYEPAGL

[Multiple Choices]
A. Position 218 (Proton donor)
B. Position 2056 (For beta-ketoacyl synthase 2 activity)
C. Position 1371 (For beta-ketoacyl synthase activity)
D. Position 931 (Proton acceptor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The supplied sequence matches the source sequence, and the UniProt annotation identifies position 931 as an active-site proton acceptor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein-kinase catalytic motifs, including HRDLK and DFG, which provide a transferable basis for identifying a catalytic acid/base residue in the kinase domain. The sequence is 1243 residues long, making positions 1371 and 2056 impossible; position 218 lies in the N-terminal region rather than the kinase catalytic domain. Thus position 931 is meaningfully distinguished among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level kinase motif recognition and the sequence length distinguish D from the offered alternatives without needing the exact protein's database record. The position-specific assignment remains an inference rather than proof of the experimental catalytic role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, only D names an in-range candidate in the catalytic domain; the other listed positions are either outside the sequence or in the N-terminal region.


### Important caveats

- The source annotation is computationally inferred from PROSITE-ProRule and should not be represented as direct experimental validation.
- The source sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase catalytic motifs, including HRDLK and DFG, which provide a transferable basis for identifying a catalytic acid/base residue in the kinase domain. The sequence is 1243 residues long, making positions 1371 and 2056 impossible; position 218 lies in the N-terminal region rather than the kinase catalytic domain. Thus position 931 is meaningfully distinguished among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level kinase motif recognition and the sequence length distinguish D from the offered alternatives without needing the exact protein's database record. The position-specific assignment remains an inference rather than proof of the experimental catalytic role."
  },
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, and the UniProt annotation identifies position 931 as an active-site proton acceptor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence."
  },
  "important_caveats": [
    "The source annotation is computationally inferred from PROSITE-ProRule and should not be represented as direct experimental validation.",
    "The source sequence matches the input, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D names an in-range candidate in the catalytic domain; the other listed positions are either outside the sequence or in the N-terminal region."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the source sequence, and the UniProt annotation identifies position 931 as an active-site proton acceptor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase catalytic motifs, including HRDLK and DFG, which provide a transferable basis for identifying a catalytic acid/base residue in the kinase domain. The sequence is 1243 residues long, making positions 1371 and 2056 impossible; position 218 lies in the N-terminal region rather than the kinase catalytic domain. Thus position 931 is meaningfully distinguished among these choices.",
    "missing_item_specific_fact": "",
    "reason": "Family-level kinase motif recognition and the sequence length distinguish D from the offered alternatives without needing the exact protein's database record. The position-specific assignment remains an inference rather than proof of the experimental catalytic role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, only D names an in-range candidate in the catalytic domain; the other listed positions are either outside the sequence or in the N-terminal region."
  },
  "important_caveats": [
    "The source annotation is computationally inferred from PROSITE-ProRule and should not be represented as direct experimental validation.",
    "The source sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly lists position 931 as 'Proton acceptor' active site, annotated via PROSITE-ProRule PRU00159 (protein kinase active site). The sequence contains clear protein kinase motifs: the glycine-rich loop (GxGxxG: 'GSSGSQ' near position 815-823), the HRD catalytic motif ('HRD' in 'RIVHRDLKPQ'), and the DFG motif ('DFG' in 'SDFGLCKK'). The aspartate in the HRD motif is the well-established catalytic proton acceptor in all protein kinases. The annotation is computational (PROSITE-ProRule) but represents a highly conserved family-level feature with strong mechanistic support across the kinase superfamily.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [C12](#evidence-c12), [C13](#evidence-c13).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable protein kinase motifs: (1) the glycine-rich loop 'GSSGSQV' (GxGxxG) near the N-terminal end of the kinase domain, (2) the HRD motif 'HRD' in 'RIVHRDLKPQ' containing the catalytic aspartate, and (3) the DFG motif 'DFG' in 'SDFGLCKK'. These three motifs together are diagnostic of the protein kinase fold. From general kinase biochemistry learned across hundreds of kinases, the aspartate in the HRD motif functions as a proton acceptor (abstracting the proton from the substrate hydroxyl during phosphotransfer). Options B (position 2056) and C (position 1371) are immediately eliminated because the sequence is only 1243 residues long. Option A (position 218, 'Proton donor') is inconsistent with kinase catalytic mechanism—the catalytic residue in the kinase active site is a proton acceptor, not a proton donor. Position 218 falls in the N-terminal region (ER luminal/sensor domain), far from the kinase catalytic center. Option D (position 931, 'Proton acceptor') matches both the location within the kinase domain and the correct mechanistic role of the HRD aspartate. A knowledgeable model can identify the HRD motif, recognize the D as the catalytic aspartate, and confirm it falls near position 931 by counting from the recognizable kinase-domain landmarks.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The kinase family motifs (GxGxxG, HRD, DFG) are directly visible in the supplied sequence. The catalytic role of the HRD aspartate as a proton acceptor is a fundamental, transferable feature across the entire protein kinase superfamily. Options B and C are trivially eliminated by sequence length. The distinction between A (proton donor at position 218) and D (proton acceptor at position 931) is resolved by standard kinase mechanism knowledge: the catalytic residue accepts a proton, and it resides in the kinase domain (C-terminal region), not the N-terminal sensor region. No target-specific memorization is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C reference positions (2056, 1371) that exceed the 1243-residue sequence length, making them clearly invalid. Option A mislabels the mechanistic role (proton donor vs. acceptor) and places the residue outside the kinase domain. Only D is consistent with both the kinase family mechanism and the sequence context.


### Important caveats

- The UniProt annotation for position 931 is based on PROSITE-ProRule (computational/protein family rule), not direct experimental mutagenesis for this specific protein. However, the HRD aspartate proton-acceptor role is one of the most universally conserved mechanistic features across all protein kinases.
- Exact position counting to 931 requires careful traversal of 931 residues; however, the model can use the kinase domain landmarks (HRD, DFG, GxGxxG) to confirm the catalytic aspartate falls in the correct region and is consistent with position 931.
- The protein is annotated as a dual-function kinase/endoribonuclease, but the question and options focus on the kinase active site specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase motifs: (1) the glycine-rich loop 'GSSGSQV' (GxGxxG) near the N-terminal end of the kinase domain, (2) the HRD motif 'HRD' in 'RIVHRDLKPQ' containing the catalytic aspartate, and (3) the DFG motif 'DFG' in 'SDFGLCKK'. These three motifs together are diagnostic of the protein kinase fold. From general kinase biochemistry learned across hundreds of kinases, the aspartate in the HRD motif functions as a proton acceptor (abstracting the proton from the substrate hydroxyl during phosphotransfer). Options B (position 2056) and C (position 1371) are immediately eliminated because the sequence is only 1243 residues long. Option A (position 218, 'Proton donor') is inconsistent with kinase catalytic mechanism—the catalytic residue in the kinase active site is a proton acceptor, not a proton donor. Position 218 falls in the N-terminal region (ER luminal/sensor domain), far from the kinase catalytic center. Option D (position 931, 'Proton acceptor') matches both the location within the kinase domain and the correct mechanistic role of the HRD aspartate. A knowledgeable model can identify the HRD motif, recognize the D as the catalytic aspartate, and confirm it falls near position 931 by counting from the recognizable kinase-domain landmarks.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The kinase family motifs (GxGxxG, HRD, DFG) are directly visible in the supplied sequence. The catalytic role of the HRD aspartate as a proton acceptor is a fundamental, transferable feature across the entire protein kinase superfamily. Options B and C are trivially eliminated by sequence length. The distinction between A (proton donor at position 218) and D (proton acceptor at position 931) is resolved by standard kinase mechanism knowledge: the catalytic residue accepts a proton, and it resides in the kinase domain (C-terminal region), not the N-terminal sensor region. No target-specific memorization is required."
  },
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "C12",
      "C13"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly lists position 931 as 'Proton acceptor' active site, annotated via PROSITE-ProRule PRU00159 (protein kinase active site). The sequence contains clear protein kinase motifs: the glycine-rich loop (GxGxxG: 'GSSGSQ' near position 815-823), the HRD catalytic motif ('HRD' in 'RIVHRDLKPQ'), and the DFG motif ('DFG' in 'SDFGLCKK'). The aspartate in the HRD motif is the well-established catalytic proton acceptor in all protein kinases. The annotation is computational (PROSITE-ProRule) but represents a highly conserved family-level feature with strong mechanistic support across the kinase superfamily."
  },
  "important_caveats": [
    "The UniProt annotation for position 931 is based on PROSITE-ProRule (computational/protein family rule), not direct experimental mutagenesis for this specific protein. However, the HRD aspartate proton-acceptor role is one of the most universally conserved mechanistic features across all protein kinases.",
    "Exact position counting to 931 requires careful traversal of 931 residues; however, the model can use the kinase domain landmarks (HRD, DFG, GxGxxG) to confirm the catalytic aspartate falls in the correct region and is consistent with position 931.",
    "The protein is annotated as a dual-function kinase/endoribonuclease, but the question and options focus on the kinase active site specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C reference positions (2056, 1371) that exceed the 1243-residue sequence length, making them clearly invalid. Option A mislabels the mechanistic role (proton donor vs. acceptor) and places the residue outside the kinase domain. Only D is consistent with both the kinase family mechanism and the sequence context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly lists position 931 as 'Proton acceptor' active site, annotated via PROSITE-ProRule PRU00159 (protein kinase active site). The sequence contains clear protein kinase motifs: the glycine-rich loop (GxGxxG: 'GSSGSQ' near position 815-823), the HRD catalytic motif ('HRD' in 'RIVHRDLKPQ'), and the DFG motif ('DFG' in 'SDFGLCKK'). The aspartate in the HRD motif is the well-established catalytic proton acceptor in all protein kinases. The annotation is computational (PROSITE-ProRule) but represents a highly conserved family-level feature with strong mechanistic support across the kinase superfamily.",
    "evidence_ids": ["C5", "H3", "C6", "C12", "C13"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable protein kinase motifs: (1) the glycine-rich loop 'GSSGSQV' (GxGxxG) near the N-terminal end of the kinase domain, (2) the HRD motif 'HRD' in 'RIVHRDLKPQ' containing the catalytic aspartate, and (3) the DFG motif 'DFG' in 'SDFGLCKK'. These three motifs together are diagnostic of the protein kinase fold. From general kinase biochemistry learned across hundreds of kinases, the aspartate in the HRD motif functions as a proton acceptor (abstracting the proton from the substrate hydroxyl during phosphotransfer). Options B (position 2056) and C (position 1371) are immediately eliminated because the sequence is only 1243 residues long. Option A (position 218, 'Proton donor') is inconsistent with kinase catalytic mechanism—the catalytic residue in the kinase active site is a proton acceptor, not a proton donor. Position 218 falls in the N-terminal region (ER luminal/sensor domain), far from the kinase catalytic center. Option D (position 931, 'Proton acceptor') matches both the location within the kinase domain and the correct mechanistic role of the HRD aspartate. A knowledgeable model can identify the HRD motif, recognize the D as the catalytic aspartate, and confirm it falls near position 931 by counting from the recognizable kinase-domain landmarks.",
    "missing_item_specific_fact": "",
    "reason": "The kinase family motifs (GxGxxG, HRD, DFG) are directly visible in the supplied sequence. The catalytic role of the HRD aspartate as a proton acceptor is a fundamental, transferable feature across the entire protein kinase superfamily. Options B and C are trivially eliminated by sequence length. The distinction between A (proton donor at position 218) and D (proton acceptor at position 931) is resolved by standard kinase mechanism knowledge: the catalytic residue accepts a proton, and it resides in the kinase domain (C-terminal region), not the N-terminal sensor region. No target-specific memorization is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C reference positions (2056, 1371) that exceed the 1243-residue sequence length, making them clearly invalid. Option A mislabels the mechanistic role (proton donor vs. acceptor) and places the residue outside the kinase domain. Only D is consistent with both the kinase family mechanism and the sequence context."
  },
  "important_caveats": [
    "The UniProt annotation for position 931 is based on PROSITE-ProRule (computational/protein family rule), not direct experimental mutagenesis for this specific protein. However, the HRD aspartate proton-acceptor role is one of the most universally conserved mechanistic features across all protein kinases.",
    "Exact position counting to 931 requires careful traversal of 931 residues; however, the model can use the kinase domain landmarks (HRD, DFG, GxGxxG) to confirm the catalytic aspartate falls in the correct region and is consistent with position 931.",
    "The protein is annotated as a dual-function kinase/endoribonuclease, but the question and options focus on the kinase active site specifically."
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
  "benchmark_sequence_length": 1243,
  "benchmark_sequence_sha256": "feffa4d520718ffc254a021012992c4dbd5b0efeb341a8fa389e84ac12a28a13",
  "current_entry_audit": {
    "entryVersion": 79,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-10-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1243,
  "current_source_sequence_sha256": "feffa4d520718ffc254a021012992c4dbd5b0efeb341a8fa389e84ac12a28a13",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 77,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G0RBE3",
  "selected_historical_entry_version": 77,
  "selected_historical_record_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "selected_historical_source_sequence_length": 1243,
  "selected_historical_source_sequence_sha256": "feffa4d520718ffc254a021012992c4dbd5b0efeb341a8fa389e84ac12a28a13",
  "selected_historical_version": {
    "accession": "G0RBE3",
    "database": "Swiss-Prot",
    "entryVersion": 77,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "IRE1_HYPJQ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G0RBE3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":79,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-10-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008984\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Trichoderma\"],\"scientificName\":\"Trichoderma reesei (strain QM6a)\",\"synonyms\":[\"Hypocrea jecorina\"],\"taxonId\":431241}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"value\":\"Endoplasmic reticulum-to-nucleus signaling 1\"}}],\"flag\":\"Precursor\",\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.11.1\"}],\"fullName\":{\"value\":\"Serine/threonine-protein kinase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"value\":\"3.1.26.-\"}],\"fullName\":{\"value\":\"Endoribonuclease\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"value\":\"Serine/threonine-protein kinase/endoribonuclease IRE1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":931},\"start\":{\"modifier\":\"EXACT\",\"value\":931}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":823},\"start\":{\"modifier\":\"EXACT\",\"value\":815}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:456216\",\"name\":\"ADP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":819},\"start\":{\"modifier\":\"EXACT\",\"value\":819}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:456216\",\"name\":\"ADP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":837},\"start\":{\"modifier\":\"EXACT\",\"value\":837}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00159\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:30616\",\"name\":\"ATP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":837},\"start\":{\"modifier\":\"EXACT\",\"value\":837}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:456216\",\"name\":\"ADP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":881},\"start\":{\"modifier\":\"EXACT\",\"value\":881}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:456216\",\"name\":\"ADP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":883},\"start\":{\"modifier\":\"EXACT\",\"value\":883}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":936},\"start\":{\"modifier\":\"EXACT\",\"value\":936}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RBE3.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P32361\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:18420\",\"name\":\"Mg(2+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":953},\"start\":{\"modifier\":\"EXACT\",\"value\":953}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/24",
  "retrieved_utc": "2026-11-02T04:28:20.334411+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2123823e76a12215e4833692b5a5e04ddd8bd1e8862b8c3bf48b9e60228a41d5",
  "url": "https://rest.uniprot.org/uniprotkb/G0RBE3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H1",
  "excerpt": "ID   IRE1_HYPJQ              Reviewed;        1243 AA.\nAC   G0RBE3; Q7Z8F3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-OCT-2011, sequence version 1.\nDT   28-JAN-2026, entry version 77.\nDE   RecName: Full=Serine/threonine-protein kinase/endoribonuclease IRE1 {ECO:0000250|UniProtKB:P32361};\nDE   AltName: Full=Endoplasmic reticulum-to-nucleus signaling 1 {ECO:0000250|UniProtKB:P32361};\nDE   Includes:\nDE     RecName: Full=Serine/threonine-protein kinase;\nDE              EC=2.7.11.1 {ECO:0000250|UniProtKB:P32361};\nDE   Includes:\nDE     RecName: Full=Endoribonuclease;\nDE              EC=3.1.26.- {ECO:0000250|UniProtKB:P32361};\nDE   Flags: Precursor;\nGN   Name=IRE1 {ECO:0000303|PubMed:15480788};\nGN   ORFNames=TRIREDRAFT_45242 {ECO:0000312|EMBL:EGR51316.1};\nOS   Hypocrea jecorina (strain QM6a) (Trichoderma reesei).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.\nOX   NCBI_TaxID=431241 {ECO:0000312|Proteomes:UP000008984};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-20",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAP92915.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], AND FUNCTION.\nRC   STRAIN=QM6a {ECO:0000303|PubMed:15480788};\nRX   PubMed=15480788; DOI=10.1007/s00438-004-1070-0;\nRA   Valkonen M., Penttila M., Saloheimo M.;\nRT   \"The ire1 and ptc2 genes involved in the unfolded protein response pathway\nRT   in the filamentous fungus Trichoderma reesei.\";\nRL   Mol. Genet. Genomics 272:443-451(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        931\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         815..823\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-196",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         819\nFT                   /ligand=\"ADP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:456216\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 197-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         837\nFT                   /ligand=\"ADP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:456216\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 201-204",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         837\nFT                   /ligand=\"ATP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:30616\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 205-208",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         881\nFT                   /ligand=\"ADP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:456216\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 209-212",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         883\nFT                   /ligand=\"ADP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:456216\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 213-216",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         936\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 217-220",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77)

```json
{
  "entry_version": 77,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         953\nFT                   /ligand=\"Mg(2+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:18420\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P32361\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:23.459878+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 221-224",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5d5317f993412ba26161188a84e8b9080ba3b898a6088db1ed2fb791ab4c2a",
  "url": "https://rest.uniprot.org/unisave/G0RBE3?format=txt&versions=77"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
