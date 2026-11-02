# cofactor_0072

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATKRKVIITCAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDPDDGHPTQDPAVFQEFLPRIKAECDAVINLTTGGSPHMTVAERLKPAHHFQPEVASLNMGSMNFGLYPMLERFKELKYDWERKHLENSRDLVFKNTFADIEYILTSCGANGTRFEFECYDISHLYNLAHFVDRGLAKPPFFVQSVFGLLGGIGAHPEDLAHMRRTADRLFGKDYVWSILGAGRNQIPLASIGVAQGSNARVGLEDSLWIEPGKLAESSAAQVRKIRQVIEGLSLDIATPAEAREMLQLKGAANTNF

[Multiple Choices]
A. [4Fe-4S] cluster
B. Zn(2+)
C. pyridoxal 5'-phosphate
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

> The exact sequence matches a UniProt entry annotated with Zn(2+) as a cofactor. However, the annotation is transferred by similarity from another UniProt entry (ECO:0000250), not shown here as a direct experimental determination for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains potential metal-binding residues, but that observation does not establish zinc dependence or distinguish Zn(2+) from the other listed cofactors.


**Missing item-specific fact**

> The protein-specific cofactor annotation, transferred from a homolog, is not supplied in the question.


**Reason**

> The sequence and choices provide no reliable general biological argument that identifies Zn(2+) specifically; selecting it depends on an absent protein-specific annotation or equivalent evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports Zn(2+) as the annotated cofactor, although it does not establish direct experimental confirmation for this exact protein.


### Important caveats

- The matched UniProt annotation is evidence for the expected answer, but its evidence code indicates transfer by similarity rather than direct experimental support for the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains potential metal-binding residues, but that observation does not establish zinc dependence or distinguish Zn(2+) from the other listed cofactors.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation, transferred from a homolog, is not supplied in the question.",
    "reason": "The sequence and choices provide no reliable general biological argument that identifies Zn(2+) specifically; selecting it depends on an absent protein-specific annotation or equivalent evidence."
  },
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as a cofactor. However, the annotation is transferred by similarity from another UniProt entry (ECO:0000250), not shown here as a direct experimental determination for this protein."
  },
  "important_caveats": [
    "The matched UniProt annotation is evidence for the expected answer, but its evidence code indicates transfer by similarity rather than direct experimental support for the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports Zn(2+) as the annotated cofactor, although it does not establish direct experimental confirmation for this exact protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Zn(2+) as a cofactor. However, the annotation is transferred by similarity from another UniProt entry (ECO:0000250), not shown here as a direct experimental determination for this protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains potential metal-binding residues, but that observation does not establish zinc dependence or distinguish Zn(2+) from the other listed cofactors.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation, transferred from a homolog, is not supplied in the question.",
    "reason": "The sequence and choices provide no reliable general biological argument that identifies Zn(2+) specifically; selecting it depends on an absent protein-specific annotation or equivalent evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports Zn(2+) as the annotated cofactor, although it does not establish direct experimental confirmation for this exact protein."
  },
  "important_caveats": [
    "The matched UniProt annotation is evidence for the expected answer, but its evidence code indicates transfer by similarity rather than direct experimental support for the supplied sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for B1G5Y9 (3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319) annotates Zn(2+) as the cofactor (C5/H4). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so it is a transferred computational annotation rather than direct experimental proof for this specific protein. However, the enzyme belongs to the thiolase superfamily (EC 2.3.1.x), whose Zn(2+) dependence is well-established textbook biochemistry. The sequence contains canonical thiolase-superfamily motifs (e.g., 'GGSPHMT', 'GGIGAHP', active-site cysteines in 'CGANGTRFEFECY'), consistent with Zn(2+) coordination. The answer is supported by both the database annotation and general biochemical knowledge of the enzyme class.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays recognizable thiolase-superfamily hallmarks: the N-terminal 'CAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDP' block, the 'GGSPHMT' motif (~residue 100), and the 'GGIGAHP' motif (~residue 215), together with catalytic cysteines in 'CGANGTRFEFECY'. Thiolase-superfamily enzymes (3-ketoacyl-CoA thiolases, 3-ketoacyl-ACP synthases, and related transferases) are well known to require Zn(2+) for catalysis. This allows elimination of PLP (aminotransferase/decarboxylase cofactor), FMN (oxidoreductase cofactor), and &#91;4Fe-4S&#93; clusters (radical SAM / ferredoxin cofactors), none of whose characteristic binding motifs (e.g., CxxCxxC for Fe-S, KxxxK for PLP, NxGxxG for FMN) are present.


**Missing item-specific fact**

> None critical. Recognizing the thiolase superfamily from sequence motifs and knowing its Zn(2+) requirement constitutes general biochemical knowledge, not an item-specific lookup. The exact EC number 2.3.1.319 is obscure, but the broader thiolase-superfamily Zn(2+) dependence is standard.


**Reason**

> A knowledgeable reader can identify thiolase-superfamily motifs in the sequence, recall that this enzyme class uses Zn(2+), and exclude the other three cofactors on the basis of incompatible enzyme classes and absent binding motifs. The reasoning chain is concrete and does not require memorizing the UniProt entry for this particular accession.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices correspond to distinct enzyme classes (Fe-S radical enzymes, metallo-hydrolases/thiolases, PLP-dependent enzymes, flavoproteins). The sequence's thiolase motifs and absence of Fe-S/PLP/FMN binding signatures leave Zn(2+) as the only defensible option.


### Important caveats

- The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity-based transfer from B0VHH0), not direct experimental verification for B1G5Y9 itself. The support rests on the well-established thiolase-superfamily Zn(2+) requirement.
- The specific EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase) is a relatively recently characterized and obscure enzyme; a solver unfamiliar with the thiolase superfamily might struggle to identify the motifs, though the motifs themselves are present in the sequence.
- All reviewer evidence is from UniProt current/historical snapshots; the author's actual source snapshot is unknown. Sequence match is confirmed (SHA-256 identical).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays recognizable thiolase-superfamily hallmarks: the N-terminal 'CAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDP' block, the 'GGSPHMT' motif (~residue 100), and the 'GGIGAHP' motif (~residue 215), together with catalytic cysteines in 'CGANGTRFEFECY'. Thiolase-superfamily enzymes (3-ketoacyl-CoA thiolases, 3-ketoacyl-ACP synthases, and related transferases) are well known to require Zn(2+) for catalysis. This allows elimination of PLP (aminotransferase/decarboxylase cofactor), FMN (oxidoreductase cofactor), and [4Fe-4S] clusters (radical SAM / ferredoxin cofactors), none of whose characteristic binding motifs (e.g., CxxCxxC for Fe-S, KxxxK for PLP, NxGxxG for FMN) are present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing the thiolase superfamily from sequence motifs and knowing its Zn(2+) requirement constitutes general biochemical knowledge, not an item-specific lookup. The exact EC number 2.3.1.319 is obscure, but the broader thiolase-superfamily Zn(2+) dependence is standard.",
    "reason": "A knowledgeable reader can identify thiolase-superfamily motifs in the sequence, recall that this enzyme class uses Zn(2+), and exclude the other three cofactors on the basis of incompatible enzyme classes and absent binding motifs. The reasoning chain is concrete and does not require memorizing the UniProt entry for this particular accession."
  },
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for B1G5Y9 (3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319) annotates Zn(2+) as the cofactor (C5/H4). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so it is a transferred computational annotation rather than direct experimental proof for this specific protein. However, the enzyme belongs to the thiolase superfamily (EC 2.3.1.x), whose Zn(2+) dependence is well-established textbook biochemistry. The sequence contains canonical thiolase-superfamily motifs (e.g., 'GGSPHMT', 'GGIGAHP', active-site cysteines in 'CGANGTRFEFECY'), consistent with Zn(2+) coordination. The answer is supported by both the database annotation and general biochemical knowledge of the enzyme class."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity-based transfer from B0VHH0), not direct experimental verification for B1G5Y9 itself. The support rests on the well-established thiolase-superfamily Zn(2+) requirement.",
    "The specific EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase) is a relatively recently characterized and obscure enzyme; a solver unfamiliar with the thiolase superfamily might struggle to identify the motifs, though the motifs themselves are present in the sequence.",
    "All reviewer evidence is from UniProt current/historical snapshots; the author's actual source snapshot is unknown. Sequence match is confirmed (SHA-256 identical)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices correspond to distinct enzyme classes (Fe-S radical enzymes, metallo-hydrolases/thiolases, PLP-dependent enzymes, flavoproteins). The sequence's thiolase motifs and absence of Fe-S/PLP/FMN binding signatures leave Zn(2+) as the only defensible option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0072",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for B1G5Y9 (3,5-dioxohexanoate:acetyl-CoA acetone transferase, EC 2.3.1.319) annotates Zn(2+) as the cofactor (C5/H4). The evidence code is ECO:0000250 (inferred by similarity from B0VHH0), so it is a transferred computational annotation rather than direct experimental proof for this specific protein. However, the enzyme belongs to the thiolase superfamily (EC 2.3.1.x), whose Zn(2+) dependence is well-established textbook biochemistry. The sequence contains canonical thiolase-superfamily motifs (e.g., 'GGSPHMT', 'GGIGAHP', active-site cysteines in 'CGANGTRFEFECY'), consistent with Zn(2+) coordination. The answer is supported by both the database annotation and general biochemical knowledge of the enzyme class.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays recognizable thiolase-superfamily hallmarks: the N-terminal 'CAPTGAIHTPSMSPYLPVTPQQIGDAALAAAKEGAAIIHLHARDP' block, the 'GGSPHMT' motif (~residue 100), and the 'GGIGAHP' motif (~residue 215), together with catalytic cysteines in 'CGANGTRFEFECY'. Thiolase-superfamily enzymes (3-ketoacyl-CoA thiolases, 3-ketoacyl-ACP synthases, and related transferases) are well known to require Zn(2+) for catalysis. This allows elimination of PLP (aminotransferase/decarboxylase cofactor), FMN (oxidoreductase cofactor), and [4Fe-4S] clusters (radical SAM / ferredoxin cofactors), none of whose characteristic binding motifs (e.g., CxxCxxC for Fe-S, KxxxK for PLP, NxGxxG for FMN) are present.",
    "missing_item_specific_fact": "None critical. Recognizing the thiolase superfamily from sequence motifs and knowing its Zn(2+) requirement constitutes general biochemical knowledge, not an item-specific lookup. The exact EC number 2.3.1.319 is obscure, but the broader thiolase-superfamily Zn(2+) dependence is standard.",
    "reason": "A knowledgeable reader can identify thiolase-superfamily motifs in the sequence, recall that this enzyme class uses Zn(2+), and exclude the other three cofactors on the basis of incompatible enzyme classes and absent binding motifs. The reasoning chain is concrete and does not require memorizing the UniProt entry for this particular accession."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices correspond to distinct enzyme classes (Fe-S radical enzymes, metallo-hydrolases/thiolases, PLP-dependent enzymes, flavoproteins). The sequence's thiolase motifs and absence of Fe-S/PLP/FMN binding signatures leave Zn(2+) as the only defensible option."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity-based transfer from B0VHH0), not direct experimental verification for B1G5Y9 itself. The support rests on the well-established thiolase-superfamily Zn(2+) requirement.",
    "The specific EC 2.3.1.319 (3,5-dioxohexanoate:acetyl-CoA acetone transferase) is a relatively recently characterized and obscure enzyme; a solver unfamiliar with the thiolase superfamily might struggle to identify the motifs, though the motifs themselves are present in the sequence.",
    "All reviewer evidence is from UniProt current/historical snapshots; the author's actual source snapshot is unknown. Sequence match is confirmed (SHA-256 identical)."
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

**Accession:** `B1G5Y9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 43. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
"B1G5Y9"
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3,5-dioxohexanoate cleavage enzyme"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24240508","source":"PubMed"}],"value":"BKACE_274"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24240508","source":"PubMed"}],"value":"2.3.1.319"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"3,5-dioxohexanoate:acetyl-CoA acetone transferase"}}}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"B0VHH0","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B1G5Y9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:00.301562+00:00.  

```json
{"citation":{"authors":["Bastard K.","Smith A.A.","Vergne-Vaxelaire C.","Perret A.","Zaparucha A.","De Melo-Minardi R.","Mariage A.","Boutard M.","Debard A.","Lechaplais C.","Pelle C.","Pellouin V.","Perchat N.","Petit J.L.","Kreimeyer A.","Medigue C.","Weissenbach J.","Artiguenave F.","De Berardinis V.","Vallenet D.","Salanoubat M."],"citationCrossReferences":[{"database":"PubMed","id":"24240508"},{"database":"DOI","id":"10.1038/nchembio.1387"}],"citationType":"journal article","firstPage":"42","id":"24240508","journal":"Nat. Chem. Biol.","lastPage":"49","publicationDate":"2014","title":"Revealing the hidden functional diversity of an enzyme family.","volume":"10"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `2f758acaffa7f035f51c7b9c1246eab2f4b6b5dd0f1a47ea47461062bd10b2fb`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
DE   RecName: Full=3,5-dioxohexanoate:acetyl-CoA acetone transferase {ECO:0000305};
DE            EC=2.3.1.319 {ECO:0000269|PubMed:24240508};
DE   AltName: Full=3,5-dioxohexanoate cleavage enzyme {ECO:0000305};
DE   AltName: Full=BKACE_274 {ECO:0000303|PubMed:24240508};
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B1G5Y9?format=txt&versions=43)  
**Locator:** `lines 52-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-01T06:27:50.999580+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:B0VHH0};
```

Source SHA-256: `d90dafbf43111239cd98ed128138c3a4aaac27f177ca000100c8186666b4ab94`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 72. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
