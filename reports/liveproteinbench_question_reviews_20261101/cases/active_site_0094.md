# active_site_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 154 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSDNTPTPQKNPDTNPYASLISQQIAIIPSFTLESGVTLNNVPVAYKTWGKLNEKADNCLVICHALTGSADVEDWWGPLLGLNKAFDPTRFFIFCGNVIGSPYGTISSVTTNPETGKPFGPEMPGSSVKDDVRLHYIILKSLGVRSVAAVVGGSMGGMTVLEYPLNTPPGFVRAIIPLATSARHSAWCISWGEAQRQSIYSDPDYKDGYYYEIEEEGGKVDLARQPARGLAAARMAALLTYRSRDSFESRFGRRAGGGKSSVPKGGVRIMGGQETTDPSVPSESDLAAKSPSWRAWREHNDGHRSAGARPISRSGSEGPAHREGDAAQAEVVKTQDVKANGNKIGTGGEAPPKIFSAQSYLRYQGDKFTGRFDANCYIHITRKLDTHDLSAPSRDTSLSSLSSGLPSSPDATEEELNARLIHALSLEPPALVIGIESDGLFTTSEQRELAAGIPDAELVVIPSPDGHDGFLLEFEAINGWVEGWLKRKMPEFYERRVINPEEYVQGEEGFGIKKESVFGEAEADVTRW

[Multiple Choices]
A. Position 119 (For glutaminase activity)
B. Position 2428 (For thioesterase activity)
C. Position 215 (1)
D. Position 154 (Nucleophile)
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

> The matched UniProt entry annotates residue 154 as the nucleophile. The annotation is supported by transfer from a homolog and a family rule, not by direct experimental evidence shown here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is 528 residues long, so position 2428 is out of range; however, that does not establish which in-range residue is the catalytic nucleophile.


**Missing item-specific fact**

> The protein-specific assignment of residue 154 as the nucleophile, or equivalent validated homology/family annotation, is not supplied in the question.


**Reason**

> The sequence and choices alone do not provide a clear, defensible way to identify the precise catalytic residue. Knowing or inferring the protein family would still require a specific active-site assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, D is the only one supported by the matched annotation. But the prompt describes identifying the residues forming the catalytic center, while D gives only one residue; the entry also annotates active-site residues 438 and 467.


### Important caveats

- The sequence matches the cited UniProt record, and the annotation uses canonical sequence numbering.
- The evidence supports an annotation, not direct experimental validation of residue 154 in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is 528 residues long, so position 2428 is out of range; however, that does not establish which in-range residue is the catalytic nucleophile.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of residue 154 as the nucleophile, or equivalent validated homology/family annotation, is not supplied in the question.",
    "reason": "The sequence and choices alone do not provide a clear, defensible way to identify the precise catalytic residue. Knowing or inferring the protein family would still require a specific active-site assignment."
  },
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates residue 154 as the nucleophile. The annotation is supported by transfer from a homolog and a family rule, not by direct experimental evidence shown here."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, and the annotation uses canonical sequence numbering.",
    "The evidence supports an annotation, not direct experimental validation of residue 154 in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, D is the only one supported by the matched annotation. But the prompt describes identifying the residues forming the catalytic center, while D gives only one residue; the entry also annotates active-site residues 438 and 467."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates residue 154 as the nucleophile. The annotation is supported by transfer from a homolog and a family rule, not by direct experimental evidence shown here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is 528 residues long, so position 2428 is out of range; however, that does not establish which in-range residue is the catalytic nucleophile.",
    "missing_item_specific_fact": "The protein-specific assignment of residue 154 as the nucleophile, or equivalent validated homology/family annotation, is not supplied in the question.",
    "reason": "The sequence and choices alone do not provide a clear, defensible way to identify the precise catalytic residue. Knowing or inferring the protein family would still require a specific active-site assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, D is the only one supported by the matched annotation. But the prompt describes identifying the residues forming the catalytic center, while D gives only one residue; the entry also annotates active-site residues 438 and 467."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, and the annotation uses canonical sequence numbering.",
    "The evidence supports an annotation, not direct experimental validation of residue 154 in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VIY8 (Homoserine O-acetyltransferase, EC 2.3.1.31, MET2_CRYN9) annotates position 154 as an Active site with the description 'Nucleophile' (evidence codes ECO:0000250 similarity to O60062, ECO:0000255 PIRSR000443-1). The supplied 528-aa sequence matches the UniProt sequence (SHA-256 confirmed). Position 154 in the sequence is Serine (S), consistent with a nucleophilic residue in an acyltransferase active site. The annotation is computational (transferred by similarity and PIRSR pattern) rather than direct site-directed mutagenesis, but the PubMed reference (17353245) provides experimental characterization of the enzyme's catalytic function. No contradicting evidence exists.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C8](#evidence-c8), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B (position 2428) is immediately eliminated because the protein is only 528 residues long. Option A (position 119, 'glutaminase activity') is eliminated because the sequence contains GNAT-family acetyltransferase hallmarks (the GGSMGG P-loop motif around residues 152-157) and no glutaminase motifs; the enzyme class is inconsistent. Option C (position 215, '(1)') provides no meaningful catalytic-role descriptor and position 215 is Glutamic acid, not a typical nucleophile. Option D (position 154, 'Nucleophile') aligns with the Ser residue embedded in the conserved GGSMGG motif characteristic of the GNAT fold, where a serine can serve as a nucleophile attacking the acetyl-CoA thioester. A model familiar with GNAT acetyltransferase architecture can recognize the P-loop and assign the nucleophilic role to the serine within it.


**Missing item-specific fact**

> Precise discrimination among the three annotated active sites (154, 438, 467) as THE nucleophile requires knowledge of the GNAT P-loop geometry and which specific residue in the motif acts as nucleophile versus substrate-binding or CoA-binding residues. However, only position 154 appears among the answer choices, so this granularity is not strictly needed to select D.


**Reason**

> General biological reasoning eliminates B (out-of-range position) and A (wrong enzyme class). Recognition of the GGSMGG GNAT P-loop and the chemical logic of serine as nucleophile in acyltransferase catalysis provides a defensible argument for D over C. The '(1)' notation in C is uninformative. While deeper mechanistic knowledge of GNAT active-site topology would strengthen confidence, the available sequence features and chemical reasoning are sufficient to distinguish D from the other options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is impossible (position exceeds sequence length). Option A names a wrong enzyme class. Option C's '(1)' descriptor is non-informative and the residue (Glu215) is not a canonical nucleophile. Only D provides a chemically coherent nucleophile assignment at a recognizable motif position. No other option is defensible.


### Important caveats

- The active-site annotation at position 154 is based on computational evidence (similarity to O60062 and PIRSR pattern match, ECO:0000250/255), not direct experimental mutagenesis of this specific protein. The PubMed reference (17353245) experimentally characterizes the enzyme's catalytic function but the residue-level nucleophile assignment is transferred.
- The UniProt entry also annotates active sites at positions 438 and 467 without the 'Nucleophile' label; a model aware of these additional sites might question whether 154 is the sole or primary nucleophile, though only 154 appears in the answer choices.
- The sequence was first released in UniProt on 2025-02-05; the author's data-construction date and exact source snapshot are unknown, though the historical entry version 54 (released 2026-01-28) already contains the position-154 annotation.
- Option C's '(1)' notation is ambiguous and may be a formatting artifact; it does not clearly describe a catalytic role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (position 2428) is immediately eliminated because the protein is only 528 residues long. Option A (position 119, 'glutaminase activity') is eliminated because the sequence contains GNAT-family acetyltransferase hallmarks (the GGSMGG P-loop motif around residues 152-157) and no glutaminase motifs; the enzyme class is inconsistent. Option C (position 215, '(1)') provides no meaningful catalytic-role descriptor and position 215 is Glutamic acid, not a typical nucleophile. Option D (position 154, 'Nucleophile') aligns with the Ser residue embedded in the conserved GGSMGG motif characteristic of the GNAT fold, where a serine can serve as a nucleophile attacking the acetyl-CoA thioester. A model familiar with GNAT acetyltransferase architecture can recognize the P-loop and assign the nucleophilic role to the serine within it.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise discrimination among the three annotated active sites (154, 438, 467) as THE nucleophile requires knowledge of the GNAT P-loop geometry and which specific residue in the motif acts as nucleophile versus substrate-binding or CoA-binding residues. However, only position 154 appears among the answer choices, so this granularity is not strictly needed to select D.",
    "reason": "General biological reasoning eliminates B (out-of-range position) and A (wrong enzyme class). Recognition of the GGSMGG GNAT P-loop and the chemical logic of serine as nucleophile in acyltransferase catalysis provides a defensible argument for D over C. The '(1)' notation in C is uninformative. While deeper mechanistic knowledge of GNAT active-site topology would strengthen confidence, the available sequence features and chemical reasoning are sufficient to distinguish D from the other options."
  },
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C8",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VIY8 (Homoserine O-acetyltransferase, EC 2.3.1.31, MET2_CRYN9) annotates position 154 as an Active site with the description 'Nucleophile' (evidence codes ECO:0000250 similarity to O60062, ECO:0000255 PIRSR000443-1). The supplied 528-aa sequence matches the UniProt sequence (SHA-256 confirmed). Position 154 in the sequence is Serine (S), consistent with a nucleophilic residue in an acyltransferase active site. The annotation is computational (transferred by similarity and PIRSR pattern) rather than direct site-directed mutagenesis, but the PubMed reference (17353245) provides experimental characterization of the enzyme's catalytic function. No contradicting evidence exists."
  },
  "important_caveats": [
    "The active-site annotation at position 154 is based on computational evidence (similarity to O60062 and PIRSR pattern match, ECO:0000250/255), not direct experimental mutagenesis of this specific protein. The PubMed reference (17353245) experimentally characterizes the enzyme's catalytic function but the residue-level nucleophile assignment is transferred.",
    "The UniProt entry also annotates active sites at positions 438 and 467 without the 'Nucleophile' label; a model aware of these additional sites might question whether 154 is the sole or primary nucleophile, though only 154 appears in the answer choices.",
    "The sequence was first released in UniProt on 2025-02-05; the author's data-construction date and exact source snapshot are unknown, though the historical entry version 54 (released 2026-01-28) already contains the position-154 annotation.",
    "Option C's '(1)' notation is ambiguous and may be a formatting artifact; it does not clearly describe a catalytic role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is impossible (position exceeds sequence length). Option A names a wrong enzyme class. Option C's '(1)' descriptor is non-informative and the residue (Glu215) is not a canonical nucleophile. Only D provides a chemically coherent nucleophile assignment at a recognizable motif position. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VIY8 (Homoserine O-acetyltransferase, EC 2.3.1.31, MET2_CRYN9) annotates position 154 as an Active site with the description 'Nucleophile' (evidence codes ECO:0000250 similarity to O60062, ECO:0000255 PIRSR000443-1). The supplied 528-aa sequence matches the UniProt sequence (SHA-256 confirmed). Position 154 in the sequence is Serine (S), consistent with a nucleophilic residue in an acyltransferase active site. The annotation is computational (transferred by similarity and PIRSR pattern) rather than direct site-directed mutagenesis, but the PubMed reference (17353245) provides experimental characterization of the enzyme's catalytic function. No contradicting evidence exists.",
    "evidence_ids": ["C5", "H3", "C4", "C8", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B (position 2428) is immediately eliminated because the protein is only 528 residues long. Option A (position 119, 'glutaminase activity') is eliminated because the sequence contains GNAT-family acetyltransferase hallmarks (the GGSMGG P-loop motif around residues 152-157) and no glutaminase motifs; the enzyme class is inconsistent. Option C (position 215, '(1)') provides no meaningful catalytic-role descriptor and position 215 is Glutamic acid, not a typical nucleophile. Option D (position 154, 'Nucleophile') aligns with the Ser residue embedded in the conserved GGSMGG motif characteristic of the GNAT fold, where a serine can serve as a nucleophile attacking the acetyl-CoA thioester. A model familiar with GNAT acetyltransferase architecture can recognize the P-loop and assign the nucleophilic role to the serine within it.",
    "missing_item_specific_fact": "Precise discrimination among the three annotated active sites (154, 438, 467) as THE nucleophile requires knowledge of the GNAT P-loop geometry and which specific residue in the motif acts as nucleophile versus substrate-binding or CoA-binding residues. However, only position 154 appears among the answer choices, so this granularity is not strictly needed to select D.",
    "reason": "General biological reasoning eliminates B (out-of-range position) and A (wrong enzyme class). Recognition of the GGSMGG GNAT P-loop and the chemical logic of serine as nucleophile in acyltransferase catalysis provides a defensible argument for D over C. The '(1)' notation in C is uninformative. While deeper mechanistic knowledge of GNAT active-site topology would strengthen confidence, the available sequence features and chemical reasoning are sufficient to distinguish D from the other options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is impossible (position exceeds sequence length). Option A names a wrong enzyme class. Option C's '(1)' descriptor is non-informative and the residue (Glu215) is not a canonical nucleophile. Only D provides a chemically coherent nucleophile assignment at a recognizable motif position. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation at position 154 is based on computational evidence (similarity to O60062 and PIRSR pattern match, ECO:0000250/255), not direct experimental mutagenesis of this specific protein. The PubMed reference (17353245) experimentally characterizes the enzyme's catalytic function but the residue-level nucleophile assignment is transferred.",
    "The UniProt entry also annotates active sites at positions 438 and 467 without the 'Nucleophile' label; a model aware of these additional sites might question whether 154 is the sole or primary nucleophile, though only 154 appears in the answer choices.",
    "The sequence was first released in UniProt on 2025-02-05; the author's data-construction date and exact source snapshot are unknown, though the historical entry version 54 (released 2026-01-28) already contains the position-154 annotation.",
    "Option C's '(1)' notation is ambiguous and may be a formatting artifact; it does not clearly describe a catalytic role."
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

**Accession:** `J9VIY8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 54. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17353245","source":"PubMed"}],"value":"2.3.1.31"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Homoserine O-acetyltransferase"}}}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000250","id":"O60062","source":"UniProtKB"},{"evidenceCode":"ECO:0000255","id":"PIRSR000443-1","source":"PIRSR"}],"location":{"end":{"modifier":"EXACT","value":154},"start":{"modifier":"EXACT","value":154}},"type":"Active site"}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VIY8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:54.980036+00:00.  

```json
{"citation":{"authors":["Nazi I.","Scott A.","Sham A.","Rossi L.","Williamson P.R.","Kronstad J.W.","Wright G.D."],"citationCrossReferences":[{"database":"PubMed","id":"17353245"},{"database":"DOI","id":"10.1128/aac.01400-06"}],"citationType":"journal article","firstPage":"1731","id":"17353245","journal":"Antimicrob. Agents Chemother.","lastPage":"1736","publicationDate":"2007","title":"Role of homoserine transacetylase as a new target for antifungal agents.","volume":"51"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1dd26bd473689f347eca69268d64365a8d99894cc29c382df0bdcbe9218d5cda`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 35-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PATHWAY, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=17353245; DOI=10.1128/aac.01400-06;
RA   Nazi I., Scott A., Sham A., Rossi L., Williamson P.R., Kronstad J.W.,
RA   Wright G.D.;
RT   "Role of homoserine transacetylase as a new target for antifungal agents.";
RL   Antimicrob. Agents Chemother. 51:1731-1736(2007).
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VIY8?format=txt&versions=54)  
**Locator:** `lines 118-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 54 / 1.  
**Retrieved:** 2026-11-02T04:28:57.924962+00:00.  

```text
FT   ACT_SITE        154
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000250|UniProtKB:O60062,
FT                   ECO:0000255|PIRSR:PIRSR000443-1"
```

Source SHA-256: `f199a40bd4613a52dfaa0c84625c1bb8a81d2d65e01501415825a1c3b01fb844`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
