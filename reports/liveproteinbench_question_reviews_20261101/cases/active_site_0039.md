# active_site_0039

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 154 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNITILSKETIKPLAPTPHHHKYYKVSLLDQFAPSSYMPFIFFYPNKFADRDAAGILTQLKESLSQILTIYYPLAGRVKDTVYVECNDEGVEFIEAQANGSLSDFLKQPDIAALNNFLPRNGNGLEKGCSISPVAIKATVFECSGIVLGVCIFHKVVDAAAAGEFLQSWAKIGRGSKETVELPNFTSASSLFPPRESLSSKFVRDFDNFFFQGSKSFMRRFVFDATAITTLRTKATSEKVPNPSRVEALMEFVVQHLSTAFKTAKSETPETLMITHPVNLRKRIEPPLPDSTFGNVIWLAFAFYDCDPSETKIKPGDVVERVREAFAALDKESISELETDDAFTSLSELLESVYTNEKIKIYRFTSTCNMGFYDVDFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN

[Multiple Choices]
A. Position 251 (Proton acceptor)
B. Position 213 (Proton acceptor)
C. Position 292 (Proton acceptor)
D. Position 154 (Proton acceptor)
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

> The exact sequence matches the UniProt entry, which annotates position 154 as a proton acceptor in both the current and archived records. The site annotation carries ECO:0000255, so this supports the key as a computational sequence-based annotation, not as direct experimental validation of that residue.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains H154-K155-V156-V157-D158, an HXXXD motif, and a downstream DFGWG motif characteristic of BAHD acyltransferases. In this enzyme family, the conserved histidine is a plausible general base/proton acceptor, distinguishing position 154 from the other listed positions.


**Missing item-specific fact**

> No item-specific database fact is necessary for a defensible motif-based inference; direct experimental confirmation of H154's role is not supplied.


**Reason**

> The sequence motifs and enzyme-family biology provide a concrete basis for selecting the conserved histidine at 154. This is an inference rather than proof of the site-specific mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 154 among the listed choices matches the conserved HXXXD catalytic motif. Reviewer-only annotation also identifies position 376 as a proton acceptor, but that position is not offered.


### Important caveats

- The site-specific UniProt annotation is computationally evidenced, not shown here to be experimentally established.
- The enzyme-level function has a literature-linked annotation, but that does not by itself constitute experimental validation of the active-site residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains H154-K155-V156-V157-D158, an HXXXD motif, and a downstream DFGWG motif characteristic of BAHD acyltransferases. In this enzyme family, the conserved histidine is a plausible general base/proton acceptor, distinguishing position 154 from the other listed positions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific database fact is necessary for a defensible motif-based inference; direct experimental confirmation of H154's role is not supplied.",
    "reason": "The sequence motifs and enzyme-family biology provide a concrete basis for selecting the conserved histidine at 154. This is an inference rather than proof of the site-specific mechanism."
  },
  "case_id": "active_site_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates position 154 as a proton acceptor in both the current and archived records. The site annotation carries ECO:0000255, so this supports the key as a computational sequence-based annotation, not as direct experimental validation of that residue."
  },
  "important_caveats": [
    "The site-specific UniProt annotation is computationally evidenced, not shown here to be experimentally established.",
    "The enzyme-level function has a literature-linked annotation, but that does not by itself constitute experimental validation of the active-site residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 among the listed choices matches the conserved HXXXD catalytic motif. Reviewer-only annotation also identifies position 376 as a proton acceptor, but that position is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates position 154 as a proton acceptor in both the current and archived records. The site annotation carries ECO:0000255, so this supports the key as a computational sequence-based annotation, not as direct experimental validation of that residue.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains H154-K155-V156-V157-D158, an HXXXD motif, and a downstream DFGWG motif characteristic of BAHD acyltransferases. In this enzyme family, the conserved histidine is a plausible general base/proton acceptor, distinguishing position 154 from the other listed positions.",
    "missing_item_specific_fact": "No item-specific database fact is necessary for a defensible motif-based inference; direct experimental confirmation of H154's role is not supplied.",
    "reason": "The sequence motifs and enzyme-family biology provide a concrete basis for selecting the conserved histidine at 154. This is an inference rather than proof of the site-specific mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 154 among the listed choices matches the conserved HXXXD catalytic motif. Reviewer-only annotation also identifies position 376 as a proton acceptor, but that position is not offered."
  },
  "important_caveats": [
    "The site-specific UniProt annotation is computationally evidenced, not shown here to be experimentally established.",
    "The enzyme-level function has a literature-linked annotation, but that does not by itself constitute experimental validation of the active-site residue."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A9E7LUL3 (Akuammiline synthase 2, EC 2.3.1.322, Alstonia scholaris) annotates position 154 as an active site 'Proton acceptor' (evidence code ECO:0000255, inferred by similarity). The historical flat-file (H3) confirms: ACT_SITE 154 /note='Proton acceptor'. The sequence matches (SHA256 confirmed). Note: position 376 is also annotated as a proton acceptor (C6/H4), but it is not among the answer choices. The annotation is computational (similarity-based), not direct experimental evidence for this specific residue, though the enzyme's overall catalytic function is experimentally supported by PubMed 36349266.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4), [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Among the four options, position 154 is Histidine (verified by counting: ...F153-H154-K155-V156-V157-D158-A159...), which is the classic proton acceptor in enzyme catalysis due to its imidazole side chain (pKa ~6). The surrounding motif H-K-V-V-D-A is a recognized variant of the BAHD acyltransferase catalytic HxxDG motif (here HxxD). The other options are Glycine (213, no ionizable side chain), Phenylalanine (292, no ionizable side chain), and Glutamate (251, typically a proton donor/acid rather than the catalytic base in acyltransferases). General biochemistry identifies His as the proton acceptor; the HxxD context further supports position 154 over other His residues in the sequence.


**Missing item-specific fact**

> Identifying the correct His among multiple His residues in the 450-aa sequence (positions 19-21, 154, 255, 275, 386, 405) requires recognizing the BAHD acyltransferase family and its HxxDG/HxxD motif context, which is not explicitly provided in the question input.


**Reason**

> The question provides sufficient grounds for biological reasoning: (1) His is the canonical proton acceptor in enzyme active sites, eliminating Gly, Phe, and (in this context) Glu; (2) the HxxD motif visible around position 154 is consistent with BAHD acyltransferase catalysis. However, distinguishing the correct His from other His residues does require family-level knowledge (BAHD motif recognition) that is not stated in the prompt. The distractors are sufficiently implausible (Gly and Phe cannot be proton acceptors) to make the answer identifiable by general biochemistry, though pinpointing the exact position among His residues adds difficulty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Position 154 (His) is the only option that is a chemically plausible proton acceptor in enzyme catalysis. Glycine (213) and Phenylalanine (292) lack ionizable side chains entirely. Glutamate (251) can accept a proton but is not the catalytic base in acyltransferases and does not fit the HxxDG motif context. No other option is defensible as 'the proton acceptor' for this enzyme class.


### Important caveats

- The active site annotation at position 154 carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/transfer annotation rather than direct experimental mutagenesis or structural evidence for this specific residue.
- Position 376 is also annotated as a proton acceptor (Proton acceptor, ECO:0000255), but it is not among the answer choices, so it does not create ambiguity for this question.
- The BAHD motif at position 154 is HxxD (H-K-V-V-D-A) rather than the canonical HxxDG, which makes motif-based identification somewhat less straightforward.
- The protein's overall function (akuammiline synthase, EC 2.3.1.322) is experimentally confirmed (PubMed 36349266), but the specific residue-level proton-acceptor assignment relies on similarity-based inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Among the four options, position 154 is Histidine (verified by counting: ...F153-H154-K155-V156-V157-D158-A159...), which is the classic proton acceptor in enzyme catalysis due to its imidazole side chain (pKa ~6). The surrounding motif H-K-V-V-D-A is a recognized variant of the BAHD acyltransferase catalytic HxxDG motif (here HxxD). The other options are Glycine (213, no ionizable side chain), Phenylalanine (292, no ionizable side chain), and Glutamate (251, typically a proton donor/acid rather than the catalytic base in acyltransferases). General biochemistry identifies His as the proton acceptor; the HxxD context further supports position 154 over other His residues in the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying the correct His among multiple His residues in the 450-aa sequence (positions 19-21, 154, 255, 275, 386, 405) requires recognizing the BAHD acyltransferase family and its HxxDG/HxxD motif context, which is not explicitly provided in the question input.",
    "reason": "The question provides sufficient grounds for biological reasoning: (1) His is the canonical proton acceptor in enzyme active sites, eliminating Gly, Phe, and (in this context) Glu; (2) the HxxD motif visible around position 154 is consistent with BAHD acyltransferase catalysis. However, distinguishing the correct His from other His residues does require family-level knowledge (BAHD motif recognition) that is not stated in the prompt. The distractors are sufficiently implausible (Gly and Phe cannot be proton acceptors) to make the answer identifiable by general biochemistry, though pinpointing the exact position among His residues adds difficulty."
  },
  "case_id": "active_site_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4",
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUL3 (Akuammiline synthase 2, EC 2.3.1.322, Alstonia scholaris) annotates position 154 as an active site 'Proton acceptor' (evidence code ECO:0000255, inferred by similarity). The historical flat-file (H3) confirms: ACT_SITE 154 /note='Proton acceptor'. The sequence matches (SHA256 confirmed). Note: position 376 is also annotated as a proton acceptor (C6/H4), but it is not among the answer choices. The annotation is computational (similarity-based), not direct experimental evidence for this specific residue, though the enzyme's overall catalytic function is experimentally supported by PubMed 36349266."
  },
  "important_caveats": [
    "The active site annotation at position 154 carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/transfer annotation rather than direct experimental mutagenesis or structural evidence for this specific residue.",
    "Position 376 is also annotated as a proton acceptor (Proton acceptor, ECO:0000255), but it is not among the answer choices, so it does not create ambiguity for this question.",
    "The BAHD motif at position 154 is HxxD (H-K-V-V-D-A) rather than the canonical HxxDG, which makes motif-based identification somewhat less straightforward.",
    "The protein's overall function (akuammiline synthase, EC 2.3.1.322) is experimentally confirmed (PubMed 36349266), but the specific residue-level proton-acceptor assignment relies on similarity-based inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Position 154 (His) is the only option that is a chemically plausible proton acceptor in enzyme catalysis. Glycine (213) and Phenylalanine (292) lack ionizable side chains entirely. Glutamate (251) can accept a proton but is not the catalytic base in acyltransferases and does not fit the HxxDG motif context. No other option is defensible as 'the proton acceptor' for this enzyme class."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A9E7LUL3 (Akuammiline synthase 2, EC 2.3.1.322, Alstonia scholaris) annotates position 154 as an active site 'Proton acceptor' (evidence code ECO:0000255, inferred by similarity). The historical flat-file (H3) confirms: ACT_SITE 154 /note='Proton acceptor'. The sequence matches (SHA256 confirmed). Note: position 376 is also annotated as a proton acceptor (C6/H4), but it is not among the answer choices. The annotation is computational (similarity-based), not direct experimental evidence for this specific residue, though the enzyme's overall catalytic function is experimentally supported by PubMed 36349266.",
    "evidence_ids": ["C5", "H3", "C6", "H4", "C4", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Among the four options, position 154 is Histidine (verified by counting: ...F153-H154-K155-V156-V157-D158-A159...), which is the classic proton acceptor in enzyme catalysis due to its imidazole side chain (pKa ~6). The surrounding motif H-K-V-V-D-A is a recognized variant of the BAHD acyltransferase catalytic HxxDG motif (here HxxD). The other options are Glycine (213, no ionizable side chain), Phenylalanine (292, no ionizable side chain), and Glutamate (251, typically a proton donor/acid rather than the catalytic base in acyltransferases). General biochemistry identifies His as the proton acceptor; the HxxD context further supports position 154 over other His residues in the sequence.",
    "missing_item_specific_fact": "Identifying the correct His among multiple His residues in the 450-aa sequence (positions 19-21, 154, 255, 275, 386, 405) requires recognizing the BAHD acyltransferase family and its HxxDG/HxxD motif context, which is not explicitly provided in the question input.",
    "reason": "The question provides sufficient grounds for biological reasoning: (1) His is the canonical proton acceptor in enzyme active sites, eliminating Gly, Phe, and (in this context) Glu; (2) the HxxD motif visible around position 154 is consistent with BAHD acyltransferase catalysis. However, distinguishing the correct His from other His residues does require family-level knowledge (BAHD motif recognition) that is not stated in the prompt. The distractors are sufficiently implausible (Gly and Phe cannot be proton acceptors) to make the answer identifiable by general biochemistry, though pinpointing the exact position among His residues adds difficulty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Position 154 (His) is the only option that is a chemically plausible proton acceptor in enzyme catalysis. Glycine (213) and Phenylalanine (292) lack ionizable side chains entirely. Glutamate (251) can accept a proton but is not the catalytic base in acyltransferases and does not fit the HxxDG motif context. No other option is defensible as 'the proton acceptor' for this enzyme class."
  },
  "important_caveats": [
    "The active site annotation at position 154 carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational/transfer annotation rather than direct experimental mutagenesis or structural evidence for this specific residue.",
    "Position 376 is also annotated as a proton acceptor (Proton acceptor, ECO:0000255), but it is not among the answer choices, so it does not create ambiguity for this question.",
    "The BAHD motif at position 154 is HxxD (H-K-V-V-D-A) rather than the canonical HxxDG, which makes motif-based identification somewhat less straightforward.",
    "The protein's overall function (akuammiline synthase, EC 2.3.1.322) is experimentally confirmed (PubMed 36349266), but the specific residue-level proton-acceptor assignment relies on similarity-based inference."
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

**Accession:** `A0A9E7LUL3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 13. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36349266","source":"PubMed"}],"value":"2.3.1.322"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"Akuammiline synthase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36349266","source":"PubMed"}],"value":"AsAKS2"}]}}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":154},"start":{"modifier":"EXACT","value":154}},"type":"Active site"}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":376},"start":{"modifier":"EXACT","value":376}},"type":"Active site"}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:09.156747+00:00.  

```json
{"citation":{"authors":["Wang Z.","Xiao Y.","Wu S.","Chen J.","Li A.","Tatsis E.C."],"citationCrossReferences":[{"database":"PubMed","id":"36349266"},{"database":"DOI","id":"10.1039/d2sc03612f"}],"citationType":"journal article","firstPage":"12389","id":"36349266","journal":"Chem. Sci.","lastPage":"12395","publicationDate":"2022","title":"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.","volume":"13"},"evidences":[{"evidenceCode":"ECO:0000312","id":"URS65388.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 72-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
FT   ACT_SITE        154
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 13 / 1.  
**Retrieved:** 2026-11-02T04:26:14.133287+00:00.  

```text
FT   ACT_SITE        376
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
