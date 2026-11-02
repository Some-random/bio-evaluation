# cofactor_0038

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — &#91;4Fe-4S&#93; cluster

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSAELASRGRKVYFVGLNEYPFLPLVAGLLRTYAEQDERIAAAYDFQEPVFLVAPVQEMADGIVEPDVLALSCYVWNFRRQMKVAKLVKERYPNVLVVAGGPHVPDRPGNFFEKHPYVDVLAHGEGEVAFRELLATRLSDHPDYTAVPGVSVRRGTEAVVGPKAKRLPRLIDTPSPYLLGVMDGAVATCRERGLRFYALWETNRGCPYSCSFCDWGSATMSTLRKFEDERLQDEIEWFARHDVEDLFICDANFGIMPRDLEIAHALAEARGELGAPRQVRVNFAKNSNDRVFDISKTWHDADLLMGTTLSMQSTDMDVLEAIDRKNIGLDNYRKLQQRYAAENIHTYTELILGLPMETARSFRDGIGSLLEAGNHEDLRVYELGILPNAPLNTPEKIEQYGLRTVPKRMYVERPGTPDDEAETFEMVMETNAMPRDAWVESFSFIQAVQFLHNGCYTRYLSIFLRQEHGIGYTRFYEGLQDYFTGRPDTVLGALYLRMRSLYHDYIDMPALPLANLVASQPDMAADLAPYGRRRGWTIDNWGWLRIATDFDRFHTELREYLATLGLDPAGDARLEDVLRFQQDVMLRPDYSPELGKSAEYAHDWPGYFAGGLLRPRRVRVAYGDQSFGANGRYRPVPGDLKAFTMAAIGTSYPVSRMGHFCHRFESAEVTSLAEPVVSEQW

[Multiple Choices]
A. Na(+)
B. [4Fe-4S] cluster
C. Ca(2+)
D. FMN
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

> The exact sequence matches the annotated TokK protein. UniProt records a &#91;4Fe-4S&#93; cluster, supported by experimental evidence and a crystal structure containing the cluster, so choice B is supported. The protein also binds cob(II)alamin, which is not among the choices.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [C10](#evidence-c10), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a CxxxCxxC motif (in the segment CPYSCSFC), a characteristic iron-sulfur-cluster-binding motif in radical SAM enzymes. That provides a concrete basis for favoring &#91;4Fe-4S&#93; over Na+, Ca2+, or FMN.


**Missing item-specific fact**

> No item-specific fact is strictly needed to favor B among the listed choices, although confirming the protein's identity and experimentally established cofactors requires external annotation or literature.


**Reason**

> The sequence motif and the biological association of radical SAM enzymes with iron-sulfur clusters meaningfully distinguish B from these alternatives. The reviewer-only annotations confirm the key but are not needed as input to the reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, &#91;4Fe-4S&#93; is the supported answer. The protein has another cofactor, cob(II)alamin, but it is not offered as an option.


### Important caveats

- The evidence supports &#91;4Fe-4S&#93; as a cofactor, but the question's singular wording can obscure that TokK also binds cob(II)alamin.
- The sequence motif is a biological clue, not by itself experimental confirmation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in the segment CPYSCSFC), a characteristic iron-sulfur-cluster-binding motif in radical SAM enzymes. That provides a concrete basis for favoring [4Fe-4S] over Na+, Ca2+, or FMN.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific fact is strictly needed to favor B among the listed choices, although confirming the protein's identity and experimentally established cofactors requires external annotation or literature.",
    "reason": "The sequence motif and the biological association of radical SAM enzymes with iron-sulfur clusters meaningfully distinguish B from these alternatives. The reviewer-only annotations confirm the key but are not needed as input to the reasoning."
  },
  "case_id": "cofactor_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "C10",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated TokK protein. UniProt records a [4Fe-4S] cluster, supported by experimental evidence and a crystal structure containing the cluster, so choice B is supported. The protein also binds cob(II)alamin, which is not among the choices."
  },
  "important_caveats": [
    "The evidence supports [4Fe-4S] as a cofactor, but the question's singular wording can obscure that TokK also binds cob(II)alamin.",
    "The sequence motif is a biological clue, not by itself experimental confirmation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, [4Fe-4S] is the supported answer. The protein has another cofactor, cob(II)alamin, but it is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated TokK protein. UniProt records a [4Fe-4S] cluster, supported by experimental evidence and a crystal structure containing the cluster, so choice B is supported. The protein also binds cob(II)alamin, which is not among the choices.",
    "evidence_ids": ["C1", "C5", "C6", "C10", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC motif (in the segment CPYSCSFC), a characteristic iron-sulfur-cluster-binding motif in radical SAM enzymes. That provides a concrete basis for favoring [4Fe-4S] over Na+, Ca2+, or FMN.",
    "missing_item_specific_fact": "No item-specific fact is strictly needed to favor B among the listed choices, although confirming the protein's identity and experimentally established cofactors requires external annotation or literature.",
    "reason": "The sequence motif and the biological association of radical SAM enzymes with iron-sulfur clusters meaningfully distinguish B from these alternatives. The reviewer-only annotations confirm the key but are not needed as input to the reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, [4Fe-4S] is the supported answer. The protein has another cofactor, cob(II)alamin, but it is not offered as an option."
  },
  "important_caveats": [
    "The evidence supports [4Fe-4S] as a cofactor, but the question's singular wording can obscure that TokK also binds cob(II)alamin.",
    "The sequence motif is a biological clue, not by itself experimental confirmation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A6B9HEI0 (TokK, cobalamin-dependent radical SAM methyltransferase) lists &#91;4Fe-4S&#93; cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:35110734, X-ray crystallography PDB 7KDX/7KDY). The cluster is coordinated by 3 cysteines and an exchangeable SAM. None of the other three choices (Na+, Ca2+, FMN) appear as cofactors for this protein. Note: cob(II)alamin is also a cofactor of this enzyme but is not among the answer choices, so B is the uniquely correct option among A–D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8), [C10](#evidence-c10), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical radical SAM motif CxxxCxxC (residues around 'CPYSCSFCDW': C-P-Y-S-C-S-F-C, i.e., C(1)xxx(4)C(5)xx(7)C(8)). This three-cysteine cluster motif is the hallmark of radical SAM enzymes and is the ligand set for the &#91;4Fe-4S&#93; cluster. Recognizing this motif and knowing that radical SAM enzymes universally require a &#91;4Fe-4S&#93; cluster to cleave SAM into 5'-deoxyadenosyl radical is general, textbook biochemistry. The other options (Na+, Ca2+, FMN) have no association with the CxxxCxxC signature. A model that scans the sequence for this conserved motif can distinguish B from A, C, and D without knowing the protein's identity.


**Missing item-specific fact**

> None strictly required. The CxxxCxxC motif is present in the supplied sequence and its link to &#91;4Fe-4S&#93; clusters is general knowledge. Identifying the exact protein (TokK) or recalling its UniProt entry is not necessary.


**Reason**

> The discriminating feature—the CxxxCxxC radical SAM motif—is embedded in the supplied 681-aa sequence. Its association with &#91;4Fe-4S&#93; clusters is a well-established, general biochemical fact taught in standard biochemistry courses. A model can locate the motif and reason to the correct cofactor without protein-specific database lookup. The task is challenging (finding an 8-residue motif in a 681-residue sequence) but does not depend on memorizing this particular protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only &#91;4Fe-4S&#93; cluster is a confirmed cofactor of this protein. Na+, Ca2+, and FMN are not associated with radical SAM enzymes or with TokK. Although the enzyme also requires cob(II)alamin (B12), that cofactor is absent from the option set, so no ambiguity arises among A–D.


### Important caveats

- This enzyme is a B12-dependent radical SAM enzyme using BOTH a &#91;4Fe-4S&#93; cluster and cob(II)alamin. The question only offers &#91;4Fe-4S&#93; among the choices; cob(II)alamin is not listed, so the question is unambiguous within the given options.
- The CxxxCxxC motif identification in a 681-residue sequence is non-trivial for a model to perform reliably by scanning, though the motif itself and its meaning are general knowledge.
- The &#91;4Fe-4S&#93; cluster assignment is backed by X-ray crystallographic evidence (PDB 7KDX/7KDY, 1.79 Å), not merely computational prediction.
- The UniProt entry was first published 2025-02-05; the author's source snapshot date is unknown, but the sequence matches across all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM motif CxxxCxxC (residues around 'CPYSCSFCDW': C-P-Y-S-C-S-F-C, i.e., C(1)xxx(4)C(5)xx(7)C(8)). This three-cysteine cluster motif is the hallmark of radical SAM enzymes and is the ligand set for the [4Fe-4S] cluster. Recognizing this motif and knowing that radical SAM enzymes universally require a [4Fe-4S] cluster to cleave SAM into 5'-deoxyadenosyl radical is general, textbook biochemistry. The other options (Na+, Ca2+, FMN) have no association with the CxxxCxxC signature. A model that scans the sequence for this conserved motif can distinguish B from A, C, and D without knowing the protein's identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The CxxxCxxC motif is present in the supplied sequence and its link to [4Fe-4S] clusters is general knowledge. Identifying the exact protein (TokK) or recalling its UniProt entry is not necessary.",
    "reason": "The discriminating feature—the CxxxCxxC radical SAM motif—is embedded in the supplied 681-aa sequence. Its association with [4Fe-4S] clusters is a well-established, general biochemical fact taught in standard biochemistry courses. A model can locate the motif and reason to the correct cofactor without protein-specific database lookup. The task is challenging (finding an 8-residue motif in a 681-residue sequence) but does not depend on memorizing this particular protein's annotation."
  },
  "case_id": "cofactor_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H7",
      "H8",
      "C10",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A6B9HEI0 (TokK, cobalamin-dependent radical SAM methyltransferase) lists [4Fe-4S] cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:35110734, X-ray crystallography PDB 7KDX/7KDY). The cluster is coordinated by 3 cysteines and an exchangeable SAM. None of the other three choices (Na+, Ca2+, FMN) appear as cofactors for this protein. Note: cob(II)alamin is also a cofactor of this enzyme but is not among the answer choices, so B is the uniquely correct option among A–D."
  },
  "important_caveats": [
    "This enzyme is a B12-dependent radical SAM enzyme using BOTH a [4Fe-4S] cluster and cob(II)alamin. The question only offers [4Fe-4S] among the choices; cob(II)alamin is not listed, so the question is unambiguous within the given options.",
    "The CxxxCxxC motif identification in a 681-residue sequence is non-trivial for a model to perform reliably by scanning, though the motif itself and its meaning are general knowledge.",
    "The [4Fe-4S] cluster assignment is backed by X-ray crystallographic evidence (PDB 7KDX/7KDY, 1.79 Å), not merely computational prediction.",
    "The UniProt entry was first published 2025-02-05; the author's source snapshot date is unknown, but the sequence matches across all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only [4Fe-4S] cluster is a confirmed cofactor of this protein. Na+, Ca2+, and FMN are not associated with radical SAM enzymes or with TokK. Although the enzyme also requires cob(II)alamin (B12), that cofactor is absent from the option set, so no ambiguity arises among A–D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A6B9HEI0 (TokK, cobalamin-dependent radical SAM methyltransferase) lists [4Fe-4S] cluster as a cofactor with experimental evidence (ECO:0000269, PubMed:35110734, X-ray crystallography PDB 7KDX/7KDY). The cluster is coordinated by 3 cysteines and an exchangeable SAM. None of the other three choices (Na+, Ca2+, FMN) appear as cofactors for this protein. Note: cob(II)alamin is also a cofactor of this enzyme but is not among the answer choices, so B is the uniquely correct option among A–D.",
    "evidence_ids": ["C5", "C6", "H7", "H8", "C10", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical radical SAM motif CxxxCxxC (residues around 'CPYSCSFCDW': C-P-Y-S-C-S-F-C, i.e., C(1)xxx(4)C(5)xx(7)C(8)). This three-cysteine cluster motif is the hallmark of radical SAM enzymes and is the ligand set for the [4Fe-4S] cluster. Recognizing this motif and knowing that radical SAM enzymes universally require a [4Fe-4S] cluster to cleave SAM into 5'-deoxyadenosyl radical is general, textbook biochemistry. The other options (Na+, Ca2+, FMN) have no association with the CxxxCxxC signature. A model that scans the sequence for this conserved motif can distinguish B from A, C, and D without knowing the protein's identity.",
    "missing_item_specific_fact": "None strictly required. The CxxxCxxC motif is present in the supplied sequence and its link to [4Fe-4S] clusters is general knowledge. Identifying the exact protein (TokK) or recalling its UniProt entry is not necessary.",
    "reason": "The discriminating feature—the CxxxCxxC radical SAM motif—is embedded in the supplied 681-aa sequence. Its association with [4Fe-4S] clusters is a well-established, general biochemical fact taught in standard biochemistry courses. A model can locate the motif and reason to the correct cofactor without protein-specific database lookup. The task is challenging (finding an 8-residue motif in a 681-residue sequence) but does not depend on memorizing this particular protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only [4Fe-4S] cluster is a confirmed cofactor of this protein. Na+, Ca2+, and FMN are not associated with radical SAM enzymes or with TokK. Although the enzyme also requires cob(II)alamin (B12), that cofactor is absent from the option set, so no ambiguity arises among A–D."
  },
  "important_caveats": [
    "This enzyme is a B12-dependent radical SAM enzyme using BOTH a [4Fe-4S] cluster and cob(II)alamin. The question only offers [4Fe-4S] among the choices; cob(II)alamin is not listed, so the question is unambiguous within the given options.",
    "The CxxxCxxC motif identification in a 681-residue sequence is non-trivial for a model to perform reliably by scanning, though the motif itself and its meaning are general knowledge.",
    "The [4Fe-4S] cluster assignment is backed by X-ray crystallographic evidence (PDB 7KDX/7KDY, 1.79 Å), not merely computational prediction.",
    "The UniProt entry was first published 2025-02-05; the author's source snapshot date is unknown, but the sequence matches across all checked versions."
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

**Accession:** `A0A6B9HEI0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6B9HEI0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.139042+00:00.  

```json
"A0A6B9HEI0"
```

Source SHA-256: `07f6f6875eb6b670742397f945aef55e5d385a36991e5466fdf5dae9f6257913`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6B9HEI0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.139042+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:49883"},"evidences":[{"evidenceCode":"ECO:0000269","id":"35110734","source":"PubMed"}],"name":"[4Fe-4S] cluster"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35110734","source":"PubMed"}],"value":"Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine."}]}}
```

Source SHA-256: `07f6f6875eb6b670742397f945aef55e5d385a36991e5466fdf5dae9f6257913`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6B9HEI0.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.139042+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:16304"},"evidences":[{"evidenceCode":"ECO:0000269","id":"35110734","source":"PubMed"}],"name":"cob(II)alamin"}],"commentType":"COFACTOR"}
```

Source SHA-256: `07f6f6875eb6b670742397f945aef55e5d385a36991e5466fdf5dae9f6257913`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A6B9HEI0.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:32.139042+00:00.  

```json
{"citation":{"authors":["Knox H.L.","Sinner E.K.","Townsend C.A.","Boal A.K.","Booker S.J."],"citationCrossReferences":[{"database":"PubMed","id":"35110734"},{"database":"DOI","id":"10.1038/s41586-021-04392-4"}],"citationType":"journal article","firstPage":"343","id":"35110734","journal":"Nature","lastPage":"348","publicationDate":"2022","title":"Structure of a B12-dependent radical SAM enzyme in carbapenem biosynthesis.","volume":"602"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7KDX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7KDY","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER; COB(II)ALAMIN; CARBAPENAM SUBSTRATE AND 5'-DEOXYADENOSINE","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","DOMAIN","MUTAGENESIS OF 19-GLU-TYR-20; TRP-76; TRP-215; ARG-280 AND LEU-383"]}
```

Source SHA-256: `07f6f6875eb6b670742397f945aef55e5d385a36991e5466fdf5dae9f6257913`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6B9HEI0?format=txt&versions=18)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:34.178407+00:00.  

```text
RN   [4] {ECO:0007744|PDB:7KDX, ECO:0007744|PDB:7KDY}
RP   X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) IN COMPLEXES WITH [4FE-4S] CLUSTER;
RP   COB(II)ALAMIN; CARBAPENAM SUBSTRATE AND 5'-DEOXYADENOSINE, FUNCTION,
RP   CATALYTIC ACTIVITY, COFACTOR, DOMAIN, AND MUTAGENESIS OF 19-GLU-TYR-20;
RP   TRP-76; TRP-215; ARG-280 AND LEU-383.
RX   PubMed=35110734; DOI=10.1038/s41586-021-04392-4;
RA   Knox H.L., Sinner E.K., Townsend C.A., Boal A.K., Booker S.J.;
RT   "Structure of a B12-dependent radical SAM enzyme in carbapenem
RT   biosynthesis.";
RL   Nature 602:343-348(2022).
```

Source SHA-256: `140f29cd7d5501b98fe670a4e8aadd5214465a83c126dce996028e3e47afe85c`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6B9HEI0?format=txt&versions=18)  
**Locator:** `lines 54-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:34.178407+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883;
CC         Evidence={ECO:0000269|PubMed:35110734};
CC       Note=Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3
CC       cysteines and an exchangeable S-adenosyl-L-methionine.
CC       {ECO:0000269|PubMed:35110734};
```

Source SHA-256: `140f29cd7d5501b98fe670a4e8aadd5214465a83c126dce996028e3e47afe85c`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A6B9HEI0?format=txt&versions=18)  
**Locator:** `lines 60-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:34.178407+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=cob(II)alamin; Xref=ChEBI:CHEBI:16304;
CC         Evidence={ECO:0000269|PubMed:35110734};
```

Source SHA-256: `140f29cd7d5501b98fe670a4e8aadd5214465a83c126dce996028e3e47afe85c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
