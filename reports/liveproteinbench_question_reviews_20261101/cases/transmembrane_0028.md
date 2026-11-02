# transmembrane_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 1404..1424

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGKTKIYSVGFTVHEAQTLVTEKGQPVDPLVVVRCCGREYRTEIKYAKSNVVSWDESHTWTDLCLTDEEWETAYITFEVQAANAFWRNTLLGLVSVQLRLIQLRKTHQIRKALPLQHPDDTDVHGSLRVTVFACAPGEAPPSPGEEEVLEEEDHNDYDDLRKAVIDTNQVVEREAGSRLYHVYVTAYRVEDLPRSSKGARDPFVTCEFAGCKLKSTQARGCCSHTFNECFRFPVVTPLPEDAILIKIWDWNFMKADELIAVGRISFSELRTRQMVPRWFNLYGFDDEEVAQATKVAGQGGRLVANCYLGRILLGARAERLTKEDDLMPAHTVAARPYETPPVIPLAVLADVYEVQGAPGEKVSVEIWCGPARARTKWVTGLETKAAQRAGVAPQAFNRAMEGALGVASYLRGDIPEGEDRFPFDNTEGRVEDLRLVVPEDTKQQWDIIISLYVRGTTKGFMGDTRIAFQRLKMSKIPGHVHNNPRAPIWVPLISTPPFESVKPAPAILMVIEKSKVEAFARSKRKHVTAVGYQLRAYVYAARNLLSPSGALPNPFVQVACAGTSRETEVFEQTSSPVFMDCLLLDITMMTDPVSRLPTVAPIVVTLFEQRSWGIQFLGRATCHYDRLRGRLKPGESPTVAEPRWIKLRGGKYANRHLGDVLLLLELIRKRDAEIIPAFPMRPVVNMCNLTFSCLGVRSLYMTQRAKRLDYVSIRKGQDKKTELRRIRGPLLRISVSSYASAGRGNNEAILRYERNLPEDPTTVNKLWTTVTKAANADIFKVVNMEIDVPVDPIYDPRLVVQVYDRKQKPKYFIGEYSMSLVPLIPWVLDQQSAIEAVSPVNDFTDTVDLKHLGGLLRGFHGNSKNRGTGQIGLEALSAADRETADAHKEKTLAQSRFATYDPDNKTFSDSWLLPSGLPKILVSSYAVPGFRCDVIYTNMFTLNVYIPAKFVLFAEGKRAADKKTKEQYARPSVDSTLEQFLDDVIFPSDSLKKSVMGDIDVTGFVKFFVNLTHHEEPNPHVDSSAAEWASSEDRMRRHLRGEDAYPKLLKIRVYVIRAISLYVGDDRILPNPYLLFNLGDKSDTLRAEAKPNTHNPEFFTVWEKDVMFPDDSQFELQVWSAHEGTSGGLDDIFIGSTCIDLEERWFSKEWQKSMSKNQVPMEYRPLKQMPSGSFKGTVEMWVELMDFQKAGEVPKFDLQSPAATEVEIRVIVWGARNLNFKALGKDFVDAMIRCNLDCTGYRGSQPIAQQTDVHYYSKTGAAIFNWRMVYSRVVMPVSTCVLQIAAYDNRNMGESPFIGEVNLELRRYLERVASTLNSIDVDAELKLINRSRESADVSSFGFVQVSLQFISQSEATSKPVGLGREPPNRDPRLTTPQEGRKWEDVLGSAGLRVDYRPLWYWVRVAAVVFLSIWIFVVAFLYPSLLG

[Multiple Choices]
A. 35..55
B. 1408..1428
C. 1404..1424
D. 1404..1424; 630..652
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

> The supplied sequence exactly matches a UniProt entry annotated with a helical transmembrane region at 1404..1424, supporting choice C. The annotation is computational (ECO:0000255), not experimental evidence.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal hydrophobic stretch is consistent with a membrane-spanning helix, so sequence reasoning can suggest the general location.


**Missing item-specific fact**

> The precise annotated boundaries 1404..1424 are needed to distinguish C from the overlapping, slightly shifted 1408..1428 in B; those exact coordinates are not supplied in the question.


**Reason**

> A hydrophobic C-terminal segment supports a broad prediction, but does not meaningfully establish the exact start and end residues among the close alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> Choice D includes the annotated 1404..1424 segment as well as 630..652. If an option need only identify a segment, D also contains the correct one; if it is meant to list all predicted transmembrane regions, the extra range makes D a different claim.


### Important caveats

- The reviewer-only sequence-matched database annotation supports the key but was not available to the evaluated model.
- The annotation establishes database support, not experimental confirmation of the membrane-spanning boundaries.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch is consistent with a membrane-spanning helix, so sequence reasoning can suggest the general location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The precise annotated boundaries 1404..1424 are needed to distinguish C from the overlapping, slightly shifted 1408..1428 in B; those exact coordinates are not supplied in the question.",
    "reason": "A hydrophobic C-terminal segment supports a broad prediction, but does not meaningfully establish the exact start and end residues among the close alternatives."
  },
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated with a helical transmembrane region at 1404..1424, supporting choice C. The annotation is computational (ECO:0000255), not experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched database annotation supports the key but was not available to the evaluated model.",
    "The annotation establishes database support, not experimental confirmation of the membrane-spanning boundaries."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "Choice D includes the annotated 1404..1424 segment as well as 630..652. If an option need only identify a segment, D also contains the correct one; if it is meant to list all predicted transmembrane regions, the extra range makes D a different claim."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a UniProt entry annotated with a helical transmembrane region at 1404..1424, supporting choice C. The annotation is computational (ECO:0000255), not experimental evidence.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal hydrophobic stretch is consistent with a membrane-spanning helix, so sequence reasoning can suggest the general location.",
    "missing_item_specific_fact": "The precise annotated boundaries 1404..1424 are needed to distinguish C from the overlapping, slightly shifted 1408..1428 in B; those exact coordinates are not supplied in the question.",
    "reason": "A hydrophobic C-terminal segment supports a broad prediction, but does not meaningfully establish the exact start and end residues among the close alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "Choice D includes the annotated 1404..1424 segment as well as 630..652. If an option need only identify a segment, D also contains the correct one; if it is meant to list all predicted transmembrane regions, the extra range makes D a different claim."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched database annotation supports the key but was not available to the evaluated model.",
    "The annotation establishes database support, not experimental confirmation of the membrane-spanning boundaries."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7J6K2G0 (Ferlin 2, Toxoplasma gondii, 1426 AA) annotates a single transmembrane helix at positions 1404-1424 (evidence C5, H4), matching choice C exactly. The evidence code ECO:0000255 indicates this is an automatic/computational prediction rather than experimental data, but the sequence at 1404-1424 (VAAVVFLSIWIFVVAFLYPSL) is indeed a hydrophobic stretch of ~21 residues consistent with a TM helix. No second TM region is annotated. The sequence matches the benchmark (SHA256 confirmed).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Ferlin-family proteins (e.g., C. elegans FER-1/FER-2, human dysferlin) are well-characterized single-pass membrane proteins anchored by a single C-terminal transmembrane helix. This general family biology eliminates option D (which posits a second TM at 630-652). Option A (35-55: CCGREYRTEIKYAKSNVVSWD) contains charged residues (R, E, K, D) and is not hydrophobic enough for a TM helix. Option B (1408-1428) extends beyond the 1426-residue protein length and is therefore impossible. The remaining C-terminal hydrophobic stretch (VAAVVFLSIWIFVVAFLYPSL) is the only TM-like region, and its boundaries (1404-1424) correspond to the longest contiguous hydrophobic segment near the C-terminus.


**Missing item-specific fact**

> The exact residue-level boundaries (1404 vs 1405/1406 as start; 1424 vs 1425 as end) are set by the automatic annotation algorithm and are somewhat fuzzy; however, among the four choices, only C survives the elimination of A (wrong location/hydrophobicity), B (out-of-range), and D (second TM contradicted by ferlin single-pass topology).


**Reason**

> The question is answerable through: (1) recognizing ferlins as single-pass membrane proteins to eliminate D; (2) noting the protein is 1426 AA to eliminate B (1428 out of range); (3) assessing hydrophobicity at 35-55 to eliminate A; (4) identifying the C-terminal hydrophobic stretch as the TM region. These are general biological and sequence-analysis arguments, not lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is eliminated by sequence length (1426 < 1428). Option A is eliminated by lack of hydrophobicity (charged/polar residues dominate). Option D is eliminated by ferlin single-pass topology. Only C remains as a defensible answer. The exact boundaries 1404-1424 are annotation-set but are the only option consistent with the C-terminal hydrophobic segment after eliminating the others.


### Important caveats

- The TM annotation uses ECO:0000255 (automatic assertion according to rules), meaning it is a computational prediction, not experimental evidence. The true boundaries could shift by 1-2 residues.
- The reviewer-only evidence confirms sequence match (SHA256) and that the UniProt entry was first public 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed when the question was authored.
- The ferlin single-pass topology argument is well-established for the family but is inferred from family biology rather than from the supplied sequence alone; a model lacking ferlin knowledge would need to rely on hydrophobicity analysis to reject the 630-652 region in option D.
- No experimental (e.g., crystallographic, cross-linking) evidence for the TM boundaries was found; the annotation is purely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Ferlin-family proteins (e.g., C. elegans FER-1/FER-2, human dysferlin) are well-characterized single-pass membrane proteins anchored by a single C-terminal transmembrane helix. This general family biology eliminates option D (which posits a second TM at 630-652). Option A (35-55: CCGREYRTEIKYAKSNVVSWD) contains charged residues (R, E, K, D) and is not hydrophobic enough for a TM helix. Option B (1408-1428) extends beyond the 1426-residue protein length and is therefore impossible. The remaining C-terminal hydrophobic stretch (VAAVVFLSIWIFVVAFLYPSL) is the only TM-like region, and its boundaries (1404-1424) correspond to the longest contiguous hydrophobic segment near the C-terminus.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact residue-level boundaries (1404 vs 1405/1406 as start; 1424 vs 1425 as end) are set by the automatic annotation algorithm and are somewhat fuzzy; however, among the four choices, only C survives the elimination of A (wrong location/hydrophobicity), B (out-of-range), and D (second TM contradicted by ferlin single-pass topology).",
    "reason": "The question is answerable through: (1) recognizing ferlins as single-pass membrane proteins to eliminate D; (2) noting the protein is 1426 AA to eliminate B (1428 out of range); (3) assessing hydrophobicity at 35-55 to eliminate A; (4) identifying the C-terminal hydrophobic stretch as the TM region. These are general biological and sequence-analysis arguments, not lookup of a specific database entry."
  },
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7J6K2G0 (Ferlin 2, Toxoplasma gondii, 1426 AA) annotates a single transmembrane helix at positions 1404-1424 (evidence C5, H4), matching choice C exactly. The evidence code ECO:0000255 indicates this is an automatic/computational prediction rather than experimental data, but the sequence at 1404-1424 (VAAVVFLSIWIFVVAFLYPSL) is indeed a hydrophobic stretch of ~21 residues consistent with a TM helix. No second TM region is annotated. The sequence matches the benchmark (SHA256 confirmed)."
  },
  "important_caveats": [
    "The TM annotation uses ECO:0000255 (automatic assertion according to rules), meaning it is a computational prediction, not experimental evidence. The true boundaries could shift by 1-2 residues.",
    "The reviewer-only evidence confirms sequence match (SHA256) and that the UniProt entry was first public 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed when the question was authored.",
    "The ferlin single-pass topology argument is well-established for the family but is inferred from family biology rather than from the supplied sequence alone; a model lacking ferlin knowledge would need to rely on hydrophobicity analysis to reject the 630-652 region in option D.",
    "No experimental (e.g., crystallographic, cross-linking) evidence for the TM boundaries was found; the annotation is purely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by sequence length (1426 < 1428). Option A is eliminated by lack of hydrophobicity (charged/polar residues dominate). Option D is eliminated by ferlin single-pass topology. Only C remains as a defensible answer. The exact boundaries 1404-1424 are annotation-set but are the only option consistent with the C-terminal hydrophobic segment after eliminating the others."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7J6K2G0 (Ferlin 2, Toxoplasma gondii, 1426 AA) annotates a single transmembrane helix at positions 1404-1424 (evidence C5, H4), matching choice C exactly. The evidence code ECO:0000255 indicates this is an automatic/computational prediction rather than experimental data, but the sequence at 1404-1424 (VAAVVFLSIWIFVVAFLYPSL) is indeed a hydrophobic stretch of ~21 residues consistent with a TM helix. No second TM region is annotated. The sequence matches the benchmark (SHA256 confirmed).",
    "evidence_ids": ["C5", "H4", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Ferlin-family proteins (e.g., C. elegans FER-1/FER-2, human dysferlin) are well-characterized single-pass membrane proteins anchored by a single C-terminal transmembrane helix. This general family biology eliminates option D (which posits a second TM at 630-652). Option A (35-55: CCGREYRTEIKYAKSNVVSWD) contains charged residues (R, E, K, D) and is not hydrophobic enough for a TM helix. Option B (1408-1428) extends beyond the 1426-residue protein length and is therefore impossible. The remaining C-terminal hydrophobic stretch (VAAVVFLSIWIFVVAFLYPSL) is the only TM-like region, and its boundaries (1404-1424) correspond to the longest contiguous hydrophobic segment near the C-terminus.",
    "missing_item_specific_fact": "The exact residue-level boundaries (1404 vs 1405/1406 as start; 1424 vs 1425 as end) are set by the automatic annotation algorithm and are somewhat fuzzy; however, among the four choices, only C survives the elimination of A (wrong location/hydrophobicity), B (out-of-range), and D (second TM contradicted by ferlin single-pass topology).",
    "reason": "The question is answerable through: (1) recognizing ferlins as single-pass membrane proteins to eliminate D; (2) noting the protein is 1426 AA to eliminate B (1428 out of range); (3) assessing hydrophobicity at 35-55 to eliminate A; (4) identifying the C-terminal hydrophobic stretch as the TM region. These are general biological and sequence-analysis arguments, not lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by sequence length (1426 < 1428). Option A is eliminated by lack of hydrophobicity (charged/polar residues dominate). Option D is eliminated by ferlin single-pass topology. Only C remains as a defensible answer. The exact boundaries 1404-1424 are annotation-set but are the only option consistent with the C-terminal hydrophobic segment after eliminating the others."
  },
  "important_caveats": [
    "The TM annotation uses ECO:0000255 (automatic assertion according to rules), meaning it is a computational prediction, not experimental evidence. The true boundaries could shift by 1-2 residues.",
    "The reviewer-only evidence confirms sequence match (SHA256) and that the UniProt entry was first public 2025-02-05; the author's data-construction date is unknown, so the annotation may not have existed when the question was authored.",
    "The ferlin single-pass topology argument is well-established for the family but is inferred from family biology rather than from the supplied sequence alone; a model lacking ferlin knowledge would need to rely on hydrophobicity analysis to reject the 630-652 region in option D.",
    "No experimental (e.g., crystallographic, cross-linking) evidence for the TM boundaries was found; the annotation is purely computational."
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

**Accession:** `A0A7J6K2G0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 12. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.269882+00:00.  

```json
"A0A7J6K2G0"
```

Source SHA-256: `68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.269882+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"30279285","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"33803212","source":"PubMed"}],"value":"Ferlin 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33803212","source":"PubMed"}],"value":"FER2"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"30279285","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"33803212","source":"PubMed"}],"value":"TgFER2"}]}}
```

Source SHA-256: `68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6K2G0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:50.269882+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":1424},"start":{"modifier":"EXACT","value":1404}},"type":"Transmembrane"}
```

Source SHA-256: `68f3954b7981cae134154b132eb88b59efc2c7ed6e73f6807fd866d3aecf8da6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6K2G0?format=txt&versions=12)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 12 / 1.  
**Retrieved:** 2026-11-01T06:27:33.007451+00:00.  

```text
FT   TRANSMEM        1404..1424
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c01f9ff322de973c7387b5304e5a6559153e4aa95c04b38f7d9f4abe69b2be9b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
