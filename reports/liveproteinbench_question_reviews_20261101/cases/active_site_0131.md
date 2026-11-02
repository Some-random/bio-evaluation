# active_site_0131

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 166 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. Position 2723 (Proton acceptor; for dehydratase activity 2)
B. Position 283 (Proton donor/acceptor)
C. Position 166 (Proton acceptor)
D. Position 347 (Cysteine persulfide intermediate)
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

> The exact-matched sequence is annotated at position 166 as a proton acceptor. The annotation is supported by similarity transfer, not direct experimental evidence for this residue in this protein.

Citations as saved: [C5](#evidence-c5), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Tyr-X3-Lys motif at positions 166–170, consistent with the catalytic motif of NAD-dependent sugar epimerases; Tyr166 is a plausible catalytic acid/base. Position 283 is alanine, whose side chain is not a plausible proton donor or acceptor.


**Missing item-specific fact**

> Direct experimental confirmation of Tyr166's role is not supplied, but is not required to distinguish the choices using the sequence motif and enzyme-family context.


**Reason**

> The motif and enzyme-family context provide a concrete sequence-based argument for C, rather than relying only on recalling a database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A and D give positions beyond the 341-residue sequence, while B assigns proton-transfer activity to alanine at position 283; C is the plausible choice.


### Important caveats

- The database active-site annotation cites similarity-based evidence (ECO:0000250); it should not be described as direct experimental validation for this exact protein.
- The sequence match establishes applicability to the supplied sequence, but the actual source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Tyr-X3-Lys motif at positions 166–170, consistent with the catalytic motif of NAD-dependent sugar epimerases; Tyr166 is a plausible catalytic acid/base. Position 283 is alanine, whose side chain is not a plausible proton donor or acceptor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Direct experimental confirmation of Tyr166's role is not supplied, but is not required to distinguish the choices using the sequence motif and enzyme-family context.",
    "reason": "The motif and enzyme-family context provide a concrete sequence-based argument for C, rather than relying only on recalling a database annotation."
  },
  "case_id": "active_site_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated at position 166 as a proton acceptor. The annotation is supported by similarity transfer, not direct experimental evidence for this residue in this protein."
  },
  "important_caveats": [
    "The database active-site annotation cites similarity-based evidence (ECO:0000250); it should not be described as direct experimental validation for this exact protein.",
    "The sequence match establishes applicability to the supplied sequence, but the actual source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D give positions beyond the 341-residue sequence, while B assigns proton-transfer activity to alanine at position 283; C is the plausible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched sequence is annotated at position 166 as a proton acceptor. The annotation is supported by similarity transfer, not direct experimental evidence for this residue in this protein.",
    "evidence_ids": ["C5", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Tyr-X3-Lys motif at positions 166–170, consistent with the catalytic motif of NAD-dependent sugar epimerases; Tyr166 is a plausible catalytic acid/base. Position 283 is alanine, whose side chain is not a plausible proton donor or acceptor.",
    "missing_item_specific_fact": "Direct experimental confirmation of Tyr166's role is not supplied, but is not required to distinguish the choices using the sequence motif and enzyme-family context.",
    "reason": "The motif and enzyme-family context provide a concrete sequence-based argument for C, rather than relying only on recalling a database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A and D give positions beyond the 341-residue sequence, while B assigns proton-transfer activity to alanine at position 283; C is the plausible choice."
  },
  "important_caveats": [
    "The database active-site annotation cites similarity-based evidence (ECO:0000250); it should not be described as direct experimental validation for this exact protein.",
    "The sequence match establishes applicability to the supplied sequence, but the actual source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8KN66 (WbpP, UDP-GlcNAc C4 epimerase, 341 aa) annotates position 166 as 'Active site: Proton acceptor' (evidence C5/H8). The evidence code is ECO:0000250 (inferred by similarity from P09147, galactose-4-epimerase), so the specific 'proton acceptor' label is a computational transfer. However, position 166 is independently confirmed by X-ray crystallography (PDB 1SB8/1SB9, PubMed 15016816) as a binding site for both NAD+ and UDP-GalNAc, and residue 166 in the supplied sequence is Tyrosine—consistent with the SDR-family catalytic tetrad Tyr that acts as proton acceptor/donor. The annotation is thus well-supported by structural and mechanistic evidence, though the precise mechanistic label is by homology transfer.

Citations as saved: [C5](#evidence-c5), [C19](#evidence-c19), [C20](#evidence-c20), [H8](#evidence-h8), [H22](#evidence-h22), [H23](#evidence-h23), [C33](#evidence-c33).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is an SDR-family NAD-dependent epimerase (Rossmann-fold NAD-binding motif TGAVGF visible near residues 22–27; NAD+ and UDP-sugar binding sites annotated). SDR enzymes use a catalytic Tyr in the YxxxK tetrad as the proton acceptor/donor. Options A (position 2723) and D (position 347) exceed the 341-residue sequence length and are trivially impossible. Between B (position 283) and C (position 166), reading the sequence reveals position 166 is Tyrosine (Y)—the canonical SDR catalytic residue—while position 283 is Alanine (A), which cannot serve as a proton acceptor. A model with knowledge of SDR catalytic chemistry and the ability to count residues in the supplied sequence can eliminate all wrong options without database lookup.


**Missing item-specific fact**

> None critical. The reasoning path relies on (1) recognizing the SDR fold and catalytic Tyr mechanism, (2) counting to identify residue identities at the candidate positions, and (3) noting that two options exceed sequence length. All information is derivable from the supplied sequence and general SDR biochemistry.


**Reason**

> The question provides the full 341-residue sequence and four options. Two options (A, D) are immediately eliminated as impossible positions. The remaining discrimination between B (Ala at 283) and C (Tyr at 166) is resolved by the well-established SDR catalytic mechanism in which a tyrosine serves as the proton acceptor. This is general enzyme-family knowledge, not a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and D reference positions (2723, 347) beyond the 341-residue sequence, making them physically impossible. Option B places a proton donor/acceptor at position 283, which is Alanine—incapable of proton transfer. Only option C (Tyr-166) is consistent with both the sequence content and SDR catalytic chemistry.


### Important caveats

- The UniProt 'Proton acceptor' annotation at position 166 carries evidence code ECO:0000250 (similarity transfer from P09147), not direct experimental demonstration on WbpP itself. However, crystallographic data (1SB8/1SB9) confirm residue 166 contacts both NAD+ and the UDP-sugar substrate, strongly supporting its catalytic role.
- Distractors A and D are extremely easy to eliminate (positions exceed sequence length), reducing the effective discrimination to a two-way choice between B and C.
- The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path described above relies solely on the supplied sequence and general SDR biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is an SDR-family NAD-dependent epimerase (Rossmann-fold NAD-binding motif TGAVGF visible near residues 22–27; NAD+ and UDP-sugar binding sites annotated). SDR enzymes use a catalytic Tyr in the YxxxK tetrad as the proton acceptor/donor. Options A (position 2723) and D (position 347) exceed the 341-residue sequence length and are trivially impossible. Between B (position 283) and C (position 166), reading the sequence reveals position 166 is Tyrosine (Y)—the canonical SDR catalytic residue—while position 283 is Alanine (A), which cannot serve as a proton acceptor. A model with knowledge of SDR catalytic chemistry and the ability to count residues in the supplied sequence can eliminate all wrong options without database lookup.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The reasoning path relies on (1) recognizing the SDR fold and catalytic Tyr mechanism, (2) counting to identify residue identities at the candidate positions, and (3) noting that two options exceed sequence length. All information is derivable from the supplied sequence and general SDR biochemistry.",
    "reason": "The question provides the full 341-residue sequence and four options. Two options (A, D) are immediately eliminated as impossible positions. The remaining discrimination between B (Ala at 283) and C (Tyr at 166) is resolved by the well-established SDR catalytic mechanism in which a tyrosine serves as the proton acceptor. This is general enzyme-family knowledge, not a protein-specific lookup."
  },
  "case_id": "active_site_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C19",
      "C20",
      "H8",
      "H22",
      "H23",
      "C33"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8KN66 (WbpP, UDP-GlcNAc C4 epimerase, 341 aa) annotates position 166 as 'Active site: Proton acceptor' (evidence C5/H8). The evidence code is ECO:0000250 (inferred by similarity from P09147, galactose-4-epimerase), so the specific 'proton acceptor' label is a computational transfer. However, position 166 is independently confirmed by X-ray crystallography (PDB 1SB8/1SB9, PubMed 15016816) as a binding site for both NAD+ and UDP-GalNAc, and residue 166 in the supplied sequence is Tyrosine—consistent with the SDR-family catalytic tetrad Tyr that acts as proton acceptor/donor. The annotation is thus well-supported by structural and mechanistic evidence, though the precise mechanistic label is by homology transfer."
  },
  "important_caveats": [
    "The UniProt 'Proton acceptor' annotation at position 166 carries evidence code ECO:0000250 (similarity transfer from P09147), not direct experimental demonstration on WbpP itself. However, crystallographic data (1SB8/1SB9) confirm residue 166 contacts both NAD+ and the UDP-sugar substrate, strongly supporting its catalytic role.",
    "Distractors A and D are extremely easy to eliminate (positions exceed sequence length), reducing the effective discrimination to a two-way choice between B and C.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path described above relies solely on the supplied sequence and general SDR biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions (2723, 347) beyond the 341-residue sequence, making them physically impossible. Option B places a proton donor/acceptor at position 283, which is Alanine—incapable of proton transfer. Only option C (Tyr-166) is consistent with both the sequence content and SDR catalytic chemistry."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8KN66 (WbpP, UDP-GlcNAc C4 epimerase, 341 aa) annotates position 166 as 'Active site: Proton acceptor' (evidence C5/H8). The evidence code is ECO:0000250 (inferred by similarity from P09147, galactose-4-epimerase), so the specific 'proton acceptor' label is a computational transfer. However, position 166 is independently confirmed by X-ray crystallography (PDB 1SB8/1SB9, PubMed 15016816) as a binding site for both NAD+ and UDP-GalNAc, and residue 166 in the supplied sequence is Tyrosine—consistent with the SDR-family catalytic tetrad Tyr that acts as proton acceptor/donor. The annotation is thus well-supported by structural and mechanistic evidence, though the precise mechanistic label is by homology transfer.",
    "evidence_ids": ["C5", "C19", "C20", "H8", "H22", "H23", "C33"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is an SDR-family NAD-dependent epimerase (Rossmann-fold NAD-binding motif TGAVGF visible near residues 22–27; NAD+ and UDP-sugar binding sites annotated). SDR enzymes use a catalytic Tyr in the YxxxK tetrad as the proton acceptor/donor. Options A (position 2723) and D (position 347) exceed the 341-residue sequence length and are trivially impossible. Between B (position 283) and C (position 166), reading the sequence reveals position 166 is Tyrosine (Y)—the canonical SDR catalytic residue—while position 283 is Alanine (A), which cannot serve as a proton acceptor. A model with knowledge of SDR catalytic chemistry and the ability to count residues in the supplied sequence can eliminate all wrong options without database lookup.",
    "missing_item_specific_fact": "None critical. The reasoning path relies on (1) recognizing the SDR fold and catalytic Tyr mechanism, (2) counting to identify residue identities at the candidate positions, and (3) noting that two options exceed sequence length. All information is derivable from the supplied sequence and general SDR biochemistry.",
    "reason": "The question provides the full 341-residue sequence and four options. Two options (A, D) are immediately eliminated as impossible positions. The remaining discrimination between B (Ala at 283) and C (Tyr at 166) is resolved by the well-established SDR catalytic mechanism in which a tyrosine serves as the proton acceptor. This is general enzyme-family knowledge, not a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and D reference positions (2723, 347) beyond the 341-residue sequence, making them physically impossible. Option B places a proton donor/acceptor at position 283, which is Alanine—incapable of proton transfer. Only option C (Tyr-166) is consistent with both the sequence content and SDR catalytic chemistry."
  },
  "important_caveats": [
    "The UniProt 'Proton acceptor' annotation at position 166 carries evidence code ECO:0000250 (similarity transfer from P09147), not direct experimental demonstration on WbpP itself. However, crystallographic data (1SB8/1SB9) confirm residue 166 contacts both NAD+ and the UDP-sugar substrate, strongly supporting its catalytic role.",
    "Distractors A and D are extremely easy to eliminate (positions exceed sequence length), reducing the effective discrimination to a two-way choice between B and C.",
    "The reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model; the reasoning path described above relies solely on the supplied sequence and general SDR biochemistry."
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

**Accession:** `Q8KN66` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 87. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10747995","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"15752069","source":"PubMed"}],"value":"5.1.3.7"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"15752069","source":"PubMed"}],"value":"UDP-N-acetylglucosamine C4 epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"10747995","source":"PubMed"}],"value":"UDP-GlcNAc C4 epimerase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"5.1.3.45"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-GlcNAcA 4-epimerase"}]}}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000250","id":"P09147","source":"UniProtKB"}],"location":{"end":{"modifier":"EXACT","value":166},"start":{"modifier":"EXACT","value":166}},"type":"Active site"}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/features/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"1SB8","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"1SB9","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:57540"}],"ligand":{"id":"ChEBI:CHEBI:57540","name":"NAD(+)"},"location":{"end":{"modifier":"EXACT","value":166},"start":{"modifier":"EXACT","value":166}},"type":"Binding site"}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"description":"","evidences":[{"evidenceCode":"ECO:0000269","id":"15016816","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"1SB8","source":"PDB"}],"featureCrossReferences":[{"database":"ChEBI","id":"CHEBI:67138"}],"ligand":{"id":"ChEBI:CHEBI:67138","name":"UDP-N-acetyl-alpha-D-galactosamine"},"location":{"end":{"modifier":"EXACT","value":166},"start":{"modifier":"EXACT","value":166}},"type":"Binding site"}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence C33

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.367428+00:00.  

```json
{"citation":{"authors":["Ishiyama N.","Creuzenet C.","Lam J.S.","Berghuis A.M."],"citationCrossReferences":[{"database":"PubMed","id":"15016816"},{"database":"DOI","id":"10.1074/jbc.m401642200"}],"citationType":"journal article","firstPage":"22635","id":"15016816","journal":"J. Biol. Chem.","lastPage":"22642","publicationDate":"2004","title":"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-epimerases.","volume":"279"},"evidences":[{"evidenceCode":"ECO:0007744","id":"1SB8","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"1SB9","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"Serotype O6"}],"referenceNumber":6,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+); UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBUNIT","MUTAGENESIS OF ALA-209 AND SER-306"]}
```

Source SHA-256: `f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 168-170`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
FT   ACT_SITE        166
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000250|UniProtKB:P09147"
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 236-240`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
FT   BINDING         166
FT                   /ligand="NAD(+)"
FT                   /ligand_id="ChEBI:CHEBI:57540"
FT                   /evidence="ECO:0000269|PubMed:15016816,
FT                   ECO:0007744|PDB:1SB8, ECO:0007744|PDB:1SB9"
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)  
**Locator:** `lines 241-245`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:28:41.451179+00:00.  

```text
FT   BINDING         166
FT                   /ligand="UDP-N-acetyl-alpha-D-galactosamine"
FT                   /ligand_id="ChEBI:CHEBI:67138"
FT                   /evidence="ECO:0000269|PubMed:15016816,
FT                   ECO:0007744|PDB:1SB8"
```

Source SHA-256: `d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
