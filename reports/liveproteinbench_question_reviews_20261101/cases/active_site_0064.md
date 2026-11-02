# active_site_0064

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **B** — Position 64 (Nucleophile (Probable))

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTEELTTVRDACARTLENTARTLHLGASGTEFVAAFRAMTDHWGAARPHDLPLSDVSPDGSPVEYAVDLGGLAPALQFAMEPLTAGVPARDPLAARAIMPLLAGRYGADATRWSALADRLLPDDAHGPHVSMYGAEVRAGAPIRFKAWFYLNVTGPDGAFNLLYSALERMGTTHLWPVVQAHVHRAGEDVPFLLSLDLSDDPAARVKVYFRHFAADVEEVAAVLKAYPGFEPGEVRAFCKVMMGGRRRFSDQPAVTCVSLLDAQTFDRTAATLYVPLWTYAEHDGEVRQRVHRTLAAWPEALYRYDSVLAGIAHRGLDAGTGIHNYISWQPGRTRPRMKVYLSPEMHDVTPPPLGVSQQHHLSGQTTARGRTE

[Multiple Choices]
A. Position 213 (Proton acceptor)
B. Position 64 (Nucleophile (Probable))
C. Position 931 (Proton acceptor)
D. Position 268 (Proton acceptor)
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

> The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6), [C23](#evidence-c23), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.


**Missing item-specific fact**

> The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.


**Reason**

> Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence.


### Important caveats

- The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.
- The historical sequence match supports applicability, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.",
    "reason": "Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6",
      "C23",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment."
  },
  "important_caveats": [
    "The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt CymD entry, which annotates residue 64 as a probable nucleophile. The same annotation appears in a historical entry predating the benchmark cutoff. This supports B as an annotation-backed answer, while the qualifier “probable” should be retained; the excerpts do not independently establish direct experimental proof of the nucleophile assignment.",
    "evidence_ids": ["C5", "H6", "C23", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence allows residue numbering and identifies residue 64 as Glu, but the supplied sequence and choices do not provide a reliable general principle for assigning this specific residue the proposed nucleophile role. Position 931 is outside the 373-residue sequence, an easy elimination that does not distinguish B from the other in-range choices.",
    "missing_item_specific_fact": "The protein-specific CymD active-site annotation or structural/mechanistic evidence assigning residue 64 as a probable nucleophile.",
    "reason": "Selecting B over the in-range alternatives depends on protein-specific active-site knowledge absent from the input; recognizing the sequence or retrieving its annotation would be lookup, not reasoning from the supplied information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only matched-sequence annotation supports B, and the supplied evidence does not establish another listed option as an equally defensible active-site assignment. The out-of-range position 931 is not a plausible coordinate for this sequence."
  },
  "important_caveats": [
    "The active-site label is explicitly qualified as “Probable” and is evidence-linked to a publication; the excerpts do not independently validate the underlying mechanistic claim.",
    "The historical sequence match supports applicability, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6), [H9](#evidence-h9), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.


**Missing item-specific fact**

> The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.


**Reason**

> The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible.


### Important caveats

- The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.
- The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.
- The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.
- While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.",
    "reason": "The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence."
  },
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H6",
      "H9",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly."
  },
  "important_caveats": [
    "The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.",
    "The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.",
    "The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.",
    "While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A8M6W6 (CymD, Dimethylallyltryptophan synthase) annotates position 64 as 'Nucleophile (Probable)' active site (evidence ECO:0000303, citing PubMed:31251043, the 2019 Roose & Christianson crystallography paper). Position 64 in the supplied 373-aa sequence is E (glutamic acid), consistent with a carboxylate nucleophile attacking DMAPP. The binding-site annotation at 64 for L-tryptophan is additionally supported by experimental evidence (ECO:0000269) and PDB structures 6OS5/6OS6. The '(Probable)' qualifier indicates structural inference rather than definitive experimental proof of nucleophilic role, but the annotation is consistent and the answer matches the database record exactly.",
    "evidence_ids": ["C5", "C8", "H6", "H9", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "By counting residues in the supplied sequence: position 64 is E (glutamate), position 213 is F (phenylalanine), position 268 is R (arginine), and position 931 exceeds the 373-residue sequence length. General amino-acid chemistry provides meaningful discrimination: (1) position 931 is impossible, eliminating C; (2) phenylalanine has no ionizable side chain and cannot serve as a proton acceptor, eliminating A; (3) arginine's guanidinium group is a proton donor, not acceptor, eliminating D; (4) glutamate's carboxylate is a well-established nucleophile in enzymatic catalysis (e.g., serine protease catalytic triad, prenyltransferase mechanisms), making B the only chemically coherent option. The label 'Nucleophile (Probable)' aligns with a carboxylate attacking the allylic carbon of DMAPP in a prenyltransferase reaction.",
    "missing_item_specific_fact": "The specific mechanistic assignment of E64 as the nucleophile (rather than another glutamate or aspartate elsewhere in the sequence) derives from the 2019 crystallographic structure (PDB 6OS5/6OS6) of CymD. A general biologist could identify E as the most chemically plausible catalytic residue among the four choices, but confirming that this particular E64 (not, e.g., E81 or E234) is THE catalytic nucleophile requires protein-specific structural knowledge.",
    "reason": "The constrained multiple-choice format allows discrimination through general amino-acid chemistry: F and R are implausible proton acceptors, position 931 is out of range, and E is the only chemically sensible nucleophile among the options. This constitutes a concrete biological argument from the sequence and choices. However, the precise mechanistic role ('Nucleophile' vs. 'Proton acceptor') and the '(Probable)' qualifier are protein-specific annotations from the 2019 crystallography study, adding a lookup component for full confidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C (position 931) is trivially impossible given the 373-residue sequence. Options A (F213 as proton acceptor) and D (R268 as proton acceptor) are chemically implausible for the stated roles. Only B (E64 as nucleophile) is chemically coherent. No other option is defensible."
  },
  "important_caveats": [
    "The active-site annotation carries the '(Probable)' qualifier and evidence code ECO:0000303 (inferred from assertion in database record), indicating structural inference rather than direct experimental proof of nucleophilic catalysis at E64.",
    "The binding-site annotation at position 64 for L-tryptophan is experimentally supported (ECO:0000269, PDB 6OS5/6OS6), but the specific assignment as 'Nucleophile' is a mechanistic interpretation from the crystallographic study.",
    "The sequence-to-accession mapping (A8M6W6) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model must work from the sequence alone.",
    "While the reasoning path through amino-acid chemistry is valid, the specific identification of E64 as THE catalytic nucleophile (vs. other acidic residues in the sequence) ultimately rests on protein-specific structural data from PubMed:31251043."
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

**Accession:** `A8M6W6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 67. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.008171+00:00.  

```json
{"description":"Nucleophile (Probable)","evidences":[{"evidenceCode":"ECO:0000303","id":"31251043","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":64},"start":{"modifier":"EXACT","value":64}},"type":"Active site"}
```

Source SHA-256: `430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.008171+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"31251043","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"6OS5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6OS6","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:57912"}],"ligand":{"id":"ChEBI:CHEBI:57912","name":"L-tryptophan"},"location":{"end":{"modifier":"EXACT","value":64},"start":{"modifier":"EXACT","value":64}},"type":"Binding site"}
```

Source SHA-256: `430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6`.

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A8M6W6.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:12.008171+00:00.  

```json
{"citation":{"authors":["Roose B.W.","Christianson D.W."],"citationCrossReferences":[{"database":"PubMed","id":"31251043"},{"database":"DOI","id":"10.1021/acs.biochem.9b00399"}],"citationType":"journal article","firstPage":"3232","id":"31251043","journal":"Biochemistry","lastPage":"3242","publicationDate":"2019","title":"Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.","volume":"58"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6OS3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6OS5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6OS6","source":"PDB"}],"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE","FUNCTION","ACTIVE SITE"]}
```

Source SHA-256: `430fba885252de655ee65e60f6df2d47b963f5cca6aa9a0f937cd165c62abaf6`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)  
**Locator:** `lines 48-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:27:14.657088+00:00.  

```text
RN   [5] {ECO:0007744|PDB:6OS3, ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6}
RP   X-RAY CRYSTALLOGRAPHY (1.33 ANGSTROMS) OF 2-373 IN APO FORM AND IN
RP   COMPLEXES WITH L-TRYPTOPHAN AND DIMETHYLALLYL S-THIOLODIPHOSPHATE,
RP   FUNCTION, AND ACTIVE SITE.
RX   PubMed=31251043; DOI=10.1021/acs.biochem.9b00399;
RA   Roose B.W., Christianson D.W.;
RT   "Structural Basis of Tryptophan Reverse N-Prenylation Catalyzed by CymD.";
RL   Biochemistry 58:3232-3242(2019).
```

Source SHA-256: `eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)  
**Locator:** `lines 130-132`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:27:14.657088+00:00.  

```text
FT   ACT_SITE        64
FT                   /note="Nucleophile (Probable)"
FT                   /evidence="ECO:0000303|PubMed:31251043"
```

Source SHA-256: `eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A8M6W6?format=txt&versions=67)  
**Locator:** `lines 143-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 67 / 1.  
**Retrieved:** 2026-11-02T04:27:14.657088+00:00.  

```text
FT   BINDING         64
FT                   /ligand="L-tryptophan"
FT                   /ligand_id="ChEBI:CHEBI:57912"
FT                   /evidence="ECO:0000269|PubMed:31251043,
FT                   ECO:0007744|PDB:6OS5, ECO:0007744|PDB:6OS6"
```

Source SHA-256: `eed31694c4a491109a0e33b56fd6610d39003989821af3bc90ec6db9097adfc6`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
