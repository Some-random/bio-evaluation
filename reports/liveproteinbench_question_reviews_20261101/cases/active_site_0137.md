# active_site_0137

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 258 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. Position 413 (Proton donor)
B. Position 258 (Nucleophile)
C. Position 52 (Proton acceptor; for glutaminase activity)
D. Position 366 (For beta-ketoacyl synthase activity)
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the UniProt entry, which annotates residue 258 as the nucleophile. This supports choice B, though the annotation is transferred by similarity from Q0P8H3 rather than presented here as direct experimental evidence for this sequence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The input provides a sequence but no enzyme identity, reaction, or mechanistic context that would establish which residue is the nucleophile. Identifying an enzyme family from sequence would not by itself establish the exact catalytic residue number.


**Missing item-specific fact**

> The protein-specific assignment of residue 258 as the nucleophile, or equivalent knowledge of this enzyme's catalytic mechanism and residue numbering.


**Reason**

> Distinguishing B requires a protein-specific functional annotation or mechanistic fact absent from the question; the reviewer-only database annotation cannot be treated as information supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; it does not identify another listed option as a catalytic residue for this enzyme.


### Important caveats

- The residue-258 annotation is supported by similarity evidence from UniProtKB entry Q0P8H3, not independently established here by direct experimental evidence for the supplied protein.
- The reviewer-only source matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The input provides a sequence but no enzyme identity, reaction, or mechanistic context that would establish which residue is the nucleophile. Identifying an enzyme family from sequence would not by itself establish the exact catalytic residue number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of residue 258 as the nucleophile, or equivalent knowledge of this enzyme's catalytic mechanism and residue numbering.",
    "reason": "Distinguishing B requires a protein-specific functional annotation or mechanistic fact absent from the question; the reviewer-only database annotation cannot be treated as information supplied to the model."
  },
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates residue 258 as the nucleophile. This supports choice B, though the annotation is transferred by similarity from Q0P8H3 rather than presented here as direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The residue-258 annotation is supported by similarity evidence from UniProtKB entry Q0P8H3, not independently established here by direct experimental evidence for the supplied protein.",
    "The reviewer-only source matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not identify another listed option as a catalytic residue for this enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates residue 258 as the nucleophile. This supports choice B, though the annotation is transferred by similarity from Q0P8H3 rather than presented here as direct experimental evidence for this sequence.",
    "evidence_ids": ["C1", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The input provides a sequence but no enzyme identity, reaction, or mechanistic context that would establish which residue is the nucleophile. Identifying an enzyme family from sequence would not by itself establish the exact catalytic residue number.",
    "missing_item_specific_fact": "The protein-specific assignment of residue 258 as the nucleophile, or equivalent knowledge of this enzyme's catalytic mechanism and residue numbering.",
    "reason": "Distinguishing B requires a protein-specific functional annotation or mechanistic fact absent from the question; the reviewer-only database annotation cannot be treated as information supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; it does not identify another listed option as a catalytic residue for this enzyme."
  },
  "important_caveats": [
    "The residue-258 annotation is supported by similarity evidence from UniProtKB entry Q0P8H3, not independently established here by direct experimental evidence for the supplied protein.",
    "The reviewer-only source matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence matches UniProt Q9RHD7 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, Pseudomonas aeruginosa) exactly (SHA256 match confirmed). UniProt annotates position 258 as 'Nucleophile' active site (evidence IDs C5, H5). However, the evidence code is ECO:0000250 (inferred by similarity to Q0P8H3), meaning the nucleophile assignment is a computational transfer rather than a direct experimental determination for this specific protein. The PubMed reference (18065759) established catalytic activity and function experimentally but the residue-level nucleophile annotation is by homology.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choices C ('Proton acceptor; for glutaminase activity') and D ('For beta-ketoacyl synthase activity') can be eliminated by recognizing the N-terminal Rossmann-fold motif (GxGxxG at ~positions 5–13) and the overall architecture as an NAD-dependent dehydrogenase, not a glutaminase or fatty-acid synthase. However, distinguishing A (position 413, proton donor) from B (position 258, nucleophile) requires knowledge of the specific catalytic mechanism of UDP-GlcNAc 6-dehydrogenase. A weak structural argument exists: position 413 of 422 lies at the extreme C-terminus, far from all annotated NAD+ binding sites (14, 32, 37, 83, 118, 329), making it an atypical location for the primary catalytic residue, while position 258 falls within the central catalytic domain. This is suggestive but not conclusive without knowing the enzyme's mechanism.


**Missing item-specific fact**

> The specific catalytic mechanism of UDP-N-acetyl-D-glucosamine 6-dehydrogenase (i.e., that a cysteine at position 258 acts as the nucleophile forming a thiohemiacetal intermediate with the C6 carbonyl), which is not derivable from sequence alone and is annotated only by similarity transfer (ECO:0000250) in UniProt.


**Reason**

> General biological knowledge allows elimination of C and D (wrong enzyme classes) and provides a weak spatial argument against A (extreme C-terminus). However, the definitive identification of position 258 as the nucleophile depends on enzyme-specific mechanistic knowledge or database annotation, not on reasoning from the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C and D are clearly incompatible with a dehydrogenase. Between A and B, the extreme C-terminal location of position 413 (residue 413/422) makes it a poor candidate for the primary catalytic residue of an NAD-dependent dehydrogenase, giving B a modest but real edge. No other option is defensible.


### Important caveats

- The UniProt nucleophile annotation at position 258 carries evidence code ECO:0000250 (by similarity to Q0P8H3), not direct experimental mutagenesis or structural determination for Q9RHD7 itself.
- The reviewer-only UniProt accession (Q9RHD7) was inferred from dataset metadata and was not provided to the evaluated model; the model saw only the raw sequence.
- The PubMed reference (18065759, Miller et al. 2008) established catalytic activity, biophysical properties, and disruption phenotype experimentally, but the residue-level nucleophile assignment is a homology transfer.
- The sequence is 422 residues; position 413 is 9 residues from the C-terminus, making it structurally implausible as the primary catalytic nucleophile of a Rossmann-fold dehydrogenase, but this is a heuristic, not a proof.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choices C ('Proton acceptor; for glutaminase activity') and D ('For beta-ketoacyl synthase activity') can be eliminated by recognizing the N-terminal Rossmann-fold motif (GxGxxG at ~positions 5–13) and the overall architecture as an NAD-dependent dehydrogenase, not a glutaminase or fatty-acid synthase. However, distinguishing A (position 413, proton donor) from B (position 258, nucleophile) requires knowledge of the specific catalytic mechanism of UDP-GlcNAc 6-dehydrogenase. A weak structural argument exists: position 413 of 422 lies at the extreme C-terminus, far from all annotated NAD+ binding sites (14, 32, 37, 83, 118, 329), making it an atypical location for the primary catalytic residue, while position 258 falls within the central catalytic domain. This is suggestive but not conclusive without knowing the enzyme's mechanism.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific catalytic mechanism of UDP-N-acetyl-D-glucosamine 6-dehydrogenase (i.e., that a cysteine at position 258 acts as the nucleophile forming a thiohemiacetal intermediate with the C6 carbonyl), which is not derivable from sequence alone and is annotated only by similarity transfer (ECO:0000250) in UniProt.",
    "reason": "General biological knowledge allows elimination of C and D (wrong enzyme classes) and provides a weak spatial argument against A (extreme C-terminus). However, the definitive identification of position 258 as the nucleophile depends on enzyme-specific mechanistic knowledge or database annotation, not on reasoning from the raw sequence."
  },
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q9RHD7 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, Pseudomonas aeruginosa) exactly (SHA256 match confirmed). UniProt annotates position 258 as 'Nucleophile' active site (evidence IDs C5, H5). However, the evidence code is ECO:0000250 (inferred by similarity to Q0P8H3), meaning the nucleophile assignment is a computational transfer rather than a direct experimental determination for this specific protein. The PubMed reference (18065759) established catalytic activity and function experimentally but the residue-level nucleophile annotation is by homology."
  },
  "important_caveats": [
    "The UniProt nucleophile annotation at position 258 carries evidence code ECO:0000250 (by similarity to Q0P8H3), not direct experimental mutagenesis or structural determination for Q9RHD7 itself.",
    "The reviewer-only UniProt accession (Q9RHD7) was inferred from dataset metadata and was not provided to the evaluated model; the model saw only the raw sequence.",
    "The PubMed reference (18065759, Miller et al. 2008) established catalytic activity, biophysical properties, and disruption phenotype experimentally, but the residue-level nucleophile assignment is a homology transfer.",
    "The sequence is 422 residues; position 413 is 9 residues from the C-terminus, making it structurally implausible as the primary catalytic nucleophile of a Rossmann-fold dehydrogenase, but this is a heuristic, not a proof."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are clearly incompatible with a dehydrogenase. Between A and B, the extreme C-terminal location of position 413 (residue 413/422) makes it a poor candidate for the primary catalytic residue of an NAD-dependent dehydrogenase, giving B a modest but real edge. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0137",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches UniProt Q9RHD7 (UDP-N-acetyl-D-glucosamine 6-dehydrogenase, EC 1.1.1.136, Pseudomonas aeruginosa) exactly (SHA256 match confirmed). UniProt annotates position 258 as 'Nucleophile' active site (evidence IDs C5, H5). However, the evidence code is ECO:0000250 (inferred by similarity to Q0P8H3), meaning the nucleophile assignment is a computational transfer rather than a direct experimental determination for this specific protein. The PubMed reference (18065759) established catalytic activity and function experimentally but the residue-level nucleophile annotation is by homology.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choices C ('Proton acceptor; for glutaminase activity') and D ('For beta-ketoacyl synthase activity') can be eliminated by recognizing the N-terminal Rossmann-fold motif (GxGxxG at ~positions 5–13) and the overall architecture as an NAD-dependent dehydrogenase, not a glutaminase or fatty-acid synthase. However, distinguishing A (position 413, proton donor) from B (position 258, nucleophile) requires knowledge of the specific catalytic mechanism of UDP-GlcNAc 6-dehydrogenase. A weak structural argument exists: position 413 of 422 lies at the extreme C-terminus, far from all annotated NAD+ binding sites (14, 32, 37, 83, 118, 329), making it an atypical location for the primary catalytic residue, while position 258 falls within the central catalytic domain. This is suggestive but not conclusive without knowing the enzyme's mechanism.",
    "missing_item_specific_fact": "The specific catalytic mechanism of UDP-N-acetyl-D-glucosamine 6-dehydrogenase (i.e., that a cysteine at position 258 acts as the nucleophile forming a thiohemiacetal intermediate with the C6 carbonyl), which is not derivable from sequence alone and is annotated only by similarity transfer (ECO:0000250) in UniProt.",
    "reason": "General biological knowledge allows elimination of C and D (wrong enzyme classes) and provides a weak spatial argument against A (extreme C-terminus). However, the definitive identification of position 258 as the nucleophile depends on enzyme-specific mechanistic knowledge or database annotation, not on reasoning from the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C and D are clearly incompatible with a dehydrogenase. Between A and B, the extreme C-terminal location of position 413 (residue 413/422) makes it a poor candidate for the primary catalytic residue of an NAD-dependent dehydrogenase, giving B a modest but real edge. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt nucleophile annotation at position 258 carries evidence code ECO:0000250 (by similarity to Q0P8H3), not direct experimental mutagenesis or structural determination for Q9RHD7 itself.",
    "The reviewer-only UniProt accession (Q9RHD7) was inferred from dataset metadata and was not provided to the evaluated model; the model saw only the raw sequence.",
    "The PubMed reference (18065759, Miller et al. 2008) established catalytic activity, biophysical properties, and disruption phenotype experimentally, but the residue-level nucleophile assignment is a homology transfer.",
    "The sequence is 422 residues; position 413 is 9 residues from the C-terminus, making it structurally implausible as the primary catalytic nucleophile of a Rossmann-fold dehydrogenase, but this is a heuristic, not a proof."
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

**Accession:** `Q9RHD7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 111. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0P8H3","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":258},"start":{"modifier":"EXACT","value":258}},"type":"Active site"}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000250","id":"Q0P8H3","source":"UniProtKB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:57540"}],"ligand":{"id":"ChEBI:CHEBI:57540","name":"NAD(+)"},"location":{"end":{"modifier":"EXACT","value":14},"start":{"modifier":"EXACT","value":14}},"type":"Binding site"}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
ID   WBPO_PSEAI              Reviewed;         422 AA.
AC   Q9RHD7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAY-2000, sequence version 1.
DT   28-JAN-2026, entry version 111.
DE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};
DE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};
DE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};
GN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};
GN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};
OS   Pseudomonas aeruginosa.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=287;
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 177-179`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
FT   ACT_SITE        258
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000250|UniProtKB:Q0P8H3"
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 137. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
