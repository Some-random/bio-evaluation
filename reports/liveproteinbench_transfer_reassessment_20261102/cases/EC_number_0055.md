# EC_number_0055

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0055.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 1.1.1.17

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDMKAIHFGGGNIGRGFVAEFLHKSGYEVVFVDVMDAIINALQQNKSYTVTEVGTSETKSKTIDNYRAINSKTDEDKVVEEIATADIVTCAVGPNILKFIAPVIAKGIENRKKDSPIAVIACENAIGATDTLRKFIEEKLSDSTKSNIQDKARFANSAIDRIVPMQDENAGLNVKIEKFYEWCVESKPFLPSQPPKIEGVHFVEDLTPFIERKLFTVNTGHATAAYYGYNRGKECIHDVLQDKELNEIVRNTLKETAHLIVNKHEISEEDQNQYVEKIIKRISNPVLKDNVERVGRAPLRKLSRNERFIGPAAHLAEMGAKYDALLGGIEMCLRFQNVEGDDESFELAKILKENSSSDATEKITGLERNHTLFPAVEEVVKKVQA

[Multiple Choices]
A. 1.1.1.336
B. 5.6.1.1
C. 2.7.1.39
D. 1.1.1.17
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

> The sequence-matched UniProt annotation assigns EC 1.1.1.17 and specifies the mannitol-1-phosphate dehydrogenase reaction. The assignment is supported by evidence transferred by similarity, rather than shown here as a direct assay of this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 386-residue sequence has a glycine-rich N-terminal dinucleotide-binding region and a downstream pattern consistent with an NAD-dependent mannitol-1-phosphate dehydrogenase-like protein. Recognition of that family from the full sequence and transferable knowledge of related enzymes meaningfully favors D over the isomerase and kinase alternatives, and can distinguish it from the other oxidoreductase choice; the glycine-rich motif alone would not establish substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference offers a credible route to the keyed EC among these choices without requiring the exact protein's database record. The evidence supports the answer, while the particular reaction is not demonstrated here by a direct experiment on this sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence-family inference.


### Important caveats

- The source assigns EC 1.1.1.17 by similarity to another UniProt entry; the supplied evidence does not independently establish experimental activity for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 386-residue sequence has a glycine-rich N-terminal dinucleotide-binding region and a downstream pattern consistent with an NAD-dependent mannitol-1-phosphate dehydrogenase-like protein. Recognition of that family from the full sequence and transferable knowledge of related enzymes meaningfully favors D over the isomerase and kinase alternatives, and can distinguish it from the other oxidoreductase choice; the glycine-rich motif alone would not establish substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference offers a credible route to the keyed EC among these choices without requiring the exact protein's database record. The evidence supports the answer, while the particular reaction is not demonstrated here by a direct experiment on this sequence."
  },
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.17 and specifies the mannitol-1-phosphate dehydrogenase reaction. The assignment is supported by evidence transferred by similarity, rather than shown here as a direct assay of this exact protein."
  },
  "important_caveats": [
    "The source assigns EC 1.1.1.17 by similarity to another UniProt entry; the supplied evidence does not independently establish experimental activity for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.17 and specifies the mannitol-1-phosphate dehydrogenase reaction. The assignment is supported by evidence transferred by similarity, rather than shown here as a direct assay of this exact protein.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 386-residue sequence has a glycine-rich N-terminal dinucleotide-binding region and a downstream pattern consistent with an NAD-dependent mannitol-1-phosphate dehydrogenase-like protein. Recognition of that family from the full sequence and transferable knowledge of related enzymes meaningfully favors D over the isomerase and kinase alternatives, and can distinguish it from the other oxidoreductase choice; the glycine-rich motif alone would not establish substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference offers a credible route to the keyed EC among these choices without requiring the exact protein's database record. The evidence supports the answer, while the particular reaction is not demonstrated here by a direct experiment on this sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence-family inference."
  },
  "important_caveats": [
    "The source assigns EC 1.1.1.17 by similarity to another UniProt entry; the supplied evidence does not independently establish experimental activity for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A223HDH4 (sequence matched) is annotated as EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase, MPDH). The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), meaning it is a computational inference by homology rather than a direct enzymatic assay on this exact protein. The protein name and its role in liamocin biosynthesis are supported by PubMed:32003433 (genetic evidence: FUNCTION, DISRUPTION PHENOTYPE). The sequence matches the benchmark input exactly (386 aa, SHA256 confirmed). The annotation is consistent with the expected answer D.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'GGGNIGRGF' is a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern), and the overall ~386-aa architecture with a hydrophobic β-sheet core ('VVFVDVMDAII') is characteristic of NAD-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 5.6.1.1, a racemase/epimerase – an isomerase that does not use NAD) and C (EC 2.7.1.39, a kinase/transferase – while some kinases have Rossmann-like folds, the strong GxGxxG NAD-binding signature and the absence of a P-loop or catalytic Lys/Arg kinase motif argue against a phosphotransferase). Between the two remaining EC 1.1.1.x options (A: 1.1.1.336 vs D: 1.1.1.17), the protein's size (~386 aa), the presence of a His-Asp catalytic dyad pattern ('CIHDVLQ'), and the overall fold architecture are well-matched to characterized fungal mannitol-1-phosphate 5-dehydrogenases (typically 350–400 aa, NAD-dependent, with conserved His/Asp catalytic residues). EC 1.1.1.336 is a very obscure/recently assigned entry; a model familiar with the well-studied MPDH family (present in fungi, bacteria, and plants) can recognize the sequence as belonging to that family rather than to the substrate class implied by 1.1.1.336. Fungal mannitol metabolism is a well-known pathway, and MPDH is a core enzyme in it, providing additional biological context that supports D over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold NAD-binding motif eliminates the isomerase and transferase options. The specific size, catalytic His-Asp dyad, and overall architecture match the well-characterized MPDH enzyme family (EC 1.1.1.17) found across fungi and other organisms. Transferable knowledge of dehydrogenase families and fungal mannitol metabolism provides a credible basis for selecting D over the obscure EC 1.1.1.336 distractor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are clearly eliminated by the NAD-binding Rossmann fold. Between A and D, the sequence features (size, catalytic dyad, family-level architecture) favor MPDH (D) over the obscure EC 1.1.1.336 (A). While the 4th-digit distinction is not trivially obvious from sequence alone, the well-characterized MPDH family signature and the biological plausibility in a fungal context provide a meaningful basis for discrimination.


### Important caveats

- The EC 1.1.1.17 annotation on the UniProt entry is based on similarity (ECO:0000250 to Q4X1A4), not a direct enzymatic assay on this specific A0A223HDH4 protein.
- The protein's function in liamocin biosynthesis was established genetically (knockout/disruption phenotype, PubMed 32003433), but the specific EC number assignment relies on homology transfer.
- EC 1.1.1.336 is a very obscure entry; its exact identity and structural features are not well-characterized in the literature, making the A-vs-D distinction partly dependent on the relative obscurity of option A as a distractor.
- The sequence is from Aureobasidium melanogenum (fungal), which is consistent with known MPDH biology but this organism identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'GGGNIGRGF' is a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern), and the overall ~386-aa architecture with a hydrophobic β-sheet core ('VVFVDVMDAII') is characteristic of NAD-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 5.6.1.1, a racemase/epimerase – an isomerase that does not use NAD) and C (EC 2.7.1.39, a kinase/transferase – while some kinases have Rossmann-like folds, the strong GxGxxG NAD-binding signature and the absence of a P-loop or catalytic Lys/Arg kinase motif argue against a phosphotransferase). Between the two remaining EC 1.1.1.x options (A: 1.1.1.336 vs D: 1.1.1.17), the protein's size (~386 aa), the presence of a His-Asp catalytic dyad pattern ('CIHDVLQ'), and the overall fold architecture are well-matched to characterized fungal mannitol-1-phosphate 5-dehydrogenases (typically 350–400 aa, NAD-dependent, with conserved His/Asp catalytic residues). EC 1.1.1.336 is a very obscure/recently assigned entry; a model familiar with the well-studied MPDH family (present in fungi, bacteria, and plants) can recognize the sequence as belonging to that family rather than to the substrate class implied by 1.1.1.336. Fungal mannitol metabolism is a well-known pathway, and MPDH is a core enzyme in it, providing additional biological context that supports D over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif eliminates the isomerase and transferase options. The specific size, catalytic His-Asp dyad, and overall architecture match the well-characterized MPDH enzyme family (EC 1.1.1.17) found across fungi and other organisms. Transferable knowledge of dehydrogenase families and fungal mannitol metabolism provides a credible basis for selecting D over the obscure EC 1.1.1.336 distractor."
  },
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A223HDH4 (sequence matched) is annotated as EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase, MPDH). The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), meaning it is a computational inference by homology rather than a direct enzymatic assay on this exact protein. The protein name and its role in liamocin biosynthesis are supported by PubMed:32003433 (genetic evidence: FUNCTION, DISRUPTION PHENOTYPE). The sequence matches the benchmark input exactly (386 aa, SHA256 confirmed). The annotation is consistent with the expected answer D."
  },
  "important_caveats": [
    "The EC 1.1.1.17 annotation on the UniProt entry is based on similarity (ECO:0000250 to Q4X1A4), not a direct enzymatic assay on this specific A0A223HDH4 protein.",
    "The protein's function in liamocin biosynthesis was established genetically (knockout/disruption phenotype, PubMed 32003433), but the specific EC number assignment relies on homology transfer.",
    "EC 1.1.1.336 is a very obscure entry; its exact identity and structural features are not well-characterized in the literature, making the A-vs-D distinction partly dependent on the relative obscurity of option A as a distractor.",
    "The sequence is from Aureobasidium melanogenum (fungal), which is consistent with known MPDH biology but this organism identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the NAD-binding Rossmann fold. Between A and D, the sequence features (size, catalytic dyad, family-level architecture) favor MPDH (D) over the obscure EC 1.1.1.336 (A). While the 4th-digit distinction is not trivially obvious from sequence alone, the well-characterized MPDH family signature and the biological plausibility in a fungal context provide a meaningful basis for discrimination."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0055",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A223HDH4 (sequence matched) is annotated as EC 1.1.1.17 (Mannitol-1-phosphate 5-dehydrogenase, MPDH). The EC assignment carries evidence code ECO:0000250 (similarity to Q4X1A4), meaning it is a computational inference by homology rather than a direct enzymatic assay on this exact protein. The protein name and its role in liamocin biosynthesis are supported by PubMed:32003433 (genetic evidence: FUNCTION, DISRUPTION PHENOTYPE). The sequence matches the benchmark input exactly (386 aa, SHA256 confirmed). The annotation is consistent with the expected answer D.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'GGGNIGRGF' is a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern), and the overall ~386-aa architecture with a hydrophobic β-sheet core ('VVFVDVMDAII') is characteristic of NAD-dependent oxidoreductases (EC 1.1.1.x). This immediately eliminates B (EC 5.6.1.1, a racemase/epimerase – an isomerase that does not use NAD) and C (EC 2.7.1.39, a kinase/transferase – while some kinases have Rossmann-like folds, the strong GxGxxG NAD-binding signature and the absence of a P-loop or catalytic Lys/Arg kinase motif argue against a phosphotransferase). Between the two remaining EC 1.1.1.x options (A: 1.1.1.336 vs D: 1.1.1.17), the protein's size (~386 aa), the presence of a His-Asp catalytic dyad pattern ('CIHDVLQ'), and the overall fold architecture are well-matched to characterized fungal mannitol-1-phosphate 5-dehydrogenases (typically 350–400 aa, NAD-dependent, with conserved His/Asp catalytic residues). EC 1.1.1.336 is a very obscure/recently assigned entry; a model familiar with the well-studied MPDH family (present in fungi, bacteria, and plants) can recognize the sequence as belonging to that family rather than to the substrate class implied by 1.1.1.336. Fungal mannitol metabolism is a well-known pathway, and MPDH is a core enzyme in it, providing additional biological context that supports D over A.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold NAD-binding motif eliminates the isomerase and transferase options. The specific size, catalytic His-Asp dyad, and overall architecture match the well-characterized MPDH enzyme family (EC 1.1.1.17) found across fungi and other organisms. Transferable knowledge of dehydrogenase families and fungal mannitol metabolism provides a credible basis for selecting D over the obscure EC 1.1.1.336 distractor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are clearly eliminated by the NAD-binding Rossmann fold. Between A and D, the sequence features (size, catalytic dyad, family-level architecture) favor MPDH (D) over the obscure EC 1.1.1.336 (A). While the 4th-digit distinction is not trivially obvious from sequence alone, the well-characterized MPDH family signature and the biological plausibility in a fungal context provide a meaningful basis for discrimination."
  },
  "important_caveats": [
    "The EC 1.1.1.17 annotation on the UniProt entry is based on similarity (ECO:0000250 to Q4X1A4), not a direct enzymatic assay on this specific A0A223HDH4 protein.",
    "The protein's function in liamocin biosynthesis was established genetically (knockout/disruption phenotype, PubMed 32003433), but the specific EC number assignment relies on homology transfer.",
    "EC 1.1.1.336 is a very obscure entry; its exact identity and structural features are not well-characterized in the literature, making the A-vs-D distinction partly dependent on the relative obscurity of option A as a distractor.",
    "The sequence is from Aureobasidium melanogenum (fungal), which is consistent with known MPDH biology but this organism identity was not provided to the evaluated model."
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
  "benchmark_sequence_length": 386,
  "benchmark_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "current_entry_audit": {
    "entryVersion": 16,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 386,
  "current_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223HDH4",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "selected_historical_source_sequence_length": 386,
  "selected_historical_source_sequence_sha256": "0560835617463254f8bb4727e9aa3fdfd4d7e2ebec6b8a2c79e57b4d0f7ae518",
  "selected_historical_version": {
    "accession": "A0A223HDH4",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "MPDH_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223HDH4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":16,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1A4\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.17\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Mannitol-1-phosphate 5-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"MPDH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.1.1.17\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4X1A4\",\"source\":\"UniProtKB\"}],\"name\":\"D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate + NADH + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:19661\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57634\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61381\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223HDH4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:43.559987+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c8df05c75e909c885087b874bfd4270859d408d933f4695e68a2b558bd8ea6e",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223HDH4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   MPDH_AURME              Reviewed;         386 AA.\nAC   A0A223HDH4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MPDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Mannitol-1-phosphate 5-dehydrogenase {ECO:0000303|PubMed:32003433};\nDE            Short=MPDH {ECO:0000303|PubMed:32003433};\nDE            EC=1.1.1.17 {ECO:0000250|UniProtKB:Q4X1A4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-mannitol 1-phosphate + NAD(+) = beta-D-fructose 6-phosphate\nCC         + NADH + H(+); Xref=Rhea:RHEA:19661, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57634, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:61381; EC=1.1.1.17;\nCC         Evidence={ECO:0000250|UniProtKB:Q4X1A4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:46.025296+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cdb64e60ab7ff06bc6c58dba44ce5f9a0a74986e515a667043ef14c65f549ac0",
  "url": "https://rest.uniprot.org/unisave/A0A223HDH4?format=txt&versions=15"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 55. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
