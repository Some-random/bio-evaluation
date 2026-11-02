# active_site_0133

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 318 (O-(5&#x27;-phospho-DNA)-tyrosine intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNLCNVNNYYLIIAEKSKAAKKIAEALSEKPILCRKYNVSYWIIKDHNSSKYVIVPAAGHLFGLKGESGFPVYDADWKPLWEIDKNSYYTKRYYQLISSLSKYALGFINACDYDIEGSVIGYLIIKNLGDIKKAKRMKFSALTKSDILSAFRNISALDYDMINAGIARHKIDWLWGINVSRALMISLQDFAKKRVILSAGRVQSPTLVQVVNSEIERNLFIPLPKFTVSIIVKIKDYSLNIKVNKEFEKITEAKEFLNKLINKTVKVVEVENRVRLLERPSPFNLTDLQIEAGRIYGISPYNVERIAEDLYLDGLISYPRTNSQKIPSTISIYNIIKGLENSSYRKLVDLVRKITGGKYVVKQGIKDDPAHPAIHPTGEAPKNLPNSKFKIYDLIARRFLGSVSADAKLSNTIYTLKVSDFPLEFTVSYTKILERNWLDIYHFHNVKEDKPIFLSKGDEGKIVDGKVNISLSKPTSRYTKVSLLKWMESSNLGTEATRGRIIEILVKRKYLTNNGRYIIPTKLGFYIAEILNKFFPDIVDVRMTADMESKLEMIKTGKVLESKVIKENIEKLNKFIEEYKVNKDKVGESLAKALGLIKIVKCKYCDLEQYKDGLCKYHYEAKVRLLDAVEIWKERTKYDHKKILKRISSSKSTGKYVKDIVTYMLSSE

[Multiple Choices]
A. Position 1142 (Proton donor; for dehydratase activity 1)
B. Position 318 (O-(5'-phospho-DNA)-tyrosine intermediate)
C. Position 976 (Proton acceptor; for dehydratase activity 1)
D. Position 70 (Acyl-ester intermediate)
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

> The supplied sequence exactly matches the annotated 668-aa DNA topoisomerase III, and its active-site annotation identifies residue 318 as the O-(5'-phospho-DNA)-tyrosine intermediate. This supports choice B. The residue annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence for residue 318.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A tyrosine-DNA phosphodiester intermediate is characteristic of topoisomerase chemistry, making B biologically plausible over the dehydratase and acyl-ester distractors.


**Missing item-specific fact**

> The input does not identify this sequence as DNA topoisomerase III or establish that its residue 318 is the catalytic tyrosine; that protein-specific site assignment comes from annotation or equivalent external knowledge.


**Reason**

> The mechanism clue in B helps distinguish the type of chemistry, but assigning the specific sequence position as the active site requires information not established by the sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched-sequence annotation specifically assigns the DNA-tyrosine intermediate to residue 318; the other listed descriptions do not provide a competing assignment for this protein.


### Important caveats

- The active-site residue annotation is PROSITE-rule computational evidence; the cited publications support the protein's topoisomerase identity and activity, but the supplied evidence does not independently establish experimental validation of Tyr318.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A tyrosine-DNA phosphodiester intermediate is characteristic of topoisomerase chemistry, making B biologically plausible over the dehydratase and acyl-ester distractors.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not identify this sequence as DNA topoisomerase III or establish that its residue 318 is the catalytic tyrosine; that protein-specific site assignment comes from annotation or equivalent external knowledge.",
    "reason": "The mechanism clue in B helps distinguish the type of chemistry, but assigning the specific sequence position as the active site requires information not established by the sequence and choices alone."
  },
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 668-aa DNA topoisomerase III, and its active-site annotation identifies residue 318 as the O-(5'-phospho-DNA)-tyrosine intermediate. This supports choice B. The residue annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence for residue 318."
  },
  "important_caveats": [
    "The active-site residue annotation is PROSITE-rule computational evidence; the cited publications support the protein's topoisomerase identity and activity, but the supplied evidence does not independently establish experimental validation of Tyr318."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation specifically assigns the DNA-tyrosine intermediate to residue 318; the other listed descriptions do not provide a competing assignment for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 668-aa DNA topoisomerase III, and its active-site annotation identifies residue 318 as the O-(5'-phospho-DNA)-tyrosine intermediate. This supports choice B. The residue annotation is computationally assigned by PROSITE-ProRule, not direct experimental evidence for residue 318.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A tyrosine-DNA phosphodiester intermediate is characteristic of topoisomerase chemistry, making B biologically plausible over the dehydratase and acyl-ester distractors.",
    "missing_item_specific_fact": "The input does not identify this sequence as DNA topoisomerase III or establish that its residue 318 is the catalytic tyrosine; that protein-specific site assignment comes from annotation or equivalent external knowledge.",
    "reason": "The mechanism clue in B helps distinguish the type of chemistry, but assigning the specific sequence position as the active site requires information not established by the sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched-sequence annotation specifically assigns the DNA-tyrosine intermediate to residue 318; the other listed descriptions do not provide a competing assignment for this protein."
  },
  "important_caveats": [
    "The active-site residue annotation is PROSITE-rule computational evidence; the cited publications support the protein's topoisomerase identity and activity, but the supplied evidence does not independently establish experimental validation of Tyr318."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q97ZJ8 (DNA topoisomerase 3, Saccharolobus solfataricus, 668 AA, sequence SHA256 matched) annotates position 318 as 'O-(5'-phospho-DNA)-tyrosine intermediate' (Active site, ECO:0000255|PROSITE-ProRule:PRU01383). This is the canonical catalytic tyrosine of type IA topoisomerases, forming a covalent phosphotyrosyl intermediate with the 5'-phospho end of DNA. The annotation is pattern-based (PROSITE-ProRule) rather than direct experimental mutagenesis, but it is the standard, well-established assignment for the TOPRIM catalytic tyrosine in Topo III proteins. The other options are clearly wrong: positions 1142 and 976 exceed the 668-residue sequence, and 'Acyl-ester intermediate' at position 70 describes a serine hydrolase mechanism irrelevant to a topoisomerase.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Two independent reasoning steps distinguish the answer: (1) Positions 1142 (A) and 976 (C) exceed the 668-residue sequence length, eliminating them by arithmetic. (2) Between B and D, the C-terminal region of the sequence contains a Cys-rich zinc-binding motif ('CKYCDLEQYKDGLCKYHYEAK') characteristic of the OB-fold/zinc-binding domain of type IA topoisomerases (Topo III/IV), not of serine hydrolases. The 'O-(5'-phospho-DNA)-tyrosine intermediate' (B) is the defining catalytic mechanism of type IA topoisomerases, while 'Acyl-ester intermediate' (D) is the hallmark of serine hydrolases/proteases. The protein lacks canonical serine hydrolase motifs (e.g., GxSxG nucleophile elbow) and its domain architecture (N-terminal TOPRIM-like domain + C-terminal Zn-binding domain) is inconsistent with a hydrolase.


**Missing item-specific fact**

> None strictly required. Identifying the exact protein as SsTop3/Q97ZJ8 would require database lookup, but the family-level assignment (type IA topoisomerase vs. serine hydrolase) can be inferred from the zinc-binding Cys-rich motif, absence of hydrolase catalytic motifs, and the mechanistic terminology in the answer choices themselves.


**Reason**

> The length-based elimination of A and C is purely arithmetic. The B-vs-D distinction relies on recognizing the zinc-binding domain signature and the incompatibility of an acyl-ester mechanism with a DNA-processing enzyme, both of which are general biological reasoning rather than item-specific memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are impossible (positions beyond sequence length). Option D describes a mechanism (acyl-ester) mechanistically incompatible with a DNA topoisomerase. Only B is consistent with both the sequence length and the enzyme class identifiable from sequence features.


### Important caveats

- The active-site annotation at position 318 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a pattern-based computational/curatorial assignment rather than a direct experimental (e.g., mutagenesis or crystallographic covalent-trapping) determination. It is nonetheless the universally accepted assignment for the TOPRIM catalytic tyrosine in Topo III.
- The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must work from the raw sequence and the answer-choice descriptions alone.
- Positions 1142 and 976 being beyond the 668-residue sequence makes options A and C trivially eliminable, reducing the effective choice to B vs. D. This somewhat lowers the difficulty but does not invalidate the question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Two independent reasoning steps distinguish the answer: (1) Positions 1142 (A) and 976 (C) exceed the 668-residue sequence length, eliminating them by arithmetic. (2) Between B and D, the C-terminal region of the sequence contains a Cys-rich zinc-binding motif ('CKYCDLEQYKDGLCKYHYEAK') characteristic of the OB-fold/zinc-binding domain of type IA topoisomerases (Topo III/IV), not of serine hydrolases. The 'O-(5'-phospho-DNA)-tyrosine intermediate' (B) is the defining catalytic mechanism of type IA topoisomerases, while 'Acyl-ester intermediate' (D) is the hallmark of serine hydrolases/proteases. The protein lacks canonical serine hydrolase motifs (e.g., GxSxG nucleophile elbow) and its domain architecture (N-terminal TOPRIM-like domain + C-terminal Zn-binding domain) is inconsistent with a hydrolase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the exact protein as SsTop3/Q97ZJ8 would require database lookup, but the family-level assignment (type IA topoisomerase vs. serine hydrolase) can be inferred from the zinc-binding Cys-rich motif, absence of hydrolase catalytic motifs, and the mechanistic terminology in the answer choices themselves.",
    "reason": "The length-based elimination of A and C is purely arithmetic. The B-vs-D distinction relies on recognizing the zinc-binding domain signature and the incompatibility of an acyl-ester mechanism with a DNA-processing enzyme, both of which are general biological reasoning rather than item-specific memorization."
  },
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt Q97ZJ8 (DNA topoisomerase 3, Saccharolobus solfataricus, 668 AA, sequence SHA256 matched) annotates position 318 as 'O-(5'-phospho-DNA)-tyrosine intermediate' (Active site, ECO:0000255|PROSITE-ProRule:PRU01383). This is the canonical catalytic tyrosine of type IA topoisomerases, forming a covalent phosphotyrosyl intermediate with the 5'-phospho end of DNA. The annotation is pattern-based (PROSITE-ProRule) rather than direct experimental mutagenesis, but it is the standard, well-established assignment for the TOPRIM catalytic tyrosine in Topo III proteins. The other options are clearly wrong: positions 1142 and 976 exceed the 668-residue sequence, and 'Acyl-ester intermediate' at position 70 describes a serine hydrolase mechanism irrelevant to a topoisomerase."
  },
  "important_caveats": [
    "The active-site annotation at position 318 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a pattern-based computational/curatorial assignment rather than a direct experimental (e.g., mutagenesis or crystallographic covalent-trapping) determination. It is nonetheless the universally accepted assignment for the TOPRIM catalytic tyrosine in Topo III.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must work from the raw sequence and the answer-choice descriptions alone.",
    "Positions 1142 and 976 being beyond the 668-residue sequence makes options A and C trivially eliminable, reducing the effective choice to B vs. D. This somewhat lowers the difficulty but does not invalidate the question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are impossible (positions beyond sequence length). Option D describes a mechanism (acyl-ester) mechanistically incompatible with a DNA topoisomerase. Only B is consistent with both the sequence length and the enzyme class identifiable from sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0133",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q97ZJ8 (DNA topoisomerase 3, Saccharolobus solfataricus, 668 AA, sequence SHA256 matched) annotates position 318 as 'O-(5'-phospho-DNA)-tyrosine intermediate' (Active site, ECO:0000255|PROSITE-ProRule:PRU01383). This is the canonical catalytic tyrosine of type IA topoisomerases, forming a covalent phosphotyrosyl intermediate with the 5'-phospho end of DNA. The annotation is pattern-based (PROSITE-ProRule) rather than direct experimental mutagenesis, but it is the standard, well-established assignment for the TOPRIM catalytic tyrosine in Topo III proteins. The other options are clearly wrong: positions 1142 and 976 exceed the 668-residue sequence, and 'Acyl-ester intermediate' at position 70 describes a serine hydrolase mechanism irrelevant to a topoisomerase.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Two independent reasoning steps distinguish the answer: (1) Positions 1142 (A) and 976 (C) exceed the 668-residue sequence length, eliminating them by arithmetic. (2) Between B and D, the C-terminal region of the sequence contains a Cys-rich zinc-binding motif ('CKYCDLEQYKDGLCKYHYEAK') characteristic of the OB-fold/zinc-binding domain of type IA topoisomerases (Topo III/IV), not of serine hydrolases. The 'O-(5'-phospho-DNA)-tyrosine intermediate' (B) is the defining catalytic mechanism of type IA topoisomerases, while 'Acyl-ester intermediate' (D) is the hallmark of serine hydrolases/proteases. The protein lacks canonical serine hydrolase motifs (e.g., GxSxG nucleophile elbow) and its domain architecture (N-terminal TOPRIM-like domain + C-terminal Zn-binding domain) is inconsistent with a hydrolase.",
    "missing_item_specific_fact": "None strictly required. Identifying the exact protein as SsTop3/Q97ZJ8 would require database lookup, but the family-level assignment (type IA topoisomerase vs. serine hydrolase) can be inferred from the zinc-binding Cys-rich motif, absence of hydrolase catalytic motifs, and the mechanistic terminology in the answer choices themselves.",
    "reason": "The length-based elimination of A and C is purely arithmetic. The B-vs-D distinction relies on recognizing the zinc-binding domain signature and the incompatibility of an acyl-ester mechanism with a DNA-processing enzyme, both of which are general biological reasoning rather than item-specific memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are impossible (positions beyond sequence length). Option D describes a mechanism (acyl-ester) mechanistically incompatible with a DNA topoisomerase. Only B is consistent with both the sequence length and the enzyme class identifiable from sequence features."
  },
  "important_caveats": [
    "The active-site annotation at position 318 carries evidence code ECO:0000255 (PROSITE-ProRule), i.e., it is a pattern-based computational/curatorial assignment rather than a direct experimental (e.g., mutagenesis or crystallographic covalent-trapping) determination. It is nonetheless the universally accepted assignment for the TOPRIM catalytic tyrosine in Topo III.",
    "The reviewer-only evidence confirms the sequence match and annotation but was not available to the evaluated model; the model must work from the raw sequence and the answer-choice descriptions alone.",
    "Positions 1142 and 976 being beyond the 668-residue sequence makes options A and C trivially eliminable, reducing the effective choice to B vs. D. This somewhat lowers the difficulty but does not invalidate the question."
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

**Accession:** `Q97ZJ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 132. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
"Q97ZJ8"
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"DNA topoisomerase III"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22722926","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29253195","source":"PubMed"}],"value":"5.6.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"DNA topoisomerase 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22722926","source":"PubMed"}],"value":"SsTop3"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"29253195","source":"PubMed"}],"value":"SsTopA"}]}}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q97ZJ8.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:26.328266+00:00.  

```json
{"description":"O-(5'-phospho-DNA)-tyrosine intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01383","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":318},"start":{"modifier":"EXACT","value":318}},"type":"Active site"}
```

Source SHA-256: `4ec40a69735e225949e29a9f2298e3634559e703f08ec9c5d619bb337f1a11d5`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
ID   TOP3_SACS2              Reviewed;         668 AA.
AC   Q97ZJ8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2001, sequence version 1.
DT   28-JAN-2026, entry version 132.
DE   RecName: Full=DNA topoisomerase 3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTop3 {ECO:0000303|PubMed:22722926};
DE            Short=SsTopA {ECO:0000303|PubMed:29253195};
DE            EC=5.6.2.1 {ECO:0000269|PubMed:22722926, ECO:0000269|PubMed:29253195};
DE   AltName: Full=DNA topoisomerase III {ECO:0000303|PubMed:29253195};
GN   Name=topA {ECO:0000303|PubMed:22722926, ECO:0000312|EMBL:AAK41190.1};
GN   OrderedLocusNames=SSO0907 {ECO:0000312|EMBL:AAK41190.1};
OS   Saccharolobus solfataricus (strain ATCC 35092 / DSM 1617 / JCM 11322 / P2)
OS   (Sulfolobus solfataricus).
OC   Archaea; Thermoproteota; Thermoprotei; Sulfolobales; Sulfolobaceae;
OC   Saccharolobus.
OX   NCBI_TaxID=273057;
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q97ZJ8?format=txt&versions=132)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 132 / 1.  
**Retrieved:** 2026-11-01T06:28:45.340278+00:00.  

```text
FT   ACT_SITE        318
FT                   /note="O-(5'-phospho-DNA)-tyrosine intermediate"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01383"
```

Source SHA-256: `77a05af9d1305445b3e0d4b67305724443fad1a6fc01422e81a6d8f5dc26d379`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 133. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
