# GO_cellular_component_0055

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0055.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **C** — mitochondrial membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSFYNKCFTNKLISAHSLFCQHVSTLKNNKKECFEDVKRSNRISDEFYSSFLYHSYIENLKSTKEYVYFIYLQDIYYNINIFKNKGRLYISNNGLCNDKLKDNNNNNNINSNNFGNSYNAYTKKKSFYHSFNDLNEAKEIRKKRKNEKSEKNIVEYLLCNIINPNENYHIQNIYNHNLNNNVSIEIHKKNDSVMYHYNNEKKTKTSKMTTDIKLKQINNVYIKYVPYKNKIITLACPNKYYPTLYRYFSSHTNKKEDAEENDKNKNININNVDNRYKEDFMYGCENKNDSEKHKKTTNNNFGDEFEKLKVKELDKILNKLEMLYDNKNNKMNINVKILGYIFKNFLLKNKELKRKIFCSLFFLLCSKMAIIYTPILLSTFIENVNLQKSLSNNIDIYSTNKSSVLLLCAYVFSRVLSSTMNELRNSVFSNISQKISTFVSKLFFYKIHNLNLTYILSKKNGELSFIFNRGCKSITNLLNVMVFQIIPIIIEFILYLYILTYKIHYTVSLVTCFNMFLYVLFTTLITKRRTIIRKHMNKAEQNTFNIFLDSIQNVEQVKYYTNEIHELKKFIKEQKKYEKEAINVQKSLSFLNFGQQIILNTNLFLCMYLTYLNIANDIFPFSYLILVNTLLFQLAMPLNMFGTIYRETKLSLVDIESMIKILVKKIKSPDYGNQMLIKNGNIKFENVYFKYPLNEDINGLEQNYQAKEKDPNIINNINNINNINNINNINNINSINNIYTFESNVKNISSTNMITSSINKLKKWYLDKVKDNKKNVQYNNNDVKKTNPNITKNLNKEIKENINTHLKNHKIINNSPNYNNNNYLFQNFTCNIENGEKVAIIGKSGSGKSSLIKLLLKFYEVNSGNIYIDNKNIDDIDLYTLRKNISVVPQDTILFNNTISYNIKYGNFQCTDKQMIQASIKAELHDKIMKMENKYDTIVGERGTKLSIGEKQRICIARCFLKDSKIIVLDEHASNLDNENKKAIEKALTKLCMGKTTFIITHVMENLKHMDKIIFFCGKNIYVGSHKNLMDDNHFYREYYDSKNNKML

[Multiple Choices]
A. inclusion body
B. ATP-binding cassette (ABC) transporter complex
C. mitochondrial membrane
D. transcription regulator complex
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

> The sequence-matched UniProt record annotates the protein to the mitochondrion membrane, with the location linked to a PubMed-supported assertion. The GO mitochondrial-membrane annotation is computationally transferred, so it is supporting annotation rather than independent experimental evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple hydrophobic membrane-spanning regions and a C-terminal ABC nucleotide-binding domain with a Walker A-like motif, supporting an ABC transporter rather than an inclusion-body protein or transcription-regulator complex. Its ATM1-like transporter-family features provide a transferable basis for favoring mitochondrial membrane localization. Choice B describes a transporter complex, whereas C names the cellular membrane location.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the transporter family and its usual mitochondrial membrane association is a credible inference from sequence features and knowledge transferable from related proteins; exact target annotation is not necessary to distinguish the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein appears to be an ABC transporter, the complex option does not specify its cellular location. The mitochondrial membrane choice more directly answers the localization question.


### Important caveats

- The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The UniProt location assertion is linked to a publication; the supplied excerpts do not independently establish the experimental methods or results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and a C-terminal ABC nucleotide-binding domain with a Walker A-like motif, supporting an ABC transporter rather than an inclusion-body protein or transcription-regulator complex. Its ATM1-like transporter-family features provide a transferable basis for favoring mitochondrial membrane localization. Choice B describes a transporter complex, whereas C names the cellular membrane location.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the transporter family and its usual mitochondrial membrane association is a credible inference from sequence features and knowledge transferable from related proteins; exact target annotation is not necessary to distinguish the choices."
  },
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrion membrane, with the location linked to a PubMed-supported assertion. The GO mitochondrial-membrane annotation is computationally transferred, so it is supporting annotation rather than independent experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The UniProt location assertion is linked to a publication; the supplied excerpts do not independently establish the experimental methods or results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein appears to be an ABC transporter, the complex option does not specify its cellular location. The mitochondrial membrane choice more directly answers the localization question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the mitochondrion membrane, with the location linked to a PubMed-supported assertion. The GO mitochondrial-membrane annotation is computationally transferred, so it is supporting annotation rather than independent experimental evidence.",
    "evidence_ids": ["C5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple hydrophobic membrane-spanning regions and a C-terminal ABC nucleotide-binding domain with a Walker A-like motif, supporting an ABC transporter rather than an inclusion-body protein or transcription-regulator complex. Its ATM1-like transporter-family features provide a transferable basis for favoring mitochondrial membrane localization. Choice B describes a transporter complex, whereas C names the cellular membrane location.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the transporter family and its usual mitochondrial membrane association is a credible inference from sequence features and knowledge transferable from related proteins; exact target annotation is not necessary to distinguish the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein appears to be an ABC transporter, the complex option does not specify its cellular location. The mitochondrial membrane choice more directly answers the localization question."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The UniProt location assertion is linked to a publication; the supplied excerpts do not independently establish the experimental methods or results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q8IDH9, ATM1_PLAF7) annotates the protein's subcellular location as 'Mitochondrion membrane' with experimental evidence (ECO:0000305|PubMed:39348385, a 2024 PLoS Pathogens paper on ATM1 function). The GO term GO:0031966 (mitochondrial membrane) is assigned with IEA:UniProtKB-SubCell evidence. The protein is described as a multi-pass membrane protein in the mitochondrion membrane. Option C text 'mitochondrial membrane' matches GO:0031966 exactly.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains clear ABC transporter signature motifs: Walker A (GKSGSGKS), Walker B (DEHASN), and ABC signature (LSGEKQ), plus a multi-pass transmembrane domain (the hydrophobic stretch ~residues 250-450). This identifies the protein as an ABC transporter. The critical distinction between B and C relies on transferable family-level knowledge: (1) The GO term 'ABC transporter complex' (GO:0043190) is explicitly defined as a multi-subunit complex forming a pore through the PLASMA MEMBRANE, not a mitochondrial transporter. (2) Mitochondrial ABC transporters (ATM1/ABCB7/ABCB8 family) are a well-characterized subfamily found in the inner mitochondrial membrane across eukaryotes (yeast ATM1, human ABCB7/ABCB8). (3) The single-polypeptide architecture with both TM domains and nucleotide-binding domains is characteristic of mitochondrial half/full ABC transporters, not the multi-subunit plasma membrane ABC complexes described by GO:0043190. (4) The N-terminal region contains basic and hydroxylated residues consistent with a mitochondrial targeting signal. A knowledgeable model recognizing the ABC transporter family and knowing that mitochondrial ABC transporters (ATM1 family) reside in the inner mitochondrial membrane—not in the plasma membrane 'ABC transporter complex'—can meaningfully distinguish C from B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction between options B and C is achievable through transferable knowledge: the GO definition of 'ABC transporter complex' specifies plasma membrane multi-subunit assemblies, while mitochondrial ABC transporters (ATM1/ABCB7 family) are a well-known subfamily localized to the inner mitochondrial membrane. The sequence's single-polypeptide TM+NBD architecture and N-terminal targeting-like region support mitochondrial membrane over plasma membrane complex. This is legitimate family-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B (ABC transporter complex) is a tempting distractor since the protein IS an ABC transporter, but the GO term GO:0043190 specifically refers to plasma membrane multi-subunit complexes, not mitochondrial membrane proteins. The GO definition and the well-known ATM1/ABCB7 mitochondrial subfamily make C clearly more appropriate than B. Options A (inclusion body) and D (transcription regulator complex) are clearly incompatible with a membrane-transport protein containing ABC motifs.


### Important caveats

- The protein is from Plasmodium falciparum, but organism identity is not provided to the model. The AT-rich N-terminal sequence is unusual but the ABC transporter motifs are unambiguous.
- The 2024 experimental evidence (PubMed:39348385) post-dates many earlier annotations; the original benchmark may have relied on computational prediction or GeneDB annotation.
- Option B could be tempting to a model that recognizes ABC transporter motifs without knowing the specific GO term scope (plasma membrane complex vs. mitochondrial membrane protein).
- The GO annotation for mitochondrial membrane (GO:0031966) uses IEA:UniProtKB-SubCell (inferred from annotation), while the experimental evidence is ECO:0000305 from the 2024 paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains clear ABC transporter signature motifs: Walker A (GKSGSGKS), Walker B (DEHASN), and ABC signature (LSGEKQ), plus a multi-pass transmembrane domain (the hydrophobic stretch ~residues 250-450). This identifies the protein as an ABC transporter. The critical distinction between B and C relies on transferable family-level knowledge: (1) The GO term 'ABC transporter complex' (GO:0043190) is explicitly defined as a multi-subunit complex forming a pore through the PLASMA MEMBRANE, not a mitochondrial transporter. (2) Mitochondrial ABC transporters (ATM1/ABCB7/ABCB8 family) are a well-characterized subfamily found in the inner mitochondrial membrane across eukaryotes (yeast ATM1, human ABCB7/ABCB8). (3) The single-polypeptide architecture with both TM domains and nucleotide-binding domains is characteristic of mitochondrial half/full ABC transporters, not the multi-subunit plasma membrane ABC complexes described by GO:0043190. (4) The N-terminal region contains basic and hydroxylated residues consistent with a mitochondrial targeting signal. A knowledgeable model recognizing the ABC transporter family and knowing that mitochondrial ABC transporters (ATM1 family) reside in the inner mitochondrial membrane—not in the plasma membrane 'ABC transporter complex'—can meaningfully distinguish C from B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction between options B and C is achievable through transferable knowledge: the GO definition of 'ABC transporter complex' specifies plasma membrane multi-subunit assemblies, while mitochondrial ABC transporters (ATM1/ABCB7 family) are a well-known subfamily localized to the inner mitochondrial membrane. The sequence's single-polypeptide TM+NBD architecture and N-terminal targeting-like region support mitochondrial membrane over plasma membrane complex. This is legitimate family-level inference from other proteins."
  },
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q8IDH9, ATM1_PLAF7) annotates the protein's subcellular location as 'Mitochondrion membrane' with experimental evidence (ECO:0000305|PubMed:39348385, a 2024 PLoS Pathogens paper on ATM1 function). The GO term GO:0031966 (mitochondrial membrane) is assigned with IEA:UniProtKB-SubCell evidence. The protein is described as a multi-pass membrane protein in the mitochondrion membrane. Option C text 'mitochondrial membrane' matches GO:0031966 exactly."
  },
  "important_caveats": [
    "The protein is from Plasmodium falciparum, but organism identity is not provided to the model. The AT-rich N-terminal sequence is unusual but the ABC transporter motifs are unambiguous.",
    "The 2024 experimental evidence (PubMed:39348385) post-dates many earlier annotations; the original benchmark may have relied on computational prediction or GeneDB annotation.",
    "Option B could be tempting to a model that recognizes ABC transporter motifs without knowing the specific GO term scope (plasma membrane complex vs. mitochondrial membrane protein).",
    "The GO annotation for mitochondrial membrane (GO:0031966) uses IEA:UniProtKB-SubCell (inferred from annotation), while the experimental evidence is ECO:0000305 from the 2024 paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (ABC transporter complex) is a tempting distractor since the protein IS an ABC transporter, but the GO term GO:0043190 specifically refers to plasma membrane multi-subunit complexes, not mitochondrial membrane proteins. The GO definition and the well-known ATM1/ABCB7 mitochondrial subfamily make C clearly more appropriate than B. Options A (inclusion body) and D (transcription regulator complex) are clearly incompatible with a membrane-transport protein containing ABC motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q8IDH9, ATM1_PLAF7) annotates the protein's subcellular location as 'Mitochondrion membrane' with experimental evidence (ECO:0000305|PubMed:39348385, a 2024 PLoS Pathogens paper on ATM1 function). The GO term GO:0031966 (mitochondrial membrane) is assigned with IEA:UniProtKB-SubCell evidence. The protein is described as a multi-pass membrane protein in the mitochondrion membrane. Option C text 'mitochondrial membrane' matches GO:0031966 exactly.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains clear ABC transporter signature motifs: Walker A (GKSGSGKS), Walker B (DEHASN), and ABC signature (LSGEKQ), plus a multi-pass transmembrane domain (the hydrophobic stretch ~residues 250-450). This identifies the protein as an ABC transporter. The critical distinction between B and C relies on transferable family-level knowledge: (1) The GO term 'ABC transporter complex' (GO:0043190) is explicitly defined as a multi-subunit complex forming a pore through the PLASMA MEMBRANE, not a mitochondrial transporter. (2) Mitochondrial ABC transporters (ATM1/ABCB7/ABCB8 family) are a well-characterized subfamily found in the inner mitochondrial membrane across eukaryotes (yeast ATM1, human ABCB7/ABCB8). (3) The single-polypeptide architecture with both TM domains and nucleotide-binding domains is characteristic of mitochondrial half/full ABC transporters, not the multi-subunit plasma membrane ABC complexes described by GO:0043190. (4) The N-terminal region contains basic and hydroxylated residues consistent with a mitochondrial targeting signal. A knowledgeable model recognizing the ABC transporter family and knowing that mitochondrial ABC transporters (ATM1 family) reside in the inner mitochondrial membrane—not in the plasma membrane 'ABC transporter complex'—can meaningfully distinguish C from B.",
    "missing_item_specific_fact": "",
    "reason": "The distinction between options B and C is achievable through transferable knowledge: the GO definition of 'ABC transporter complex' specifies plasma membrane multi-subunit assemblies, while mitochondrial ABC transporters (ATM1/ABCB7 family) are a well-known subfamily localized to the inner mitochondrial membrane. The sequence's single-polypeptide TM+NBD architecture and N-terminal targeting-like region support mitochondrial membrane over plasma membrane complex. This is legitimate family-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (ABC transporter complex) is a tempting distractor since the protein IS an ABC transporter, but the GO term GO:0043190 specifically refers to plasma membrane multi-subunit complexes, not mitochondrial membrane proteins. The GO definition and the well-known ATM1/ABCB7 mitochondrial subfamily make C clearly more appropriate than B. Options A (inclusion body) and D (transcription regulator complex) are clearly incompatible with a membrane-transport protein containing ABC motifs."
  },
  "important_caveats": [
    "The protein is from Plasmodium falciparum, but organism identity is not provided to the model. The AT-rich N-terminal sequence is unusual but the ABC transporter motifs are unambiguous.",
    "The 2024 experimental evidence (PubMed:39348385) post-dates many earlier annotations; the original benchmark may have relied on computational prediction or GeneDB annotation.",
    "Option B could be tempting to a model that recognizes ABC transporter motifs without knowing the specific GO term scope (plasma membrane complex vs. mitochondrial membrane protein).",
    "The GO annotation for mitochondrial membrane (GO:0031966) uses IEA:UniProtKB-SubCell (inferred from annotation), while the experimental evidence is ECO:0000305 from the 2024 paper."
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
  "benchmark_sequence_length": 1049,
  "benchmark_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "current_entry_audit": {
    "entryVersion": 150,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1049,
  "current_source_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 148,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8IDH9",
  "selected_historical_entry_version": 148,
  "selected_historical_record_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "selected_historical_source_sequence_length": 1049,
  "selected_historical_source_sequence_sha256": "0e938c20743637e45d04227baafe55014e41bc01995ba516bab1cce5bc703a70",
  "selected_historical_version": {
    "accession": "Q8IDH9",
    "database": "Swiss-Prot",
    "entryVersion": 148,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ATM1_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8IDH9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":150,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAD52642.1\",\"source\":\"EMBL\"}],\"value\":\"ABC transporter B family member 6, putative\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfABCB6\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfMDR6\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"7.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ABC transporter ATM1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"value\":\"PfATM1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39348385\",\"source\":\"PubMed\"}],\"id\":\"SL-0171\",\"value\":\"Mitochondrion membrane\"},\"topology\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"id\":\"SL-9909\",\"value\":\"Multi-pass membrane protein\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"12368867\",\"source\":\"PubMed\"}],\"id\":\"GO:0016020\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:GeneDB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/22",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0031966\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:mitochondrial membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-SubCell\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/23",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Hall N.\",\"Pain A.\",\"Berriman M.\",\"Churcher C.M.\",\"Harris B.\",\"Harris D.\",\"Mungall K.L.\",\"Bowman S.\",\"Atkin R.\",\"Baker S.\",\"Barron A.\",\"Brooks K.\",\"Buckee C.O.\",\"Burrows C.\",\"Cherevach I.\",\"Chillingworth C.\",\"Chillingworth T.\",\"Christodoulou Z.\",\"Clark L.\",\"Clark R.\",\"Corton C.\",\"Cronin A.\",\"Davies R.M.\",\"Davis P.\",\"Dear P.\",\"Dearden F.\",\"Doggett J.\",\"Feltwell T.\",\"Goble A.\",\"Goodhead I.\",\"Gwilliam R.\",\"Hamlin N.\",\"Hance Z.\",\"Harper D.\",\"Hauser H.\",\"Hornsby T.\",\"Holroyd S.\",\"Horrocks P.\",\"Humphray S.\",\"Jagels K.\",\"James K.D.\",\"Johnson D.\",\"Kerhornou A.\",\"Knights A.\",\"Konfortov B.\",\"Kyes S.\",\"Larke N.\",\"Lawson D.\",\"Lennard N.\",\"Line A.\",\"Maddison M.\",\"Mclean J.\",\"Mooney P.\",\"Moule S.\",\"Murphy L.\",\"Oliver K.\",\"Ormond D.\",\"Price C.\",\"Quail M.A.\",\"Rabbinowitsch E.\",\"Rajandream M.A.\",\"Rutter S.\",\"Rutherford K.M.\",\"Sanders M.\",\"Simmonds M.\",\"Seeger K.\",\"Sharp S.\",\"Smith R.\",\"Squares R.\",\"Squares S.\",\"Stevens K.\",\"Taylor K.\",\"Tivey A.\",\"Unwin L.\",\"Whitehead S.\",\"Woodward J.R.\",\"Sulston J.E.\",\"Craig A.\",\"Newbold C.\",\"Barrell B.G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12368867\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature01095\"}],\"citationType\":\"journal article\",\"firstPage\":\"527\",\"id\":\"12368867\",\"journal\":\"Nature\",\"lastPage\":\"531\",\"publicationDate\":\"2002\",\"title\":\"Sequence of Plasmodium falciparum chromosomes 1, 3-9 and 13.\",\"volume\":\"419\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"type\":\"STRAIN\",\"value\":\"3D7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8IDH9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Shrivastava D.\",\"Abboud E.\",\"Ramchandra J.P.\",\"Jha A.\",\"Marq J.B.\",\"Chaurasia A.\",\"Mitra K.\",\"Sadik M.\",\"Siddiqi M.I.\",\"Soldati-Favre D.\",\"Kloehn J.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39348385\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.ppat.1012593\"}],\"citationType\":\"journal article\",\"firstPage\":\"e1012593\",\"id\":\"39348385\",\"journal\":\"PLoS Pathog.\",\"lastPage\":\"e1012593\",\"publicationDate\":\"2024\",\"title\":\"ATM1, an essential conserved transporter in Apicomplexa, bridges mitochondrial and cytosolic [Fe-S] biogenesis.\",\"volume\":\"20\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF ARG-534 AND GLU-972\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:32:08.625514+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e8f2bda44f575e480dae54a87949611a9f660eeebc858da9b702318946aeef67",
  "url": "https://rest.uniprot.org/uniprotkb/Q8IDH9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "entry_version": 148,
  "evidence_id": "H1",
  "excerpt": "ID   ATM1_PLAF7              Reviewed;        1049 AA.\nAC   Q8IDH9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 148.\nDE   RecName: Full=ABC transporter ATM1 {ECO:0000305};\nDE            Short=PfATM1 {ECO:0000303|PubMed:39348385};\nDE            EC=7.-.-.- {ECO:0000269|PubMed:39348385};\nDE   AltName: Full=ABC transporter B family member 6, putative {ECO:0000312|EMBL:CAD52642.1};\nDE            Short=PfABCB6 {ECO:0000303|PubMed:39348385};\nDE   AltName: Full=PfMDR6 {ECO:0000303|PubMed:39348385};\nDE   Flags: Precursor;\nGN   Name=ABCB6 {ECO:0000305};\nGN   ORFNames=PF3D7_1352100 {ECO:0000312|EMBL:CAD52642.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "entry_version": 148,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, INTERACTION WITH ISCU; ISCA2; MHCF101/CFD1 AND NBP35,\nRP   SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, AND MUTAGENESIS OF ARG-534 AND\nRP   GLU-972.\nRX   PubMed=39348385; DOI=10.1371/journal.ppat.1012593;\nRA   Shrivastava D., Abboud E., Ramchandra J.P., Jha A., Marq J.B.,\nRA   Chaurasia A., Mitra K., Sadik M., Siddiqi M.I., Soldati-Favre D.,\nRA   Kloehn J., Habib S.;\nRT   \"ATM1, an essential conserved transporter in Apicomplexa, bridges\nRT   mitochondrial and cytosolic [Fe-S] biogenesis.\";\nRL   PLoS Pathog. 20:e1012593-e1012593(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "entry_version": 148,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Mitochondrion membrane\nCC       {ECO:0000305|PubMed:39348385}; Multi-pass membrane protein\nCC       {ECO:0000255}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "entry_version": 148,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0016020; C:membrane; ISS:GeneDB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148)

```json
{
  "entry_version": 148,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0031966; C:mitochondrial membrane; IEA:UniProtKB-SubCell.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:10.963943+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ecc9fb1303c91e20ea222fee968f93a70954dff7b257572b63e18f4fe50795bb",
  "url": "https://rest.uniprot.org/unisave/Q8IDH9?format=txt&versions=148"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005667\nname: transcription regulator complex\nnamespace: cellular_component\nalt_id: GO:0044797\nalt_id: GO:0044798\ndef: \"A protein complex that is capable of associating with DNA by direct binding, or via other DNA-binding proteins or complexes, and regulating transcription.\" [GOC:jl]\nsubset: goslim_pir\nsynonym: \"cytoplasmic transcription factor complex\" RELATED []\nsynonym: \"nuclear transcription factor complex\" RELATED []\nsynonym: \"transcription factor complex\" RELATED []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005667",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 58346-58358",
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
  "excerpt": "[Term]\nid: GO:0016234\nname: inclusion body\nnamespace: cellular_component\ndef: \"A discrete intracellular part formed of aggregated molecules such as proteins or other biopolymers.\" [GOC:mah, PMID:11121744]\nsynonym: \"cellular inclusion\" RELATED [NIF_Subcellular:sao120573470]\nsynonym: \"neuronal cytoplasmic inclusion\" NARROW []\nxref: NIF_Subcellular:sao120573470\nxref: Wikipedia:Inclusion_bodies\nis_a: GO:0005622 ! intracellular anatomical structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016234",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 124897-124907",
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
  "excerpt": "[Term]\nid: GO:0031966\nname: mitochondrial membrane\nnamespace: cellular_component\ndef: \"Either of the lipid bilayers that surround the mitochondrion and form the mitochondrial envelope.\" [GOC:mah, NIF_Subcellular:sao1045389829]\nxref: NIF_Subcellular:sao1045389829\nis_a: GO:0031090 ! organelle membrane\nrelationship: part_of GO:0005740 ! mitochondrial envelope\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031966",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 181484-181492",
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
  "excerpt": "[Term]\nid: GO:0043190\nname: ATP-binding cassette (ABC) transporter complex\nnamespace: cellular_component\nalt_id: GO:0043191\nalt_id: GO:0043192\ndef: \"A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter.\" [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsynonym: \"ABC-type efflux permease complex\" NARROW []\nsynonym: \"ABC-type efflux porter complex\" NARROW []\nsynonym: \"ABC-type uptake permease complex\" NARROW []\nsynonym: \"mating pheromone exporter\" NARROW []\nis_a: GO:0098533 ! ATPase dependent transmembrane transport complex\nis_a: GO:0098797 ! plasma membrane protein complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 244782-244797",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
