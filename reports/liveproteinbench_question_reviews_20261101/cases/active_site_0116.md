# active_site_0116

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 83 (Acyl-ester intermediate)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKLLKILSLVCLSISIGACAEHSMSRAKTSTIPQVNNSIIDQNVQALFNEISADAVFVTYDGQNIKKYGTHLDRAKTAYIPASTFKIANALIGLENHKATSTEIFKWDGKPRFFKAWDKDFTLGEAMQASTVPVYQELARRIGPSLMQSELQRIGYGNMQIGTEVDQFWLKGPLTITPIQEVKFVYDLAQGQLPFKPEVQQQVKEMLYVERRGENRLYAKSGWGMAVDPQVGWYVGFVEKADGQVVAFALNMQMKAGDDIALRKQLSLDVLDKLGVFHYL

[Multiple Choices]
A. Position 83 (Acyl-ester intermediate)
B. Position 735 (For beta-ketoacyl synthase activity)
C. Position 234 (Proton donor)
D. Position 241 (Lowers pKa of active site Tyr)
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

> The sequence matches OXA-58, and the matched UniProt record annotates residue 83 as the acyl-ester intermediate, with evidence citing both a PubMed study and a PDB structure. This supports choice A, while preserving that the annotation combines evidence sources rather than representing a single independently reviewed experiment here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved SXXK motif of serine beta-lactamases (STFK); its serine is the nucleophile that forms an acyl-enzyme intermediate during beta-lactam hydrolysis. The motif’s serine is at position 83, supporting choice A. Choice B also names a position beyond this 280-residue sequence.


**Missing item-specific fact**

> Experimental or database confirmation of this particular protein’s residue-83 role is absent from the input, but the conserved sequence motif and its established chemistry meaningfully distinguish A.


**Reason**

> The active-site chemistry is supported by a recognizable conserved motif in the supplied sequence, not merely by recognizing the exact sequence or recalling an annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence motif and the stated acyl-enzyme role support A; the other options are inconsistent with the sequence length or the motif’s expected chemistry.


### Important caveats

- The reviewer-only UniProt and structural evidence was not supplied to the evaluated model and is used only to assess whether the key is supported.
- The exact sequence match and residue numbering refer to the canonical 280-residue entry; construct or isoform numbering is not assumed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved SXXK motif of serine beta-lactamases (STFK); its serine is the nucleophile that forms an acyl-enzyme intermediate during beta-lactam hydrolysis. The motif’s serine is at position 83, supporting choice A. Choice B also names a position beyond this 280-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Experimental or database confirmation of this particular protein’s residue-83 role is absent from the input, but the conserved sequence motif and its established chemistry meaningfully distinguish A.",
    "reason": "The active-site chemistry is supported by a recognizable conserved motif in the supplied sequence, not merely by recognizing the exact sequence or recalling an annotation."
  },
  "case_id": "active_site_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches OXA-58, and the matched UniProt record annotates residue 83 as the acyl-ester intermediate, with evidence citing both a PubMed study and a PDB structure. This supports choice A, while preserving that the annotation combines evidence sources rather than representing a single independently reviewed experiment here."
  },
  "important_caveats": [
    "The reviewer-only UniProt and structural evidence was not supplied to the evaluated model and is used only to assess whether the key is supported.",
    "The exact sequence match and residue numbering refer to the canonical 280-residue entry; construct or isoform numbering is not assumed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif and the stated acyl-enzyme role support A; the other options are inconsistent with the sequence length or the motif’s expected chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches OXA-58, and the matched UniProt record annotates residue 83 as the acyl-ester intermediate, with evidence citing both a PubMed study and a PDB structure. This supports choice A, while preserving that the annotation combines evidence sources rather than representing a single independently reviewed experiment here.",
    "evidence_ids": ["C1", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved SXXK motif of serine beta-lactamases (STFK); its serine is the nucleophile that forms an acyl-enzyme intermediate during beta-lactam hydrolysis. The motif’s serine is at position 83, supporting choice A. Choice B also names a position beyond this 280-residue sequence.",
    "missing_item_specific_fact": "Experimental or database confirmation of this particular protein’s residue-83 role is absent from the input, but the conserved sequence motif and its established chemistry meaningfully distinguish A.",
    "reason": "The active-site chemistry is supported by a recognizable conserved motif in the supplied sequence, not merely by recognizing the exact sequence or recalling an annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motif and the stated acyl-enzyme role support A; the other options are inconsistent with the sequence length or the motif’s expected chemistry."
  },
  "important_caveats": [
    "The reviewer-only UniProt and structural evidence was not supplied to the evaluated model and is used only to assess whether the key is supported.",
    "The exact sequence match and residue numbering refer to the canonical 280-residue entry; construct or isoform numbering is not assumed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2TR58 (Beta-lactamase OXA-58, 280 AA, sequence matched) explicitly annotates position 83 as 'Active site' with description 'Acyl-ester intermediate' (C5, H5). This annotation is supported by experimental evidence (PubMed:26459904, PDB:4Y0U) and mutagenesis studies confirming Ser-83 is the catalytic nucleophile (C13, H3). The residue at position 83 in the supplied sequence is indeed Ser (S), consistent with the class D beta-lactamase ST motif. The binding-site annotation at position 83 for beta-lactam ligand (C6, H6) further corroborates.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C13](#evidence-c13), [H5](#evidence-h5), [H6](#evidence-h6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Option B (position 735) is trivially eliminated because the protein is only 280 amino acids. Among the remaining options, the sequence context at positions 82-84 is 'S-T-F' (the Ser-Thr motif), which is the well-known catalytic dyad hallmark of class D (OXA-type) beta-lactamases. The description 'Acyl-ester intermediate' (option A) precisely matches the canonical serine-nucleophile mechanism of beta-lactam hydrolysis (Ser attacks the beta-lactam carbonyl to form a covalent acyl-enzyme). Options C ('Proton donor') and D ('Lowers pKa of active site Tyr') describe mechanistic roles inconsistent with class D beta-lactamase catalysis, which does not employ a Tyr-based mechanism. The N-terminal signal peptide (MKLLKILSLVCLSISIGACA) is consistent with a secreted/periplasmic enzyme, fitting a beta-lactamase.


**Missing item-specific fact**

> Precise recognition that this specific 280-aa sequence is OXA-58 and that the ST motif at position 82-83 is the catalytic center (rather than another Ser/Thr elsewhere in the sequence) benefits from database lookup, though the ST-F motif context and mechanistic descriptions provide meaningful biological discrimination.


**Reason**

> The elimination of option B is trivial (position exceeds protein length). The identification of the Ser-Thr motif at 82-83 as the catalytic center, combined with the mechanistic description 'Acyl-ester intermediate' matching serine beta-lactamase catalysis, and the inconsistency of options C and D with class D beta-lactamase mechanism, provides a defensible biological argument. However, confident identification of the ST motif specifically at position 82-83 (vs. other S/T residues) without database confirmation requires specialized knowledge of class D beta-lactamase architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is impossible (position 735 in a 280-aa protein). Options C and D describe mechanistic roles (proton donor, Tyr pKa lowering) that are inconsistent with the serine-nucleophile mechanism of class D beta-lactamases. Only option A is consistent with both the sequence motif (ST at 82-83) and the canonical catalytic mechanism.


### Important caveats

- The evaluated model was not given the UniProt accession or protein identity; identification relies on sequence-level pattern recognition.
- The ST motif at position 82-83 is suggestive but not uniquely diagnostic without broader structural context; however, combined with the mechanistic descriptions in the options, it provides meaningful discrimination.
- The UniProt annotation for position 83 includes both computational (PIRSR, ECO:0000255) and experimental (PubMed, PDB) evidence codes, strengthening the key.
- Option B (position 735) is an obviously invalid distractor for a 280-aa protein, reducing the effective question to a 3-way choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (position 735) is trivially eliminated because the protein is only 280 amino acids. Among the remaining options, the sequence context at positions 82-84 is 'S-T-F' (the Ser-Thr motif), which is the well-known catalytic dyad hallmark of class D (OXA-type) beta-lactamases. The description 'Acyl-ester intermediate' (option A) precisely matches the canonical serine-nucleophile mechanism of beta-lactam hydrolysis (Ser attacks the beta-lactam carbonyl to form a covalent acyl-enzyme). Options C ('Proton donor') and D ('Lowers pKa of active site Tyr') describe mechanistic roles inconsistent with class D beta-lactamase catalysis, which does not employ a Tyr-based mechanism. The N-terminal signal peptide (MKLLKILSLVCLSISIGACA) is consistent with a secreted/periplasmic enzyme, fitting a beta-lactamase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition that this specific 280-aa sequence is OXA-58 and that the ST motif at position 82-83 is the catalytic center (rather than another Ser/Thr elsewhere in the sequence) benefits from database lookup, though the ST-F motif context and mechanistic descriptions provide meaningful biological discrimination.",
    "reason": "The elimination of option B is trivial (position exceeds protein length). The identification of the Ser-Thr motif at 82-83 as the catalytic center, combined with the mechanistic description 'Acyl-ester intermediate' matching serine beta-lactamase catalysis, and the inconsistency of options C and D with class D beta-lactamase mechanism, provides a defensible biological argument. However, confident identification of the ST motif specifically at position 82-83 (vs. other S/T residues) without database confirmation requires specialized knowledge of class D beta-lactamase architecture."
  },
  "case_id": "active_site_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C13",
      "H5",
      "H6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2TR58 (Beta-lactamase OXA-58, 280 AA, sequence matched) explicitly annotates position 83 as 'Active site' with description 'Acyl-ester intermediate' (C5, H5). This annotation is supported by experimental evidence (PubMed:26459904, PDB:4Y0U) and mutagenesis studies confirming Ser-83 is the catalytic nucleophile (C13, H3). The residue at position 83 in the supplied sequence is indeed Ser (S), consistent with the class D beta-lactamase ST motif. The binding-site annotation at position 83 for beta-lactam ligand (C6, H6) further corroborates."
  },
  "important_caveats": [
    "The evaluated model was not given the UniProt accession or protein identity; identification relies on sequence-level pattern recognition.",
    "The ST motif at position 82-83 is suggestive but not uniquely diagnostic without broader structural context; however, combined with the mechanistic descriptions in the options, it provides meaningful discrimination.",
    "The UniProt annotation for position 83 includes both computational (PIRSR, ECO:0000255) and experimental (PubMed, PDB) evidence codes, strengthening the key.",
    "Option B (position 735) is an obviously invalid distractor for a 280-aa protein, reducing the effective question to a 3-way choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is impossible (position 735 in a 280-aa protein). Options C and D describe mechanistic roles (proton donor, Tyr pKa lowering) that are inconsistent with the serine-nucleophile mechanism of class D beta-lactamases. Only option A is consistent with both the sequence motif (ST at 82-83) and the canonical catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2TR58 (Beta-lactamase OXA-58, 280 AA, sequence matched) explicitly annotates position 83 as 'Active site' with description 'Acyl-ester intermediate' (C5, H5). This annotation is supported by experimental evidence (PubMed:26459904, PDB:4Y0U) and mutagenesis studies confirming Ser-83 is the catalytic nucleophile (C13, H3). The residue at position 83 in the supplied sequence is indeed Ser (S), consistent with the class D beta-lactamase ST motif. The binding-site annotation at position 83 for beta-lactam ligand (C6, H6) further corroborates.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C13", "H5", "H6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Option B (position 735) is trivially eliminated because the protein is only 280 amino acids. Among the remaining options, the sequence context at positions 82-84 is 'S-T-F' (the Ser-Thr motif), which is the well-known catalytic dyad hallmark of class D (OXA-type) beta-lactamases. The description 'Acyl-ester intermediate' (option A) precisely matches the canonical serine-nucleophile mechanism of beta-lactam hydrolysis (Ser attacks the beta-lactam carbonyl to form a covalent acyl-enzyme). Options C ('Proton donor') and D ('Lowers pKa of active site Tyr') describe mechanistic roles inconsistent with class D beta-lactamase catalysis, which does not employ a Tyr-based mechanism. The N-terminal signal peptide (MKLLKILSLVCLSISIGACA) is consistent with a secreted/periplasmic enzyme, fitting a beta-lactamase.",
    "missing_item_specific_fact": "Precise recognition that this specific 280-aa sequence is OXA-58 and that the ST motif at position 82-83 is the catalytic center (rather than another Ser/Thr elsewhere in the sequence) benefits from database lookup, though the ST-F motif context and mechanistic descriptions provide meaningful biological discrimination.",
    "reason": "The elimination of option B is trivial (position exceeds protein length). The identification of the Ser-Thr motif at 82-83 as the catalytic center, combined with the mechanistic description 'Acyl-ester intermediate' matching serine beta-lactamase catalysis, and the inconsistency of options C and D with class D beta-lactamase mechanism, provides a defensible biological argument. However, confident identification of the ST motif specifically at position 82-83 (vs. other S/T residues) without database confirmation requires specialized knowledge of class D beta-lactamase architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is impossible (position 735 in a 280-aa protein). Options C and D describe mechanistic roles (proton donor, Tyr pKa lowering) that are inconsistent with the serine-nucleophile mechanism of class D beta-lactamases. Only option A is consistent with both the sequence motif (ST at 82-83) and the canonical catalytic mechanism."
  },
  "important_caveats": [
    "The evaluated model was not given the UniProt accession or protein identity; identification relies on sequence-level pattern recognition.",
    "The ST motif at position 82-83 is suggestive but not uniquely diagnostic without broader structural context; however, combined with the mechanistic descriptions in the options, it provides meaningful discrimination.",
    "The UniProt annotation for position 83 includes both computational (PIRSR, ECO:0000255) and experimental (PubMed, PDB) evidence codes, strengthening the key.",
    "Option B (position 735) is an obviously invalid distractor for a 280-aa protein, reducing the effective question to a 3-way choice."
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

**Accession:** `Q2TR58` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 133. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
"Q2TR58"
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000269","id":"15616297","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"26701320","source":"PubMed"}],"value":"3.5.2.6"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"RU361140","source":"RuleBase"},{"evidenceCode":"ECO:0000303","id":"15616297","source":"PubMed"}],"value":"Beta-lactamase OXA-58"}}}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"description":"Acyl-ester intermediate","evidences":[{"evidenceCode":"ECO:0000255","id":"PIRSR602137-50","source":"PIRSR"},{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"4Y0U","source":"PDB"}],"location":{"end":{"modifier":"EXACT","value":83},"start":{"modifier":"EXACT","value":83}},"type":"Active site"}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"26459904","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"4Y0U","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:35627"}],"ligand":{"id":"ChEBI:CHEBI:35627","name":"a beta-lactam"},"location":{"end":{"modifier":"EXACT","value":83},"start":{"modifier":"EXACT","value":83}},"type":"Binding site"}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TR58.json)  
**Locator:** `/references/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:39.664161+00:00.  

```json
{"citation":{"authors":["Saino H.","Sugiyabu T.","Ueno G.","Yamamoto M.","Ishii Y.","Miyano M."],"citationCrossReferences":[{"database":"PubMed","id":"26701320"},{"database":"DOI","id":"10.1371/journal.pone.0145869"}],"citationType":"journal article","firstPage":"e0145869","id":"26701320","journal":"PLoS ONE","lastPage":"e0145869","publicationDate":"2015","title":"Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed State: Insights into the Mobility and Stability of the OXA-58 Structure.","volume":"10"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5BOH","source":"PDB"}],"referenceNumber":23,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","CARBOXYLATION AT LYS-86","MUTAGENESIS OF SER-83 AND TRP-169"]}
```

Source SHA-256: `90800739268b3a91a720a2ca6b56cd2e1f1fdaaa169bc64ee8999ea5771dcb35`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 227-235`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
RN   [23] {ECO:0007744|PDB:5BOH}
RP   X-RAY CRYSTALLOGRAPHY (1.80 ANGSTROMS) OF 44-280, FUNCTION, CATALYTIC
RP   ACTIVITY, ACTIVITY REGULATION, CARBOXYLATION AT LYS-86, AND MUTAGENESIS OF
RP   SER-83 AND TRP-169.
RX   PubMed=26701320; DOI=10.1371/journal.pone.0145869;
RA   Saino H., Sugiyabu T., Ueno G., Yamamoto M., Ishii Y., Miyano M.;
RT   "Crystal Structure of OXA-58 with the Substrate-Binding Cleft in a Closed
RT   State: Insights into the Mobility and Stability of the OXA-58 Structure.";
RL   PLoS ONE 10:e0145869-e0145869(2015).
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 457-460`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
FT   ACT_SITE        83
FT                   /note="Acyl-ester intermediate"
FT                   /evidence="ECO:0000255|PIRSR:PIRSR602137-50,
FT                   ECO:0000269|PubMed:26459904, ECO:0007744|PDB:4Y0U"
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TR58?format=txt&versions=133)  
**Locator:** `lines 461-465`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 133 / 1.  
**Retrieved:** 2026-11-02T04:30:42.289456+00:00.  

```text
FT   BINDING         83
FT                   /ligand="a beta-lactam"
FT                   /ligand_id="ChEBI:CHEBI:35627"
FT                   /evidence="ECO:0000269|PubMed:26459904,
FT                   ECO:0007744|PDB:4Y0U"
```

Source SHA-256: `866adbe4a25883d784b4da01795f3c6d0f8328c05c58ea698350889ad138c921`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
