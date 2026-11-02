# cofactor_0139

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKKIAIIFGGNSPEYTVSLASATSAIEALQSSPYDYDLSLIGIAPDAMDWYLYTGELENIRQDTWLLDTKHKQKIQPLFEGNGFWLSEEQQTLVPDVLFPIMHGKYGEDGSIQGLFELMKLPYVGCGVAGSALCMNKWLLHQAAAAIGVQSAPTILLTNQANQQEQIEAFIQTHGFPVFFKPNEAGSSKGITKVTCVEEIASALKEAFTYCSAVLLQKNIAGVEIGCGILGNDSLTVGACDAISLVDGFFDFEEKYQLISAKITVPAPLPETIETKVKEQAQLLYRSLGLKGLARIDFFVTERGELYLNEINTMPGFTSHSRYPAMMAAVGLSYQELLQKLLVLAKEEVK

[Multiple Choices]
A. heme b
B. Mn(2+)
C. Zn(2+)
D. Mg(2+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches the VanC2 ligase entry, whose cofactor annotation includes Mg(2+). That annotation is based on a PROSITE rule and says the enzyme binds two Mg(2+) or Mn(2+) ions per subunit; it supports Mg(2+) but does not establish it as the exclusive choice.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices include plausible catalytic metal ions, but the sequence and general knowledge that this is an ATP-dependent ligase do not distinguish Mg(2+) from Mn(2+) for this particular protein.


**Missing item-specific fact**

> The protein-specific cofactor annotation or experimental metal-dependence measurement; the available annotation allows either Mg(2+) or Mn(2+).


**Reason**

> Selecting a metal requires a protein-specific fact absent from the prompt, and even the reviewer-only annotation does not make Mg(2+) unique.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The matched-sequence annotation explicitly states that the protein binds Mg(2+) or Mn(2+), so both listed choices are defensible.


### Important caveats

- The cofactor annotation is computationally supported by a PROSITE rule, not established as an experimental measurement in the supplied evidence.
- The cited literature concerns VanC2 function, but the provided excerpts do not independently establish which metal was experimentally required.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices include plausible catalytic metal ions, but the sequence and general knowledge that this is an ATP-dependent ligase do not distinguish Mg(2+) from Mn(2+) for this particular protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental metal-dependence measurement; the available annotation allows either Mg(2+) or Mn(2+).",
    "reason": "Selecting a metal requires a protein-specific fact absent from the prompt, and even the reviewer-only annotation does not make Mg(2+) unique."
  },
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the VanC2 ligase entry, whose cofactor annotation includes Mg(2+). That annotation is based on a PROSITE rule and says the enzyme binds two Mg(2+) or Mn(2+) ions per subunit; it supports Mg(2+) but does not establish it as the exclusive choice."
  },
  "important_caveats": [
    "The cofactor annotation is computationally supported by a PROSITE rule, not established as an experimental measurement in the supplied evidence.",
    "The cited literature concerns VanC2 function, but the provided excerpts do not independently establish which metal was experimentally required."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The matched-sequence annotation explicitly states that the protein binds Mg(2+) or Mn(2+), so both listed choices are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the VanC2 ligase entry, whose cofactor annotation includes Mg(2+). That annotation is based on a PROSITE rule and says the enzyme binds two Mg(2+) or Mn(2+) ions per subunit; it supports Mg(2+) but does not establish it as the exclusive choice.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices include plausible catalytic metal ions, but the sequence and general knowledge that this is an ATP-dependent ligase do not distinguish Mg(2+) from Mn(2+) for this particular protein.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental metal-dependence measurement; the available annotation allows either Mg(2+) or Mn(2+).",
    "reason": "Selecting a metal requires a protein-specific fact absent from the prompt, and even the reviewer-only annotation does not make Mg(2+) unique."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The matched-sequence annotation explicitly states that the protein binds Mg(2+) or Mn(2+), so both listed choices are defensible."
  },
  "important_caveats": [
    "The cofactor annotation is computationally supported by a PROSITE rule, not established as an experimental measurement in the supplied evidence.",
    "The cited literature concerns VanC2 function, but the provided excerpts do not independently establish which metal was experimentally required."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q47720 (VanC2, D-Ala-D-Ser ligase, EC 6.3.2.35) explicitly lists Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' The evidence code is ECO:0000255 (PROSITE-ProRule PRU00409), a computational family-rule annotation rather than a single-protein experimental measurement. Mg(2+) is indeed a supported cofactor for this protein. However, Mn(2+) is equally listed as a valid cofactor in the same annotation, meaning the author's exclusive selection of Mg(2+) over Mn(2+) is not uniquely determined by the annotation alone.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence belongs to the D-Ala-D-Ala ligase (ATP-grasp) superfamily, identifiable by conserved motifs (e.g., the 'GGNSPEY' and 'CGVAGSAL' regions characteristic of the Ddl/Van ligase fold). Members of this superfamily (VanA, VanB, VanC, Ddl) canonically require Mg(2+) to coordinate the β- and γ-phosphates of ATP during the two-step ligation mechanism. This family-level cofactor preference is general biochemical knowledge. Mn(2+) can substitute in vitro for some family members but Mg(2+) is the physiological cofactor.


**Missing item-specific fact**

> The specific annotation for VanC2 lists BOTH Mg(2+) and Mn(2+) as valid cofactors ('Mg(2+) or Mn(2+)'), making the exclusive choice of Mg(2+) over Mn(2+) dependent on knowing which is the preferred/physiological ion for this particular enzyme variant, which is not uniquely resolvable from the annotation text alone.


**Reason**

> A knowledgeable biochemist can reason from the ATP-grasp fold and D-Ala-D-Ala ligase family identity to Mg(2+) as the canonical cofactor. However, the annotation's 'or' language and the presence of Mn(2+) as an equally valid option introduce ambiguity that cannot be fully resolved by general reasoning without additional experimental data specific to VanC2's relative ion preference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The UniProt COFACTOR annotation for Q47720 lists both Mg(2+) and Mn(2+) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Both choices B and D are supported by the same evidence code (ECO:0000255|PROSITE-ProRule:PRU00409). The question asks for 'the specific cofactor required,' but the annotation does not uniquely privilege Mg(2+) over Mn(2+) for this protein. Mg(2+) is the more commonly emphasized primary cofactor in the D-Ala-D-Ala ligase literature, but Mn(2+) is not excluded.


### Important caveats

- The cofactor annotation is based on PROSITE-ProRule PRU00409 (ECO:0000255), a computational family-rule annotation, not a single-protein experimental cofactor determination.
- Experimental papers (PubMed 9294159, 9545431) characterized VanC2's biophysical properties but the specific relative preference for Mg(2+) vs Mn(2+) is not quoted in the supplied excerpts.
- The author's choice of Mg(2+) as the sole correct answer is defensible as the canonical family cofactor but is not uniquely determined by the annotation, which lists Mn(2+) as equally valid.
- Sequence identity is confirmed (SHA-256 match to Q47720, 350 aa, sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence belongs to the D-Ala-D-Ala ligase (ATP-grasp) superfamily, identifiable by conserved motifs (e.g., the 'GGNSPEY' and 'CGVAGSAL' regions characteristic of the Ddl/Van ligase fold). Members of this superfamily (VanA, VanB, VanC, Ddl) canonically require Mg(2+) to coordinate the β- and γ-phosphates of ATP during the two-step ligation mechanism. This family-level cofactor preference is general biochemical knowledge. Mn(2+) can substitute in vitro for some family members but Mg(2+) is the physiological cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific annotation for VanC2 lists BOTH Mg(2+) and Mn(2+) as valid cofactors ('Mg(2+) or Mn(2+)'), making the exclusive choice of Mg(2+) over Mn(2+) dependent on knowing which is the preferred/physiological ion for this particular enzyme variant, which is not uniquely resolvable from the annotation text alone.",
    "reason": "A knowledgeable biochemist can reason from the ATP-grasp fold and D-Ala-D-Ala ligase family identity to Mg(2+) as the canonical cofactor. However, the annotation's 'or' language and the presence of Mn(2+) as an equally valid option introduce ambiguity that cannot be fully resolved by general reasoning without additional experimental data specific to VanC2's relative ion preference."
  },
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q47720 (VanC2, D-Ala-D-Ser ligase, EC 6.3.2.35) explicitly lists Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' The evidence code is ECO:0000255 (PROSITE-ProRule PRU00409), a computational family-rule annotation rather than a single-protein experimental measurement. Mg(2+) is indeed a supported cofactor for this protein. However, Mn(2+) is equally listed as a valid cofactor in the same annotation, meaning the author's exclusive selection of Mg(2+) over Mn(2+) is not uniquely determined by the annotation alone."
  },
  "important_caveats": [
    "The cofactor annotation is based on PROSITE-ProRule PRU00409 (ECO:0000255), a computational family-rule annotation, not a single-protein experimental cofactor determination.",
    "Experimental papers (PubMed 9294159, 9545431) characterized VanC2's biophysical properties but the specific relative preference for Mg(2+) vs Mn(2+) is not quoted in the supplied excerpts.",
    "The author's choice of Mg(2+) as the sole correct answer is defensible as the canonical family cofactor but is not uniquely determined by the annotation, which lists Mn(2+) as equally valid.",
    "Sequence identity is confirmed (SHA-256 match to Q47720, 350 aa, sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The UniProt COFACTOR annotation for Q47720 lists both Mg(2+) and Mn(2+) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Both choices B and D are supported by the same evidence code (ECO:0000255|PROSITE-ProRule:PRU00409). The question asks for 'the specific cofactor required,' but the annotation does not uniquely privilege Mg(2+) over Mn(2+) for this protein. Mg(2+) is the more commonly emphasized primary cofactor in the D-Ala-D-Ala ligase literature, but Mn(2+) is not excluded."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0139",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q47720 (VanC2, D-Ala-D-Ser ligase, EC 6.3.2.35) explicitly lists Mg(2+) as a cofactor (CHEBI:18420), with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' The evidence code is ECO:0000255 (PROSITE-ProRule PRU00409), a computational family-rule annotation rather than a single-protein experimental measurement. Mg(2+) is indeed a supported cofactor for this protein. However, Mn(2+) is equally listed as a valid cofactor in the same annotation, meaning the author's exclusive selection of Mg(2+) over Mn(2+) is not uniquely determined by the annotation alone.",
    "evidence_ids": ["C5", "H5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence belongs to the D-Ala-D-Ala ligase (ATP-grasp) superfamily, identifiable by conserved motifs (e.g., the 'GGNSPEY' and 'CGVAGSAL' regions characteristic of the Ddl/Van ligase fold). Members of this superfamily (VanA, VanB, VanC, Ddl) canonically require Mg(2+) to coordinate the β- and γ-phosphates of ATP during the two-step ligation mechanism. This family-level cofactor preference is general biochemical knowledge. Mn(2+) can substitute in vitro for some family members but Mg(2+) is the physiological cofactor.",
    "missing_item_specific_fact": "The specific annotation for VanC2 lists BOTH Mg(2+) and Mn(2+) as valid cofactors ('Mg(2+) or Mn(2+)'), making the exclusive choice of Mg(2+) over Mn(2+) dependent on knowing which is the preferred/physiological ion for this particular enzyme variant, which is not uniquely resolvable from the annotation text alone.",
    "reason": "A knowledgeable biochemist can reason from the ATP-grasp fold and D-Ala-D-Ala ligase family identity to Mg(2+) as the canonical cofactor. However, the annotation's 'or' language and the presence of Mn(2+) as an equally valid option introduce ambiguity that cannot be fully resolved by general reasoning without additional experimental data specific to VanC2's relative ion preference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The UniProt COFACTOR annotation for Q47720 lists both Mg(2+) and Mn(2+) with the note 'Binds 2 Mg(2+) or Mn(2+) ions per subunit.' Both choices B and D are supported by the same evidence code (ECO:0000255|PROSITE-ProRule:PRU00409). The question asks for 'the specific cofactor required,' but the annotation does not uniquely privilege Mg(2+) over Mn(2+) for this protein. Mg(2+) is the more commonly emphasized primary cofactor in the D-Ala-D-Ala ligase literature, but Mn(2+) is not excluded."
  },
  "important_caveats": [
    "The cofactor annotation is based on PROSITE-ProRule PRU00409 (ECO:0000255), a computational family-rule annotation, not a single-protein experimental cofactor determination.",
    "Experimental papers (PubMed 9294159, 9545431) characterized VanC2's biophysical properties but the specific relative preference for Mg(2+) vs Mn(2+) is not quoted in the supplied excerpts.",
    "The author's choice of Mg(2+) as the sole correct answer is defensible as the canonical family cofactor but is not uniquely determined by the annotation, which lists Mn(2+) as equally valid.",
    "Sequence identity is confirmed (SHA-256 match to Q47720, 350 aa, sequence version 1)."
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

**Accession:** `Q47720` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 147. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
"Q47720"
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00047","source":"HAMAP-Rule"}],"value":"D-alanine--D-serine ligase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanC2 ligase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"9545431","source":"PubMed"}],"value":"6.3.2.35"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"},{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin C-type resistance protein VanC2"}}}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00409","source":"PROSITE-ProRule"}],"name":"Mg(2+)"},{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29035"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00409","source":"PROSITE-ProRule"}],"name":"Mn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00409","source":"PROSITE-ProRule"}],"value":"Binds 2 Mg(2+) or Mn(2+) ions per subunit."}]}}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Park I.S.","Lin C.H.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9294159"},{"database":"DOI","id":"10.1073/pnas.94.19.10040"}],"citationType":"journal article","firstPage":"10040","id":"9294159","journal":"Proc. Natl. Acad. Sci. U.S.A.","lastPage":"10044","publicationDate":"1997","title":"Bacterial resistance to vancomycin: overproduction, purification, and characterization of VanC2 from Enterococcus casseliflavus as a D-Ala-D-Ser ligase.","volume":"94"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"9294159","source":"PubMed"}],"type":"STRAIN","value":"ATCC 25788"}],"referenceNumber":4,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","ACTIVITY REGULATION","SUBUNIT"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q47720.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:46.048238+00:00.  

```json
{"citation":{"authors":["Healy V.L.","Park I.S.","Walsh C.T."],"citationCrossReferences":[{"database":"PubMed","id":"9545431"},{"database":"DOI","id":"10.1016/s1074-5521(98)90633-0"}],"citationType":"journal article","firstPage":"197","id":"9545431","journal":"Chem. Biol.","lastPage":"207","publicationDate":"1998","title":"Active-site mutants of the VanC2 D-alanyl-D-serine ligase, characteristic of one vancomycin-resistant bacterial phenotype, revert towards wild-type D-alanyl-D-alanine ligases.","volume":"5"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":5,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF PHE-250 AND ARG-322"]}
```

Source SHA-256: `06db9d8bdf71a60d46c0d76bf8119766f2c979bd548827237a9036af1752f4cd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q47720?format=txt&versions=147)  
**Locator:** `lines 77-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 147 / 1.  
**Retrieved:** 2026-11-02T04:30:51.643943+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00409};
CC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00409};
CC       Note=Binds 2 Mg(2+) or Mn(2+) ions per subunit. {ECO:0000255|PROSITE-
CC       ProRule:PRU00409};
```

Source SHA-256: `7cd95341b40880e3967efdffddc7f3a25c7982d99fb2b3f1cf21db004390d78a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 139. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
