# active_site_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 156 (Acyl-thioester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSVKKAGVLGATGSVGQRFILLLSKHPEFEIHALGASSRSAGKKYKDAASWKQTETLPETEQDIVVQECKPEGNFLECDVVFSGLDADVAGDIEKSFVEAGLAVVSNAKNYRREKDVPLVVPIVNPEHIDVVENKVKQAVSKGGKKPGFIICISNCSTAGLVAPLKPLVEKFGPIDALTTTTLQAISGAGFSPGVSGMDILDNIVPYISGEEDKLEWETKKILGGVNAEGTEFVPIPESEMKVSAQCNRVPVIDGHTECISLRFANRPAPSVEDVKQCLREYECAASKLGCHSAPKQTIHVLDQPDRPQPRLDRDRDSGYGVSVGRIREDSLLDFKMVVLSHNTIIGAAGAGILIAEILKAKNII

[Multiple Choices]
A. Position 1141 (Proton donor; for dehydratase activity 1)
B. Position 215 (Proton acceptor)
C. Position 156 (Acyl-thioester intermediate)
D. Position 308 (Proton acceptor)
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

> The supplied sequence exactly matches the 365-residue UniProt entry, whose active-site annotation identifies position 156 as forming an acyl-thioester intermediate. This supports choice C as a database annotation, though the cited evidence is computationally assigned via PIRSR rather than direct experimental evidence for this residue.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a cysteine-containing region that may be consistent with catalytic chemistry, but sequence inspection alone does not establish that position 156 forms an acyl-thioester intermediate or distinguish that precise annotation from the other proposed roles.


**Missing item-specific fact**

> The protein-specific mapping of position 156 to the acyl-thioester intermediate, or equivalent structural, experimental, or curated active-site information.


**Reason**

> The key distinction depends on a residue-specific catalytic annotation not stated in the question. Knowing the exact sequence or using generic sequence heuristics does not independently establish the annotated role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database record supports the position and role stated in C; it annotates the proton acceptor at position 256, not the positions in B or D.


### Important caveats

- The active-site annotation is supported by a computational PIRSR evidence code; the cited excerpts do not independently establish it through direct residue-specific experimentation.
- The sequence match and annotation are reviewer-only evidence and were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-containing region that may be consistent with catalytic chemistry, but sequence inspection alone does not establish that position 156 forms an acyl-thioester intermediate or distinguish that precise annotation from the other proposed roles.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific mapping of position 156 to the acyl-thioester intermediate, or equivalent structural, experimental, or curated active-site information.",
    "reason": "The key distinction depends on a residue-specific catalytic annotation not stated in the question. Knowing the exact sequence or using generic sequence heuristics does not independently establish the annotated role."
  },
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 365-residue UniProt entry, whose active-site annotation identifies position 156 as forming an acyl-thioester intermediate. This supports choice C as a database annotation, though the cited evidence is computationally assigned via PIRSR rather than direct experimental evidence for this residue."
  },
  "important_caveats": [
    "The active-site annotation is supported by a computational PIRSR evidence code; the cited excerpts do not independently establish it through direct residue-specific experimentation.",
    "The sequence match and annotation are reviewer-only evidence and were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database record supports the position and role stated in C; it annotates the proton acceptor at position 256, not the positions in B or D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 365-residue UniProt entry, whose active-site annotation identifies position 156 as forming an acyl-thioester intermediate. This supports choice C as a database annotation, though the cited evidence is computationally assigned via PIRSR rather than direct experimental evidence for this residue.",
    "evidence_ids": ["C1", "C5", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a cysteine-containing region that may be consistent with catalytic chemistry, but sequence inspection alone does not establish that position 156 forms an acyl-thioester intermediate or distinguish that precise annotation from the other proposed roles.",
    "missing_item_specific_fact": "The protein-specific mapping of position 156 to the acyl-thioester intermediate, or equivalent structural, experimental, or curated active-site information.",
    "reason": "The key distinction depends on a residue-specific catalytic annotation not stated in the question. Knowing the exact sequence or using generic sequence heuristics does not independently establish the annotated role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database record supports the position and role stated in C; it annotates the proton acceptor at position 256, not the positions in B or D."
  },
  "important_caveats": [
    "The active-site annotation is supported by a computational PIRSR evidence code; the cited excerpts do not independently establish it through direct residue-specific experimentation.",
    "The sequence match and annotation are reviewer-only evidence and were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence C5, H8). The residue at position 156 in the supplied 365-aa sequence is C (Cysteine), chemically consistent with thioester intermediate formation. The annotation is based on PIRSF pattern similarity (ECO:0000255, PIRSR000148-1) rather than direct experimental mutagenesis of this specific residue, but the PDB structure 3HSK (2.2 Å, in complex with NADP+) provides experimental structural context for the enzyme's catalytic architecture.

Citations as saved: [C5](#evidence-c5), [H8](#evidence-h8), [C22](#evidence-c22), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A concrete multi-step reasoning chain distinguishes the answer from the supplied sequence alone: (1) The protein is 365 residues long, immediately eliminating Choice A (position 1141 does not exist). (2) An 'acyl-thioester intermediate' can only be formed by a nucleophilic residue bearing a thiol or hydroxyl group (Cys or Ser). Checking the residue at each candidate position: position 156 = C (Cys), position 215 = L (Leu), position 308 = D (Asp). Only Cys at 156 is chemically capable of forming a thioester. (3) Leucine at 215 cannot act as a proton acceptor, eliminating B. (4) While Asp at 308 could in principle accept a proton, in NAD(P)-dependent semialdehyde dehydrogenases (identifiable from the N-terminal Rossmann-fold GxGxxG motif 'ATGSVGQR' at positions 11-17 and the overall fold architecture), the catalytic proton acceptor is a histidine (position 256 = His), not aspartate. The Cys-His catalytic dyad is the hallmark of this enzyme family.


**Missing item-specific fact**

> Precise identification of which cysteine among the several present in the sequence (positions 70, 79, 152, 156, 248, 260, 279, 285, 292) is the catalytic one requires either recognizing the conserved 'CISNCST' motif of the semialdehyde dehydrogenase PIRSF pattern or knowing the UniProt annotation. However, the chemical-capability filter (only Cys can form a thioester) combined with elimination of other choices by residue identity is sufficient to arrive at C without memorizing the database entry.


**Reason**

> The question provides enough information (the full sequence plus the stated functional role in each option) to apply basic biochemical reasoning: match residue chemistry to stated function, eliminate impossible positions, and use family-level mechanistic knowledge (Cys-His dyad in semialdehyde dehydrogenases). The discriminating step—recognizing that only Cys forms thioesters—is general biochemistry, not an item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is eliminated by sequence length. Choice B is eliminated because Leu cannot be a proton acceptor. Choice D is weakly defensible in isolation (Asp can accept a proton) but is inconsistent with the known Cys-His catalytic mechanism of semialdehyde dehydrogenases and is not the annotated active site. Choice C is the only option where the residue identity (Cys) matches the stated chemical function (thioester formation). No genuine ambiguity remains.


### Important caveats

- The active-site annotation (ECO:0000255, PIRSR000148-1) is pattern-similarity-based, not derived from site-directed mutagenesis of C156 in this specific Candida albicans enzyme. However, the PDB structure 3HSK (2.2 Å) provides experimental structural evidence for the enzyme's active-site architecture.
- The question presents only single-residue options rather than the full catalytic center (Cys156 + His256 dyad), which is a simplification but does not create ambiguity among the given choices.
- The UniProt entry was first released 2025-02-05; the author's exact source snapshot is unknown, though sequence version 1 has been unchanged since 2005-04-26.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A concrete multi-step reasoning chain distinguishes the answer from the supplied sequence alone: (1) The protein is 365 residues long, immediately eliminating Choice A (position 1141 does not exist). (2) An 'acyl-thioester intermediate' can only be formed by a nucleophilic residue bearing a thiol or hydroxyl group (Cys or Ser). Checking the residue at each candidate position: position 156 = C (Cys), position 215 = L (Leu), position 308 = D (Asp). Only Cys at 156 is chemically capable of forming a thioester. (3) Leucine at 215 cannot act as a proton acceptor, eliminating B. (4) While Asp at 308 could in principle accept a proton, in NAD(P)-dependent semialdehyde dehydrogenases (identifiable from the N-terminal Rossmann-fold GxGxxG motif 'ATGSVGQR' at positions 11-17 and the overall fold architecture), the catalytic proton acceptor is a histidine (position 256 = His), not aspartate. The Cys-His catalytic dyad is the hallmark of this enzyme family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of which cysteine among the several present in the sequence (positions 70, 79, 152, 156, 248, 260, 279, 285, 292) is the catalytic one requires either recognizing the conserved 'CISNCST' motif of the semialdehyde dehydrogenase PIRSF pattern or knowing the UniProt annotation. However, the chemical-capability filter (only Cys can form a thioester) combined with elimination of other choices by residue identity is sufficient to arrive at C without memorizing the database entry.",
    "reason": "The question provides enough information (the full sequence plus the stated functional role in each option) to apply basic biochemical reasoning: match residue chemistry to stated function, eliminate impossible positions, and use family-level mechanistic knowledge (Cys-His dyad in semialdehyde dehydrogenases). The discriminating step—recognizing that only Cys forms thioesters—is general biochemistry, not an item-specific lookup."
  },
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H8",
      "C22",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence C5, H8). The residue at position 156 in the supplied 365-aa sequence is C (Cysteine), chemically consistent with thioester intermediate formation. The annotation is based on PIRSF pattern similarity (ECO:0000255, PIRSR000148-1) rather than direct experimental mutagenesis of this specific residue, but the PDB structure 3HSK (2.2 Å, in complex with NADP+) provides experimental structural context for the enzyme's catalytic architecture."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000255, PIRSR000148-1) is pattern-similarity-based, not derived from site-directed mutagenesis of C156 in this specific Candida albicans enzyme. However, the PDB structure 3HSK (2.2 Å) provides experimental structural evidence for the enzyme's active-site architecture.",
    "The question presents only single-residue options rather than the full catalytic center (Cys156 + His256 dyad), which is a simplification but does not create ambiguity among the given choices.",
    "The UniProt entry was first released 2025-02-05; the author's exact source snapshot is unknown, though sequence version 1 has been unchanged since 2005-04-26."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is eliminated by sequence length. Choice B is eliminated because Leu cannot be a proton acceptor. Choice D is weakly defensible in isolation (Asp can accept a proton) but is inconsistent with the known Cys-His catalytic mechanism of semialdehyde dehydrogenases and is not the annotated active site. Choice C is the only option where the residue identity (Cys) matches the stated chemical function (thioester formation). No genuine ambiguity remains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5ALM0 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, Candida albicans) annotates position 156 as 'Acyl-thioester intermediate' active site (evidence C5, H8). The residue at position 156 in the supplied 365-aa sequence is C (Cysteine), chemically consistent with thioester intermediate formation. The annotation is based on PIRSF pattern similarity (ECO:0000255, PIRSR000148-1) rather than direct experimental mutagenesis of this specific residue, but the PDB structure 3HSK (2.2 Å, in complex with NADP+) provides experimental structural context for the enzyme's catalytic architecture.",
    "evidence_ids": ["C5", "H8", "C22", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A concrete multi-step reasoning chain distinguishes the answer from the supplied sequence alone: (1) The protein is 365 residues long, immediately eliminating Choice A (position 1141 does not exist). (2) An 'acyl-thioester intermediate' can only be formed by a nucleophilic residue bearing a thiol or hydroxyl group (Cys or Ser). Checking the residue at each candidate position: position 156 = C (Cys), position 215 = L (Leu), position 308 = D (Asp). Only Cys at 156 is chemically capable of forming a thioester. (3) Leucine at 215 cannot act as a proton acceptor, eliminating B. (4) While Asp at 308 could in principle accept a proton, in NAD(P)-dependent semialdehyde dehydrogenases (identifiable from the N-terminal Rossmann-fold GxGxxG motif 'ATGSVGQR' at positions 11-17 and the overall fold architecture), the catalytic proton acceptor is a histidine (position 256 = His), not aspartate. The Cys-His catalytic dyad is the hallmark of this enzyme family.",
    "missing_item_specific_fact": "Precise identification of which cysteine among the several present in the sequence (positions 70, 79, 152, 156, 248, 260, 279, 285, 292) is the catalytic one requires either recognizing the conserved 'CISNCST' motif of the semialdehyde dehydrogenase PIRSF pattern or knowing the UniProt annotation. However, the chemical-capability filter (only Cys can form a thioester) combined with elimination of other choices by residue identity is sufficient to arrive at C without memorizing the database entry.",
    "reason": "The question provides enough information (the full sequence plus the stated functional role in each option) to apply basic biochemical reasoning: match residue chemistry to stated function, eliminate impossible positions, and use family-level mechanistic knowledge (Cys-His dyad in semialdehyde dehydrogenases). The discriminating step—recognizing that only Cys forms thioesters—is general biochemistry, not an item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is eliminated by sequence length. Choice B is eliminated because Leu cannot be a proton acceptor. Choice D is weakly defensible in isolation (Asp can accept a proton) but is inconsistent with the known Cys-His catalytic mechanism of semialdehyde dehydrogenases and is not the annotated active site. Choice C is the only option where the residue identity (Cys) matches the stated chemical function (thioester formation). No genuine ambiguity remains."
  },
  "important_caveats": [
    "The active-site annotation (ECO:0000255, PIRSR000148-1) is pattern-similarity-based, not derived from site-directed mutagenesis of C156 in this specific Candida albicans enzyme. However, the PDB structure 3HSK (2.2 Å) provides experimental structural evidence for the enzyme's active-site architecture.",
    "The question presents only single-residue options rather than the full catalytic center (Cys156 + His256 dyad), which is a simplification but does not create ambiguity among the given choices.",
    "The UniProt entry was first released 2025-02-05; the author's exact source snapshot is unknown, though sequence version 1 has been unchanged since 2005-04-26."
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

**Accession:** `Q5ALM0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 145. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
"Q5ALM0"
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"description":"Acyl-thioester intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR000148-1","source":"PIRSR"}],"location":{"end":{"modifier":"EXACT","value":156},"start":{"modifier":"EXACT","value":156}},"type":"Active site"}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5ALM0.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:05.955388+00:00.  

```json
{"citation":{"authors":["Arachea B.T.","Liu X.","Pavlovsky A.G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"20124701"},{"database":"DOI","id":"10.1107/s0907444909052834"}],"citationType":"journal article","firstPage":"205","id":"20124701","journal":"Acta Crystallogr. D","lastPage":"212","publicationDate":"2010","title":"Expansion of the aspartate beta-semialdehyde dehydrogenase family: the first structure of a fungal ortholog.","volume":"66"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3HSK","source":"PDB"}],"referenceNumber":8,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `8c276c69d39d476d3057ea3296988bd426dcdaf03f794873fbb8acd887c2353f`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 75-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
RN   [8] {ECO:0007744|PDB:3HSK}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,
RP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, AND SUBUNIT.
RX   PubMed=20124701; DOI=10.1107/s0907444909052834;
RA   Arachea B.T., Liu X., Pavlovsky A.G., Viola R.E.;
RT   "Expansion of the aspartate beta-semialdehyde dehydrogenase family: the
RT   first structure of a fungal ortholog.";
RL   Acta Crystallogr. D 66:205-212(2010).
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5ALM0?format=txt&versions=145)  
**Locator:** `lines 194-196`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 145 / 1.  
**Retrieved:** 2026-11-02T04:31:09.278811+00:00.  

```text
FT   ACT_SITE        156
FT                   /note="Acyl-thioester intermediate"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR000148-1"
```

Source SHA-256: `ab9c01417c6f2a032f2631374121e35ba1fcae8b50dee37db4c6262ccf31884d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
