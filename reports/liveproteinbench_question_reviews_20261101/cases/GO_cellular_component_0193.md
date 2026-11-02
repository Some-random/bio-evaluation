# GO_cellular_component_0193

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — lysosomal membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTRPYIKRLSFTLLDSITDKDPMVQEQVCSALCSLGDAQPDETLHACEEYLRQHDKLAHPYRTKILRAMETVLSSHIHDLDKDTAGAVILLATSEMTRTKELDCDWQQAAGSVLVAVGKRFTNQVMEEVLSRFQPGMLPHSSVLHTLANLSVSNAFDMVPFLPSILSTMLPMLSMAKQDALKVVFCGALQHFSESILEYLANLDQAPDPTVRKDTFGADIFGAYDVLFHHWLQSRDAKLRLAVVAALGPMSHLLPSERLEEQLPKLLPAVLGLYKKHAEAFQISKSLGQILEAAVNVSSRTLEVQLDALLVALHAQICVPVESSSPLVMNSQKEVLRCFTVLACCSPDRLLAFLLPRLDTSNERLRVGTLQILRHIINSAAAQMEAKQPFILSSMRLPLLDTNDKVKRAVVQVISAMAHHGYLEQPGGEVMVEYIVQQCALPAEEPEKPGPDGEDLAADSVRAVSIRTLYLVSTTVDRMNSVLWPYLLEFLTPVRFTAALTPLCRSLVHLALKRQEAGADDFLIQYNANANLPSPFAMTTRLLVVSSNPYLGDGRGAASLRLLKVMHQNIHPFLGQRWETTMPMLLEYLDEHTEESLSLKEWEEKLLMFLRDTLAVVSDNIWICQLSQEMCKQLPSYSGTPQEKNFLYKCIGTTLGAASSKEVVRKHLRELLETARYQEEAEQEGLACCFGICAITHLEDTLAQLEDFVRSDVFRKSTGIFSIFKDRSEHEVERMKSCLILCYGHVAAQAPRELVLARVESDILRSMFQCFNTKVLGIKVETKDPALKLCLVQSLCMVSQAMCSSAQASSFHFLRKTELVTQMMEFIRAEPPDCLRTPIRKKAMLACTYLVNLEPALEEQTQADVVHSCLHSVMALPPEAEGGDGVGREPLYLDTVCALEDLLTRLLRQNMTPQGLQIMVEHLSPWIKSPRGHERARALGLGACLLEFFQEHLLVSTLVPFHNLGLLVGLFAPRCADTWTTTRQKAVGCVYSLLYLQLGYEGFSRDHRDDVAERLLTLQDGLVNADPTILFHTCHSIAQVIAKRLPSDQLISLLLTVFESLGDPDKNCSRAATVMINCLLKERGNVLLEKVPEIVSVLRAKLRDTQEEHVLPAAQHSVYLLASQHCEAVVSSLLGSPLPFDSHTCALWRALAVEPGLTAQVLELLLEKMSKDVPFKESRAFLLGSTADRVATLLPLAATCALYEVLSAPSSGTVVLELYPQLFAALLLRVSCTVGVQLPRNLQAKERRSTSPARAARNLDPCSSAVDALQALLLRSGSQDMLRCVELERGWELLKTSAGHEDGVAQLASSMAKYAGPRLPPVTKALACTQNSVYEIQRVTSTAFLAELLSSNVVNDLMLLEPLLDNLTARLKDSSASVRRLVLRGLANMASGSPDKVRAHGPQLLTAMVSGLDDGDEPHSPVALEAMVGLSRLLDLVEPWDLRLVLLHTTIRIRPFFDSEKVEFRTASIRLFGHLNKACHGDCEDVFLEQVVGGLVPLLLHLRDPQVPVASACKFALCMCVPHLECAELAAAFYKYLQEGRSVHFGEFLNSTCKHLMHHFPDLLGRLVSTNLFYFKSSWDDVRAAAPMFTGFLVLHAEPEQKTQVDLEQLIVALQLLLKDPVPGVREKAAETLGRLVKFA

[Multiple Choices]
A. nuclear pore
B. lysosomal membrane
C. SAGA complex
D. striated muscle dense body
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the MROH1_MOUSE record, which annotates lysosomal membrane localization and recruitment there by RAB7. This supports B, though the localization is transferred by similarity (ECO:0000250) and the GO annotation is ISS, not direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence does not provide a clear targeting signal that distinguishes lysosomal membrane localization from the listed alternatives. Its lack of an obvious transmembrane segment would not rule out peripheral recruitment to a membrane.


**Missing item-specific fact**

> That MROH1 is recruited to the lysosomal membrane by RAB7, or an equivalent protein-specific localization annotation or measurement.


**Reason**

> The key is supported by a protein-specific annotation, but that fact is absent from the sequence and choices; sequence-based general reasoning does not meaningfully establish B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; no competing option is supported for this sequence.


### Important caveats

- The localization evidence is similarity-transferred, not a direct experimental localization result for this mouse protein.
- The exact author source snapshot is unknown, although the matched historical record already contained the lysosomal membrane annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence does not provide a clear targeting signal that distinguishes lysosomal membrane localization from the listed alternatives. Its lack of an obvious transmembrane segment would not rule out peripheral recruitment to a membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That MROH1 is recruited to the lysosomal membrane by RAB7, or an equivalent protein-specific localization annotation or measurement.",
    "reason": "The key is supported by a protein-specific annotation, but that fact is absent from the sequence and choices; sequence-based general reasoning does not meaningfully establish B."
  },
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the MROH1_MOUSE record, which annotates lysosomal membrane localization and recruitment there by RAB7. This supports B, though the localization is transferred by similarity (ECO:0000250) and the GO annotation is ISS, not direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The localization evidence is similarity-transferred, not a direct experimental localization result for this mouse protein.",
    "The exact author source snapshot is unknown, although the matched historical record already contained the lysosomal membrane annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no competing option is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the MROH1_MOUSE record, which annotates lysosomal membrane localization and recruitment there by RAB7. This supports B, though the localization is transferred by similarity (ECO:0000250) and the GO annotation is ISS, not direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence does not provide a clear targeting signal that distinguishes lysosomal membrane localization from the listed alternatives. Its lack of an obvious transmembrane segment would not rule out peripheral recruitment to a membrane.",
    "missing_item_specific_fact": "That MROH1 is recruited to the lysosomal membrane by RAB7, or an equivalent protein-specific localization annotation or measurement.",
    "reason": "The key is supported by a protein-specific annotation, but that fact is absent from the sequence and choices; sequence-based general reasoning does not meaningfully establish B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no competing option is supported for this sequence."
  },
  "important_caveats": [
    "The localization evidence is similarity-transferred, not a direct experimental localization result for this mouse protein.",
    "The exact author source snapshot is unknown, although the matched historical record already contained the lysosomal membrane annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0CZ22 (MROH1_MOUSE) annotates the subcellular location as 'Lysosome membrane' with note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B)' (evidence code ECO:0000250, inferred from similarity to human Q8NDA8). The GO cross-reference GO:0005765 C:lysosomal membrane with evidence type ISS:UniProtKB confirms the annotation. However, this is a computational/sequence-similarity transfer annotation, not direct experimental localization of the mouse protein. A secondary GO annotation for cytoplasm (GO:0005737, IBA:GO_Central) also exists but is not among the answer choices.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 1640-aa sequence is a large HEAT/armadillo-repeat protein with no obvious transmembrane helix, signal peptide, nuclear localization signal, or muscle-structural domain. General sequence reasoning can eliminate D (striated muscle dense body: no vinculin/actin-binding architecture) and C (SAGA complex: no HAT/ADA/SPT-domain signatures). Eliminating A (nuclear pore) vs. B (lysosomal membrane) requires knowing that MROH1 is specifically recruited to the lysosomal membrane via a protein-protein interaction with RAB7 — an item-specific fact not encoded in any recognizable targeting motif in the sequence. HEAT repeats occur in proteins across all compartments, so the repeat architecture alone cannot distinguish nuclear pore from lysosomal membrane.


**Missing item-specific fact**

> The specific RAB7-mediated recruitment of MROH1 to the lysosomal membrane, which is a protein-protein interaction fact absent from the sequence and not inferable from general targeting-signal logic.


**Reason**

> A model cannot deduce from the HEAT-repeat sequence alone that this protein associates with the lysosomal membrane rather than the nuclear pore or another compartment. Correct selection depends on recognizing the protein as MROH1 and recalling its documented RAB7-dependent lysosomal membrane association.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided choices, the other three (nuclear pore, SAGA complex, striated muscle dense body) are clearly incompatible with the sequence architecture and known biology of MROH1. Although the protein also carries a cytoplasm GO annotation (IBA), cytoplasm is not an option. No ambiguity exists among the listed choices.


### Important caveats

- The lysosomal membrane annotation carries evidence code ECO:0000250 / ISS, meaning it was inferred by sequence similarity to human MROH1 (Q8NDA8), not by direct experimental localization of the mouse protein.
- A secondary GO annotation places the protein in cytoplasm (GO:0005737, IBA:GO_Central), which is not among the answer choices but reflects that the protein may also reside in the cytosol when not recruited to the lysosome.
- The sequence-match is confirmed against both current (v95) and historical (v93) UniProt records; the accession E0CZ22 was inferred by the reviewer from dataset metadata, not provided to the evaluated model.
- The entry was first publicly released on 2025-06-18, raising a question about whether it existed in the annotation databases at the time the benchmark was constructed; however, the sequence itself (version 1, dated 2010-10-05) predates that release.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1640-aa sequence is a large HEAT/armadillo-repeat protein with no obvious transmembrane helix, signal peptide, nuclear localization signal, or muscle-structural domain. General sequence reasoning can eliminate D (striated muscle dense body: no vinculin/actin-binding architecture) and C (SAGA complex: no HAT/ADA/SPT-domain signatures). Eliminating A (nuclear pore) vs. B (lysosomal membrane) requires knowing that MROH1 is specifically recruited to the lysosomal membrane via a protein-protein interaction with RAB7 — an item-specific fact not encoded in any recognizable targeting motif in the sequence. HEAT repeats occur in proteins across all compartments, so the repeat architecture alone cannot distinguish nuclear pore from lysosomal membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific RAB7-mediated recruitment of MROH1 to the lysosomal membrane, which is a protein-protein interaction fact absent from the sequence and not inferable from general targeting-signal logic.",
    "reason": "A model cannot deduce from the HEAT-repeat sequence alone that this protein associates with the lysosomal membrane rather than the nuclear pore or another compartment. Correct selection depends on recognizing the protein as MROH1 and recalling its documented RAB7-dependent lysosomal membrane association."
  },
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0CZ22 (MROH1_MOUSE) annotates the subcellular location as 'Lysosome membrane' with note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B)' (evidence code ECO:0000250, inferred from similarity to human Q8NDA8). The GO cross-reference GO:0005765 C:lysosomal membrane with evidence type ISS:UniProtKB confirms the annotation. However, this is a computational/sequence-similarity transfer annotation, not direct experimental localization of the mouse protein. A secondary GO annotation for cytoplasm (GO:0005737, IBA:GO_Central) also exists but is not among the answer choices."
  },
  "important_caveats": [
    "The lysosomal membrane annotation carries evidence code ECO:0000250 / ISS, meaning it was inferred by sequence similarity to human MROH1 (Q8NDA8), not by direct experimental localization of the mouse protein.",
    "A secondary GO annotation places the protein in cytoplasm (GO:0005737, IBA:GO_Central), which is not among the answer choices but reflects that the protein may also reside in the cytosol when not recruited to the lysosome.",
    "The sequence-match is confirmed against both current (v95) and historical (v93) UniProt records; the accession E0CZ22 was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The entry was first publicly released on 2025-06-18, raising a question about whether it existed in the annotation databases at the time the benchmark was constructed; however, the sequence itself (version 1, dated 2010-10-05) predates that release."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, the other three (nuclear pore, SAGA complex, striated muscle dense body) are clearly incompatible with the sequence architecture and known biology of MROH1. Although the protein also carries a cytoplasm GO annotation (IBA), cytoplasm is not an option. No ambiguity exists among the listed choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0CZ22 (MROH1_MOUSE) annotates the subcellular location as 'Lysosome membrane' with note 'Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B)' (evidence code ECO:0000250, inferred from similarity to human Q8NDA8). The GO cross-reference GO:0005765 C:lysosomal membrane with evidence type ISS:UniProtKB confirms the annotation. However, this is a computational/sequence-similarity transfer annotation, not direct experimental localization of the mouse protein. A secondary GO annotation for cytoplasm (GO:0005737, IBA:GO_Central) also exists but is not among the answer choices.",
    "evidence_ids": ["C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 1640-aa sequence is a large HEAT/armadillo-repeat protein with no obvious transmembrane helix, signal peptide, nuclear localization signal, or muscle-structural domain. General sequence reasoning can eliminate D (striated muscle dense body: no vinculin/actin-binding architecture) and C (SAGA complex: no HAT/ADA/SPT-domain signatures). Eliminating A (nuclear pore) vs. B (lysosomal membrane) requires knowing that MROH1 is specifically recruited to the lysosomal membrane via a protein-protein interaction with RAB7 — an item-specific fact not encoded in any recognizable targeting motif in the sequence. HEAT repeats occur in proteins across all compartments, so the repeat architecture alone cannot distinguish nuclear pore from lysosomal membrane.",
    "missing_item_specific_fact": "The specific RAB7-mediated recruitment of MROH1 to the lysosomal membrane, which is a protein-protein interaction fact absent from the sequence and not inferable from general targeting-signal logic.",
    "reason": "A model cannot deduce from the HEAT-repeat sequence alone that this protein associates with the lysosomal membrane rather than the nuclear pore or another compartment. Correct selection depends on recognizing the protein as MROH1 and recalling its documented RAB7-dependent lysosomal membrane association."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided choices, the other three (nuclear pore, SAGA complex, striated muscle dense body) are clearly incompatible with the sequence architecture and known biology of MROH1. Although the protein also carries a cytoplasm GO annotation (IBA), cytoplasm is not an option. No ambiguity exists among the listed choices."
  },
  "important_caveats": [
    "The lysosomal membrane annotation carries evidence code ECO:0000250 / ISS, meaning it was inferred by sequence similarity to human MROH1 (Q8NDA8), not by direct experimental localization of the mouse protein.",
    "A secondary GO annotation places the protein in cytoplasm (GO:0005737, IBA:GO_Central), which is not among the answer choices but reflects that the protein may also reside in the cytosol when not recruited to the lysosome.",
    "The sequence-match is confirmed against both current (v95) and historical (v93) UniProt records; the accession E0CZ22 was inferred by the reviewer from dataset metadata, not provided to the evaluated model.",
    "The entry was first publicly released on 2025-06-18, raising a question about whether it existed in the annotation databases at the time the benchmark was constructed; however, the sequence itself (version 1, dated 2010-10-05) predates that release."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `E0CZ22` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 93. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
"E0CZ22"
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8NDA8","source":"UniProtKB"}],"value":"Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q8NDA8","source":"UniProtKB"}],"id":"SL-0157","value":"Lysosome membrane"}}]}
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0CZ22.json)  
**Locator:** `/uniProtKBCrossReferences/43`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:53.277334+00:00.  

```json
{"database":"GO","id":"GO:0005765","properties":[{"key":"GoTerm","value":"C:lysosomal membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `f6a20f4b2e49cac1aebed4df6c926a4cbaf277f2a8d77049ee0e2cc7af2472d0`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)  
**Locator:** `lines 46-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 93 / 1.  
**Retrieved:** 2026-11-02T04:27:56.152074+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Lysosome membrane {ECO:0000250|UniProtKB:Q8NDA8}.
CC       Note=Recruited to the lysosome membrane by RAB7 (RAB7A or RAB7B).
CC       {ECO:0000250|UniProtKB:Q8NDA8}.
```

Source SHA-256: `ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0CZ22?format=txt&versions=93)  
**Locator:** `lines 105-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 93 / 1.  
**Retrieved:** 2026-11-02T04:27:56.152074+00:00.  

```text
DR   GO; GO:0005765; C:lysosomal membrane; ISS:UniProtKB.
```

Source SHA-256: `ec15527623ff2c6713c5dc447b8ee3d269dc5a7b2b4241db5d9f640829918316`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 193. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
