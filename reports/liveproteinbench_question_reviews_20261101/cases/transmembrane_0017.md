# transmembrane_0017

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 305..325

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQFNSLVLLAGATILSPFVQAQTWTTCNPLNETCPNDPALGTNHTFVFNTSSTVTDYYNITAGSLTYGDDGAEFTIAKQGQSPTIQSKFYIFFGQVSVIMKAATGVGIVSSIVLESDDLDEIDWEFIGGNDTHAETNYFGKGNTTSYDRAIWYPTPSDPTANFHNYTVDWTAERVQWWIDDSLVRTLAYADAVDGKNFPQTPMTVRLGIWSGGDPKGNSQGTIEWAGGETDFTKVPFTMYVKSAAVQDYSTGSEYEWTDKTGDWTSIKVISGNSTVAETITKNETPTLSLGEKWDNLPKTTKLAVYCGGGAAVAALVSAFLFTFLRQRRNGRLEREAYNQLIEKQQQDAYKDQMELHNKGIGGFDNNSYATQGDDALGGWGSNQGTGYVGPSGSASAMASGSPMVQAGQHGPMSPTMVMRNGEMSPHSAEFPQPQQPMFGGSANGGSYMKM

[Multiple Choices]
A. 305..325; 704..727
B. 301..328
C. 305..325
D. 483..503
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches a UniProt record annotating residues 305–325 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not evidence of an experimental measurement.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a strongly hydrophobic stretch around residues 305–325, making a membrane-spanning helix plausible and distinguishing this region from the out-of-range choices. But sequence composition alone does not establish the precise endpoints or decide between C and the broader B interval.


**Missing item-specific fact**

> The protein-specific transmembrane-region annotation or an equivalent prediction specifying its boundaries.


**Reason**

> The sequence supports a likely membrane-spanning helix, but selecting the exact annotated boundaries requires a protein-specific boundary assignment absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> C matches the annotated 305–325 boundaries. B is a broader interval that includes the same hydrophobic segment; the wording asks for a segment that crosses the membrane without specifying how tightly its endpoints must match the helix.


### Important caveats

- Reviewer-only database evidence supports the key but was not available to the evaluated model.
- The cited transmembrane annotation is computational, not established here as experimentally determined.
- The source record sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a strongly hydrophobic stretch around residues 305–325, making a membrane-spanning helix plausible and distinguishing this region from the out-of-range choices. But sequence composition alone does not establish the precise endpoints or decide between C and the broader B interval.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation or an equivalent prediction specifying its boundaries.",
    "reason": "The sequence supports a likely membrane-spanning helix, but selecting the exact annotated boundaries requires a protein-specific boundary assignment absent from the input."
  },
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt record annotating residues 305–325 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not evidence of an experimental measurement."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The cited transmembrane annotation is computational, not established here as experimentally determined.",
    "The source record sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "C matches the annotated 305–325 boundaries. B is a broader interval that includes the same hydrophobic segment; the wording asks for a segment that crosses the membrane without specifying how tightly its endpoints must match the helix."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt record annotating residues 305–325 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not evidence of an experimental measurement.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a strongly hydrophobic stretch around residues 305–325, making a membrane-spanning helix plausible and distinguishing this region from the out-of-range choices. But sequence composition alone does not establish the precise endpoints or decide between C and the broader B interval.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation or an equivalent prediction specifying its boundaries.",
    "reason": "The sequence supports a likely membrane-spanning helix, but selecting the exact annotated boundaries requires a protein-specific boundary assignment absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "C matches the annotated 305–325 boundaries. B is a broader interval that includes the same hydrophobic segment; the wording asks for a segment that crosses the membrane without specifying how tightly its endpoints must match the helix."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The cited transmembrane annotation is computational, not established here as experimentally determined.",
    "The source record sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB annotation for A0A384K4T0 (CRH2_BOTFB, Botrytis cinerea Crh-like protein 2, 451 AA) explicitly annotates a Transmembrane helical feature at positions 305..325 (evidence C5 and H3). The sequence SHA256 matches the benchmark input. However, the evidence code is ECO:0000255 (inferred by similarity), indicating a computational/transferred annotation rather than an experimental determination. The annotation is nonetheless the authoritative database entry for this sequence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C2](#evidence-c2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options A (704..727) and D (483..503) reference positions beyond the 451-residue protein and are trivially eliminated. The substantive choice is B (301..328) vs C (305..325). Option B includes a lysine (K302) near the N-terminus and arginine/arginine (R326, R328) plus glutamine (Q327) at the C-terminus of the proposed helix. Charged residues (K, R) are energetically incompatible with the hydrophobic interior of a lipid bilayer and are hallmarks of transmembrane helix boundaries, not helix cores. Option C (305..325) excludes these charged residues, retaining a predominantly hydrophobic segment (VYCGGGAAVAALVSAFLFTFL). A student applying the general principle that TM helices must be hydrophobic and avoid buried charges can meaningfully prefer C over B.


**Missing item-specific fact**

> The precise boundary residues (why 305 rather than 304, why 325 rather than 326) are set by a similarity-based prediction (ECO:0000255) rather than experimental data, so the exact endpoints carry some arbitrariness. However, the distinction from option B does not depend on knowing the exact annotation—it follows from the hydrophobicity principle.


**Reason**

> The elimination of A and D is trivial (positions exceed protein length). The B-vs-C distinction is supported by a general biological principle: transmembrane helices are hydrophobic and exclude charged residues. Option B's inclusion of K302, R326, and R328 is inconsistent with a TM helix, while C's boundaries avoid these. This provides a concrete, general-knowledge-based argument without requiring memorization of the specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D are impossible (positions exceed the 451-residue protein). Between B and C, the presence of multiple charged residues in B provides a clear biological disqualifier for a TM helix. While the exact boundaries of C are set by a similarity-based annotation and a slightly different hydrophobic core (e.g., 311-325) could be argued, no other option is defensible given the choices provided.


### Important caveats

- The TM annotation carries evidence code ECO:0000255 (inferred by similarity to Q8J0P4), not experimental verification. The 'correct' boundaries are a computational prediction transferred from a homolog.
- The region 305-325 includes a GGG tripeptide (308-310) which is atypical for a TM helix; the most hydrophobic core is arguably 311-325. The annotation boundaries reflect the similarity-based transfer rather than a from-scratch hydropathy analysis.
- The UniProt entry was first public on 2025-06-18 (entry version 29 as of retrieval); the author's source snapshot date is unknown but the sequence version has been unchanged since 2018-11-07.
- Options A and D are trivially impossible distractors (positions >451), reducing the effective discrimination to B vs C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options A (704..727) and D (483..503) reference positions beyond the 451-residue protein and are trivially eliminated. The substantive choice is B (301..328) vs C (305..325). Option B includes a lysine (K302) near the N-terminus and arginine/arginine (R326, R328) plus glutamine (Q327) at the C-terminus of the proposed helix. Charged residues (K, R) are energetically incompatible with the hydrophobic interior of a lipid bilayer and are hallmarks of transmembrane helix boundaries, not helix cores. Option C (305..325) excludes these charged residues, retaining a predominantly hydrophobic segment (VYCGGGAAVAALVSAFLFTFL). A student applying the general principle that TM helices must be hydrophobic and avoid buried charges can meaningfully prefer C over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise boundary residues (why 305 rather than 304, why 325 rather than 326) are set by a similarity-based prediction (ECO:0000255) rather than experimental data, so the exact endpoints carry some arbitrariness. However, the distinction from option B does not depend on knowing the exact annotation—it follows from the hydrophobicity principle.",
    "reason": "The elimination of A and D is trivial (positions exceed protein length). The B-vs-C distinction is supported by a general biological principle: transmembrane helices are hydrophobic and exclude charged residues. Option B's inclusion of K302, R326, and R328 is inconsistent with a TM helix, while C's boundaries avoid these. This provides a concrete, general-knowledge-based argument without requiring memorization of the specific database entry."
  },
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C2"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB annotation for A0A384K4T0 (CRH2_BOTFB, Botrytis cinerea Crh-like protein 2, 451 AA) explicitly annotates a Transmembrane helical feature at positions 305..325 (evidence C5 and H3). The sequence SHA256 matches the benchmark input. However, the evidence code is ECO:0000255 (inferred by similarity), indicating a computational/transferred annotation rather than an experimental determination. The annotation is nonetheless the authoritative database entry for this sequence."
  },
  "important_caveats": [
    "The TM annotation carries evidence code ECO:0000255 (inferred by similarity to Q8J0P4), not experimental verification. The 'correct' boundaries are a computational prediction transferred from a homolog.",
    "The region 305-325 includes a GGG tripeptide (308-310) which is atypical for a TM helix; the most hydrophobic core is arguably 311-325. The annotation boundaries reflect the similarity-based transfer rather than a from-scratch hydropathy analysis.",
    "The UniProt entry was first public on 2025-06-18 (entry version 29 as of retrieval); the author's source snapshot date is unknown but the sequence version has been unchanged since 2018-11-07.",
    "Options A and D are trivially impossible distractors (positions >451), reducing the effective discrimination to B vs C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are impossible (positions exceed the 451-residue protein). Between B and C, the presence of multiple charged residues in B provides a clear biological disqualifier for a TM helix. While the exact boundaries of C are set by a similarity-based annotation and a slightly different hydrophobic core (e.g., 311-325) could be argued, no other option is defensible given the choices provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB annotation for A0A384K4T0 (CRH2_BOTFB, Botrytis cinerea Crh-like protein 2, 451 AA) explicitly annotates a Transmembrane helical feature at positions 305..325 (evidence C5 and H3). The sequence SHA256 matches the benchmark input. However, the evidence code is ECO:0000255 (inferred by similarity), indicating a computational/transferred annotation rather than an experimental determination. The annotation is nonetheless the authoritative database entry for this sequence.",
    "evidence_ids": ["C5", "H3", "C1", "C2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options A (704..727) and D (483..503) reference positions beyond the 451-residue protein and are trivially eliminated. The substantive choice is B (301..328) vs C (305..325). Option B includes a lysine (K302) near the N-terminus and arginine/arginine (R326, R328) plus glutamine (Q327) at the C-terminus of the proposed helix. Charged residues (K, R) are energetically incompatible with the hydrophobic interior of a lipid bilayer and are hallmarks of transmembrane helix boundaries, not helix cores. Option C (305..325) excludes these charged residues, retaining a predominantly hydrophobic segment (VYCGGGAAVAALVSAFLFTFL). A student applying the general principle that TM helices must be hydrophobic and avoid buried charges can meaningfully prefer C over B.",
    "missing_item_specific_fact": "The precise boundary residues (why 305 rather than 304, why 325 rather than 326) are set by a similarity-based prediction (ECO:0000255) rather than experimental data, so the exact endpoints carry some arbitrariness. However, the distinction from option B does not depend on knowing the exact annotation—it follows from the hydrophobicity principle.",
    "reason": "The elimination of A and D is trivial (positions exceed protein length). The B-vs-C distinction is supported by a general biological principle: transmembrane helices are hydrophobic and exclude charged residues. Option B's inclusion of K302, R326, and R328 is inconsistent with a TM helix, while C's boundaries avoid these. This provides a concrete, general-knowledge-based argument without requiring memorization of the specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D are impossible (positions exceed the 451-residue protein). Between B and C, the presence of multiple charged residues in B provides a clear biological disqualifier for a TM helix. While the exact boundaries of C are set by a similarity-based annotation and a slightly different hydrophobic core (e.g., 311-325) could be argued, no other option is defensible given the choices provided."
  },
  "important_caveats": [
    "The TM annotation carries evidence code ECO:0000255 (inferred by similarity to Q8J0P4), not experimental verification. The 'correct' boundaries are a computational prediction transferred from a homolog.",
    "The region 305-325 includes a GGG tripeptide (308-310) which is atypical for a TM helix; the most hydrophobic core is arguably 311-325. The annotation boundaries reflect the similarity-based transfer rather than a from-scratch hydropathy analysis.",
    "The UniProt entry was first public on 2025-06-18 (entry version 29 as of retrieval); the author's source snapshot date is unknown but the sequence version has been unchanged since 2018-11-07.",
    "Options A and D are trivially impossible distractors (positions >451), reducing the effective discrimination to B vs C."
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

**Accession:** `A0A384K4T0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 27. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.289455+00:00.  

```json
"A0A384K4T0"
```

Source SHA-256: `ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca`.

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)  
**Locator:** `/entryAudit`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.289455+00:00.  

```json
{"entryVersion":29,"firstPublicDate":"2025-06-18","lastAnnotationUpdateDate":"2026-09-02","lastSequenceUpdateDate":"2018-11-07","sequenceVersion":1}
```

Source SHA-256: `ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.289455+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":325},"start":{"modifier":"EXACT","value":305}},"type":"Transmembrane"}
```

Source SHA-256: `ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-01T06:27:27.918229+00:00.  

```text
FT   TRANSMEM        305..325
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
