# transmembrane_0089

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 17..40

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFSVQRPPLTRTVVRMGLATLLPKTACLAGLNVALVFLLFQVQDGTGITLGPSKLDSKPTSLDSQQHVADKRWLATVGHYKHLAGATESTRDVSLLEERAQHRVNAQETNQRRTIFQRLLNLLRRRERDGEVSGSAADSSSRPRLSVRQRLAQLWRRAKSLFKRGIRRYFPQGRNRQRSLRAQRRRSELVFEKADSGCVIGKRILAHMQEQIGQPQALENSERLDRILTVAAWPPDVPKRFVSVTTGETRTLVRGAPLGSGGFATVYEATDVETNEELAVKVFMSEKEPTDETMLDLQRESSCYRNFSLAKTAKDAQESCRFMVPSDVVMLEGQPASTEVVIGLTTRWVPNYFLLMMRAEADMSKVISWVFGDASVNKSEFGLVVRMYLSSQAIKLVANVQAQGIVHTDIKPANFLLLKDGRLFLGDFGTYRINNSVGRAIGTPGYEPPERPFQATGITYTFPTDAWQLGITLYCIWCKERPTPADGIWDYLHFADCPSTPELVQDLIRSLLNRDPQKRMLPLQALETAAFKEMDSVVKGAAQNFEQQEHLHTE

[Multiple Choices]
A. 48..68; 83..103; 121..141; 145..165; 171..191; 203..223; 236..256; 269..289; 298..318; 336..356; 374..394; 403..423; 438..460; 516..536
B. 17..40; 165..184
C. 17..40
D. 12..39
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

> The exact sequence is matched to a UniProt entry annotating residues 17–40 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental measurement.

Citations as saved: [C5](#evidence-c5), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a localized, largely hydrophobic N-terminal stretch around residues 17–40, unlike the downstream sequence. Compared with D, C avoids extending the segment into the upstream region containing Arg15 and includes the hydrophobic Phe40 at its end.


**Missing item-specific fact**

> No protein-specific external fact is necessary to favor C from these options; the exact boundaries remain a sequence-based prediction rather than an experimentally established measurement in the supplied input.


**Reason**

> The sequence provides meaningful evidence for an N-terminal membrane-spanning helix and allows a biologically defensible preference among the candidates, though boundary precision is inherently uncertain.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D overlaps substantially with C, but includes an upstream charged residue and omits a hydrophobic terminal residue, making C the more defensible boundary choice.


### Important caveats

- The supporting database feature is computationally annotated, not experimentally demonstrated by the supplied evidence.
- Exact transmembrane boundaries can be uncertain from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a localized, largely hydrophobic N-terminal stretch around residues 17–40, unlike the downstream sequence. Compared with D, C avoids extending the segment into the upstream region containing Arg15 and includes the hydrophobic Phe40 at its end.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to favor C from these options; the exact boundaries remain a sequence-based prediction rather than an experimentally established measurement in the supplied input.",
    "reason": "The sequence provides meaningful evidence for an N-terminal membrane-spanning helix and allows a biologically defensible preference among the candidates, though boundary precision is inherently uncertain."
  },
  "case_id": "transmembrane_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotating residues 17–40 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental measurement."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated, not experimentally demonstrated by the supplied evidence.",
    "Exact transmembrane boundaries can be uncertain from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D overlaps substantially with C, but includes an upstream charged residue and omits a hydrophobic terminal residue, making C the more defensible boundary choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is matched to a UniProt entry annotating residues 17–40 as a helical transmembrane region. The annotation is computational (ECO:0000255), not evidence of experimental measurement.",
    "evidence_ids": ["C5", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a localized, largely hydrophobic N-terminal stretch around residues 17–40, unlike the downstream sequence. Compared with D, C avoids extending the segment into the upstream region containing Arg15 and includes the hydrophobic Phe40 at its end.",
    "missing_item_specific_fact": "No protein-specific external fact is necessary to favor C from these options; the exact boundaries remain a sequence-based prediction rather than an experimentally established measurement in the supplied input.",
    "reason": "The sequence provides meaningful evidence for an N-terminal membrane-spanning helix and allows a biologically defensible preference among the candidates, though boundary precision is inherently uncertain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D overlaps substantially with C, but includes an upstream charged residue and omits a hydrophobic terminal residue, making C the more defensible boundary choice."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated, not experimentally demonstrated by the supplied evidence.",
    "Exact transmembrane boundaries can be uncertain from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2PAY2 (ROP18_TOXGO) explicitly annotates a single transmembrane helix at positions 17..40 (evidence C5, H7: 'FT TRANSMEM 17..40 /note="Helical"'). The sequence at positions 17-40 (GLATLLPKTACLAGLNVALVFLLF) is predominantly hydrophobic, consistent with a TM helix. The annotation evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental determination, but it is the authoritative reference annotation. No other TM region is annotated in this entry.

Citations as saved: [C5](#evidence-c5), [H7](#evidence-h7), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple biological arguments distinguish C from the other options: (1) Option A lists 14 TM regions for a 554-aa protein identified as a serine/threonine kinase (the kinase domain fold is evident from the conserved catalytic motifs in the C-terminal ~350 residues). A multi-pass membrane protein with 14 TMs is incompatible with a secreted effector kinase, eliminating A. (2) Option B adds a second region at 165..184, which contains residues G-I-R-R-Y-F-P-Q-G-R-N-R-Q-R-S-L-R-A-Q-R — highly charged and polar, energetically incompatible with a lipid bilayer-spanning helix, eliminating B. (3) Between C (17..40) and D (12..39), position 15 is Arg (R), a positively charged residue. Placing a buried charged side chain within the hydrophobic core of a TM helix carries a large energetic penalty (~5-10 kcal/mol), making D (which includes R15) biophysically implausible relative to C, which begins at G17 after the charged residues. The N-terminal region before position 17 (MFSVQRPPLTRTVVRM) contains multiple charged/polar residues (Q, R, R, R) inconsistent with a TM segment.


**Missing item-specific fact**

> The exact boundary at position 17 vs 12 relies on the precise hydrophobicity profile and the energetic penalty of the Arg at position 15. While the charged-residue argument is a valid biophysical constraint, the exact boundary (17 vs 12) could vary by a few residues depending on the prediction algorithm used. The UniProt annotation (ECO:0000255, inferred by similarity) provides the definitive boundary, but a model applying general hydrophobicity rules might place the start at 16 or 18.


**Reason**

> The question provides sufficient sequence information for a knowledgeable model to eliminate A (absurd number of TMs for a kinase), eliminate B (charged second region), and prefer C over D (charged Arg at position 15 incompatible with TM helix interior). The reasoning relies on general biophysical principles (charged residues in TM helices are disfavored; secreted kinases have at most one TM helix) rather than memorizing this specific protein's annotation. The exact boundary precision (17 vs 12) is the weakest point but the R15 argument provides a concrete, generalizable reason.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option D (12..39) is the closest competitor to C, but the inclusion of Arg15 within the proposed TM helix provides a clear biophysical argument against D. Options A and B are eliminated by straightforward biological and sequence-composition arguments. No other option is genuinely defensible.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not an experimentally verified topology. No experimental data (e.g., cryo-EM of the full-length protein, membrane insertion assays) is cited for the TM region.
- The PDB structure (4JRN, evidence C10) covers only residues 187-554 (the kinase domain), so it provides no experimental information about the N-terminal TM region.
- The exact TM boundaries (17..40) may differ by ±2-3 residues depending on the prediction method; the annotation represents one computational estimate.
- The protein is from Toxoplasma gondii (a protozoan parasite), and ROP18 is a rhoptry effector kinase injected into host cells. Its TM helix likely anchors it to the rhoptry membrane rather than the plasma membrane, but this biological context does not affect the TM prediction itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple biological arguments distinguish C from the other options: (1) Option A lists 14 TM regions for a 554-aa protein identified as a serine/threonine kinase (the kinase domain fold is evident from the conserved catalytic motifs in the C-terminal ~350 residues). A multi-pass membrane protein with 14 TMs is incompatible with a secreted effector kinase, eliminating A. (2) Option B adds a second region at 165..184, which contains residues G-I-R-R-Y-F-P-Q-G-R-N-R-Q-R-S-L-R-A-Q-R — highly charged and polar, energetically incompatible with a lipid bilayer-spanning helix, eliminating B. (3) Between C (17..40) and D (12..39), position 15 is Arg (R), a positively charged residue. Placing a buried charged side chain within the hydrophobic core of a TM helix carries a large energetic penalty (~5-10 kcal/mol), making D (which includes R15) biophysically implausible relative to C, which begins at G17 after the charged residues. The N-terminal region before position 17 (MFSVQRPPLTRTVVRM) contains multiple charged/polar residues (Q, R, R, R) inconsistent with a TM segment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary at position 17 vs 12 relies on the precise hydrophobicity profile and the energetic penalty of the Arg at position 15. While the charged-residue argument is a valid biophysical constraint, the exact boundary (17 vs 12) could vary by a few residues depending on the prediction algorithm used. The UniProt annotation (ECO:0000255, inferred by similarity) provides the definitive boundary, but a model applying general hydrophobicity rules might place the start at 16 or 18.",
    "reason": "The question provides sufficient sequence information for a knowledgeable model to eliminate A (absurd number of TMs for a kinase), eliminate B (charged second region), and prefer C over D (charged Arg at position 15 incompatible with TM helix interior). The reasoning relies on general biophysical principles (charged residues in TM helices are disfavored; secreted kinases have at most one TM helix) rather than memorizing this specific protein's annotation. The exact boundary precision (17 vs 12) is the weakest point but the R15 argument provides a concrete, generalizable reason."
  },
  "case_id": "transmembrane_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H7",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY2 (ROP18_TOXGO) explicitly annotates a single transmembrane helix at positions 17..40 (evidence C5, H7: 'FT TRANSMEM 17..40 /note=\"Helical\"'). The sequence at positions 17-40 (GLATLLPKTACLAGLNVALVFLLF) is predominantly hydrophobic, consistent with a TM helix. The annotation evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental determination, but it is the authoritative reference annotation. No other TM region is annotated in this entry."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not an experimentally verified topology. No experimental data (e.g., cryo-EM of the full-length protein, membrane insertion assays) is cited for the TM region.",
    "The PDB structure (4JRN, evidence C10) covers only residues 187-554 (the kinase domain), so it provides no experimental information about the N-terminal TM region.",
    "The exact TM boundaries (17..40) may differ by ±2-3 residues depending on the prediction method; the annotation represents one computational estimate.",
    "The protein is from Toxoplasma gondii (a protozoan parasite), and ROP18 is a rhoptry effector kinase injected into host cells. Its TM helix likely anchors it to the rhoptry membrane rather than the plasma membrane, but this biological context does not affect the TM prediction itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (12..39) is the closest competitor to C, but the inclusion of Arg15 within the proposed TM helix provides a clear biophysical argument against D. Options A and B are eliminated by straightforward biological and sequence-composition arguments. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2PAY2 (ROP18_TOXGO) explicitly annotates a single transmembrane helix at positions 17..40 (evidence C5, H7: 'FT TRANSMEM 17..40 /note=\"Helical\"'). The sequence at positions 17-40 (GLATLLPKTACLAGLNVALVFLLF) is predominantly hydrophobic, consistent with a TM helix. The annotation evidence code is ECO:0000255 (inferred by similarity), so this is a computational annotation rather than experimental determination, but it is the authoritative reference annotation. No other TM region is annotated in this entry.",
    "evidence_ids": ["C5", "H7", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple biological arguments distinguish C from the other options: (1) Option A lists 14 TM regions for a 554-aa protein identified as a serine/threonine kinase (the kinase domain fold is evident from the conserved catalytic motifs in the C-terminal ~350 residues). A multi-pass membrane protein with 14 TMs is incompatible with a secreted effector kinase, eliminating A. (2) Option B adds a second region at 165..184, which contains residues G-I-R-R-Y-F-P-Q-G-R-N-R-Q-R-S-L-R-A-Q-R — highly charged and polar, energetically incompatible with a lipid bilayer-spanning helix, eliminating B. (3) Between C (17..40) and D (12..39), position 15 is Arg (R), a positively charged residue. Placing a buried charged side chain within the hydrophobic core of a TM helix carries a large energetic penalty (~5-10 kcal/mol), making D (which includes R15) biophysically implausible relative to C, which begins at G17 after the charged residues. The N-terminal region before position 17 (MFSVQRPPLTRTVVRM) contains multiple charged/polar residues (Q, R, R, R) inconsistent with a TM segment.",
    "missing_item_specific_fact": "The exact boundary at position 17 vs 12 relies on the precise hydrophobicity profile and the energetic penalty of the Arg at position 15. While the charged-residue argument is a valid biophysical constraint, the exact boundary (17 vs 12) could vary by a few residues depending on the prediction algorithm used. The UniProt annotation (ECO:0000255, inferred by similarity) provides the definitive boundary, but a model applying general hydrophobicity rules might place the start at 16 or 18.",
    "reason": "The question provides sufficient sequence information for a knowledgeable model to eliminate A (absurd number of TMs for a kinase), eliminate B (charged second region), and prefer C over D (charged Arg at position 15 incompatible with TM helix interior). The reasoning relies on general biophysical principles (charged residues in TM helices are disfavored; secreted kinases have at most one TM helix) rather than memorizing this specific protein's annotation. The exact boundary precision (17 vs 12) is the weakest point but the R15 argument provides a concrete, generalizable reason."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option D (12..39) is the closest competitor to C, but the inclusion of Arg15 within the proposed TM helix provides a clear biophysical argument against D. Options A and B are eliminated by straightforward biological and sequence-composition arguments. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not an experimentally verified topology. No experimental data (e.g., cryo-EM of the full-length protein, membrane insertion assays) is cited for the TM region.",
    "The PDB structure (4JRN, evidence C10) covers only residues 187-554 (the kinase domain), so it provides no experimental information about the N-terminal TM region.",
    "The exact TM boundaries (17..40) may differ by ±2-3 residues depending on the prediction method; the annotation represents one computational estimate.",
    "The protein is from Toxoplasma gondii (a protozoan parasite), and ROP18 is a rhoptry effector kinase injected into host cells. Its TM helix likely anchors it to the rhoptry membrane rather than the plasma membrane, but this biological context does not affect the TM prediction itself."
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

**Accession:** `Q2PAY2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 128. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
"Q2PAY2"
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"AFO54811.1","source":"EMBL"}],"value":"Rhoptry kinase family protein"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAJ27113.1","source":"EMBL"}],"value":"Rhoptry protein 18"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"KAF4642700.1","source":"EMBL"}],"value":"Rhoptry protein ROP18"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"21147463","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"21203588","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24129568","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"23144612","source":"PubMed"}],"value":"2.7.11.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"19266027","source":"PubMed"}],"value":"Serine/threonine-protein kinase ROP18"}}}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":40},"start":{"modifier":"EXACT","value":17}},"type":"Transmembrane"}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2PAY2.json)  
**Locator:** `/references/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:20.547223+00:00.  

```json
{"citation":{"authors":["Lim D.","Gold D.A.","Julien L.","Rosowski E.E.","Niedelman W.","Yaffe M.B.","Saeij J.P."],"citationCrossReferences":[{"database":"PubMed","id":"24129568"},{"database":"DOI","id":"10.1074/jbc.m113.523266"}],"citationType":"journal article","firstPage":"34968","id":"24129568","journal":"J. Biol. Chem.","lastPage":"34980","publicationDate":"2013","title":"Structure of the Toxoplasma gondii ROP18 kinase domain reveals a second ligand binding pocket required for acute virulence.","volume":"288"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4JRN","source":"PDB"}],"referenceNumber":14,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.71 ANGSTROMS) OF 187-554 IN COMPLEX WITH ATP ANALOG AND MAGNESIUM ION","FUNCTION","CATALYTIC ACTIVITY","DOMAIN","DISULFIDE BOND","MUTAGENESIS OF ASP-409"]}
```

Source SHA-256: `8df2f8adea3f30336796f12604d9132ac56ded3e05e2b6771494b9233e648d8c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2PAY2?format=txt&versions=128)  
**Locator:** `lines 294-296`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 128 / 1.  
**Retrieved:** 2026-11-01T06:28:30.449896+00:00.  

```text
FT   TRANSMEM        17..40
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `d742a9e016b6f30b83223ee19894f6ef23ef15a029631c50b8b5eb70a7cb2700`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
