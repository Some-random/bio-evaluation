# cofactor_0045

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. Na(+)
B. heme
C. Mg(2+)
D. tungstopterin
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

> The exact sequence matches the UniProt entry for FrzK, a phosphoribosylpyrophosphate amidotransferase. That entry annotates one Mg(2+) ion per subunit, supporting choice C. The annotation is transferred by similarity from UniProtKB:P00497 rather than direct experimental evidence for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme family, but it does not by itself establish that this protein binds Mg(2+) or distinguish that specific cofactor from the distractors with confidence.


**Missing item-specific fact**

> The FrzK function and its Mg(2+) cofactor annotation, or equivalent protein-family biochemical knowledge, are not supplied in the question.


**Reason**

> The key is supported by a protein-specific annotation transferred from a homolog. Inferring the exact cofactor requires identifying the protein or family and supplying biochemical knowledge absent from the input; exact-sequence recognition alone would be lookup or memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the supplied annotation supports Mg(2+); the other annotated cofactor, a &#91;4Fe-4S&#93; cluster, is not offered.


### Important caveats

- The Mg(2+) annotation is evidence by similarity, not direct experimental evidence for this specific protein.
- The matched UniProt entry also annotates a &#91;4Fe-4S&#93; cluster per subunit, likewise by similarity, so the singular wording does not capture all annotated cofactors.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme family, but it does not by itself establish that this protein binds Mg(2+) or distinguish that specific cofactor from the distractors with confidence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The FrzK function and its Mg(2+) cofactor annotation, or equivalent protein-family biochemical knowledge, are not supplied in the question.",
    "reason": "The key is supported by a protein-specific annotation transferred from a homolog. Inferring the exact cofactor requires identifying the protein or family and supplying biochemical knowledge absent from the input; exact-sequence recognition alone would be lookup or memorization."
  },
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for FrzK, a phosphoribosylpyrophosphate amidotransferase. That entry annotates one Mg(2+) ion per subunit, supporting choice C. The annotation is transferred by similarity from UniProtKB:P00497 rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The Mg(2+) annotation is evidence by similarity, not direct experimental evidence for this specific protein.",
    "The matched UniProt entry also annotates a [4Fe-4S] cluster per subunit, likewise by similarity, so the singular wording does not capture all annotated cofactors."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied annotation supports Mg(2+); the other annotated cofactor, a [4Fe-4S] cluster, is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for FrzK, a phosphoribosylpyrophosphate amidotransferase. That entry annotates one Mg(2+) ion per subunit, supporting choice C. The annotation is transferred by similarity from UniProtKB:P00497 rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme family, but it does not by itself establish that this protein binds Mg(2+) or distinguish that specific cofactor from the distractors with confidence.",
    "missing_item_specific_fact": "The FrzK function and its Mg(2+) cofactor annotation, or equivalent protein-family biochemical knowledge, are not supplied in the question.",
    "reason": "The key is supported by a protein-specific annotation transferred from a homolog. Inferring the exact cofactor requires identifying the protein or family and supplying biochemical knowledge absent from the input; exact-sequence recognition alone would be lookup or memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the supplied annotation supports Mg(2+); the other annotated cofactor, a [4Fe-4S] cluster, is not offered."
  },
  "important_caveats": [
    "The Mg(2+) annotation is evidence by similarity, not direct experimental evidence for this specific protein.",
    "The matched UniProt entry also annotates a [4Fe-4S] cluster per subunit, likewise by similarity, so the singular wording does not capture all annotated cofactors."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8J1U7 (Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) annotates Mg(2+) as a cofactor (CHEBI:18420, 'Binds 1 Mg(2+) ion per subunit'). The EC number itself is supported by experimental evidence (ECO:0000269, PubMed:33372776). The Mg(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P00497, E. coli PurF), so it is a transferred annotation rather than direct experimental measurement on this protein. However, the requirement of Mg(2+) for PPAT catalysis is well-established textbook biochemistry. The entry also annotates a &#91;4Fe-4S&#93; cluster, but that option is not among the choices. Among the four provided options, Mg(2+) is the correct and supported answer.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 510-aa sequence contains features consistent with a glutamine amidotransferase (GAT) domain followed by a transferase domain (e.g., a 'CXG' region near residues ~190-200, and a C-terminal region with phosphate-binding-like motifs). GAT-domain transferases that act on phosphorylated substrates (PRPP, ATP, etc.) characteristically require Mg(2+) to coordinate the phosphate groups. Among the four choices, heme (B) is associated with oxidoreductases/cytochromes, tungstopterin (D) is specific to anaerobic aldehyde oxidoreductases, and Na(+) (A) is an extremely rare catalytic cofactor. A model recognizing the protein as a transferase with a GAT domain can reason that Mg(2+) is the expected cofactor and eliminate the other three options through general enzymology knowledge.


**Missing item-specific fact**

> Exact identification of this protein as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14) from an obscure fungal organism (Cladobotryum sp.) without database access would be non-trivial; the sequence lacks a single unmistakable signature motif that uniquely distinguishes it from other GAT-domain proteins. The Mg(2+) annotation is itself transferred by similarity (ECO:0000250) rather than directly measured for this protein.


**Reason**

> While precise protein identification benefits from database lookup, the question is answerable through general biological reasoning: recognizing GAT-domain/transferase features in the sequence, knowing that phosphorylated-substrate transferases require Mg(2+), and eliminating heme, tungstopterin, and Na(+) as implausible for this enzyme class. The distractors are sufficiently eliminable by broad enzymology knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although UniProt also annotates a &#91;4Fe-4S&#93; cluster as a cofactor, this option is absent from the choices. Among A (Na+), B (heme), C (Mg2+), and D (tungstopterin), only Mg(2+) is consistent with the enzyme's annotated cofactor and with general transferase biochemistry. No ambiguity among the provided options.


### Important caveats

- The Mg(2+) cofactor annotation is ECO:0000250 (similarity-based transfer from E. coli PurF P00497), not direct experimental evidence for FrzK itself.
- The protein also has a &#91;4Fe-4S&#93; cluster annotation (also similarity-based), which is not offered as a choice; this does not invalidate Mg(2+) as the correct answer among the given options.
- The EC 2.4.2.14 assignment is experimentally supported (ECO:0000269), but the cofactor assignment for this specific protein is computational.
- The protein is from Cladobotryum sp. (a mycoparasitic fungus) and is involved in FR901483 immunosuppressant biosynthesis, making it an unusual and obscure entry; identification from sequence alone without database access is challenging.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 510-aa sequence contains features consistent with a glutamine amidotransferase (GAT) domain followed by a transferase domain (e.g., a 'CXG' region near residues ~190-200, and a C-terminal region with phosphate-binding-like motifs). GAT-domain transferases that act on phosphorylated substrates (PRPP, ATP, etc.) characteristically require Mg(2+) to coordinate the phosphate groups. Among the four choices, heme (B) is associated with oxidoreductases/cytochromes, tungstopterin (D) is specific to anaerobic aldehyde oxidoreductases, and Na(+) (A) is an extremely rare catalytic cofactor. A model recognizing the protein as a transferase with a GAT domain can reason that Mg(2+) is the expected cofactor and eliminate the other three options through general enzymology knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact identification of this protein as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14) from an obscure fungal organism (Cladobotryum sp.) without database access would be non-trivial; the sequence lacks a single unmistakable signature motif that uniquely distinguishes it from other GAT-domain proteins. The Mg(2+) annotation is itself transferred by similarity (ECO:0000250) rather than directly measured for this protein.",
    "reason": "While precise protein identification benefits from database lookup, the question is answerable through general biological reasoning: recognizing GAT-domain/transferase features in the sequence, knowing that phosphorylated-substrate transferases require Mg(2+), and eliminating heme, tungstopterin, and Na(+) as implausible for this enzyme class. The distractors are sufficiently eliminable by broad enzymology knowledge."
  },
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8J1U7 (Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) annotates Mg(2+) as a cofactor (CHEBI:18420, 'Binds 1 Mg(2+) ion per subunit'). The EC number itself is supported by experimental evidence (ECO:0000269, PubMed:33372776). The Mg(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P00497, E. coli PurF), so it is a transferred annotation rather than direct experimental measurement on this protein. However, the requirement of Mg(2+) for PPAT catalysis is well-established textbook biochemistry. The entry also annotates a [4Fe-4S] cluster, but that option is not among the choices. Among the four provided options, Mg(2+) is the correct and supported answer."
  },
  "important_caveats": [
    "The Mg(2+) cofactor annotation is ECO:0000250 (similarity-based transfer from E. coli PurF P00497), not direct experimental evidence for FrzK itself.",
    "The protein also has a [4Fe-4S] cluster annotation (also similarity-based), which is not offered as a choice; this does not invalidate Mg(2+) as the correct answer among the given options.",
    "The EC 2.4.2.14 assignment is experimentally supported (ECO:0000269), but the cofactor assignment for this specific protein is computational.",
    "The protein is from Cladobotryum sp. (a mycoparasitic fungus) and is involved in FR901483 immunosuppressant biosynthesis, making it an unusual and obscure entry; identification from sequence alone without database access is challenging."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also annotates a [4Fe-4S] cluster as a cofactor, this option is absent from the choices. Among A (Na+), B (heme), C (Mg2+), and D (tungstopterin), only Mg(2+) is consistent with the enzyme's annotated cofactor and with general transferase biochemistry. No ambiguity among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0045",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8J1U7 (Phosphoribosylpyrophosphate amidotransferase FrzK, EC 2.4.2.14) annotates Mg(2+) as a cofactor (CHEBI:18420, 'Binds 1 Mg(2+) ion per subunit'). The EC number itself is supported by experimental evidence (ECO:0000269, PubMed:33372776). The Mg(2+) cofactor annotation carries evidence code ECO:0000250 (inferred by similarity to P00497, E. coli PurF), so it is a transferred annotation rather than direct experimental measurement on this protein. However, the requirement of Mg(2+) for PPAT catalysis is well-established textbook biochemistry. The entry also annotates a [4Fe-4S] cluster, but that option is not among the choices. Among the four provided options, Mg(2+) is the correct and supported answer.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 510-aa sequence contains features consistent with a glutamine amidotransferase (GAT) domain followed by a transferase domain (e.g., a 'CXG' region near residues ~190-200, and a C-terminal region with phosphate-binding-like motifs). GAT-domain transferases that act on phosphorylated substrates (PRPP, ATP, etc.) characteristically require Mg(2+) to coordinate the phosphate groups. Among the four choices, heme (B) is associated with oxidoreductases/cytochromes, tungstopterin (D) is specific to anaerobic aldehyde oxidoreductases, and Na(+) (A) is an extremely rare catalytic cofactor. A model recognizing the protein as a transferase with a GAT domain can reason that Mg(2+) is the expected cofactor and eliminate the other three options through general enzymology knowledge.",
    "missing_item_specific_fact": "Exact identification of this protein as phosphoribosylpyrophosphate amidotransferase FrzK (EC 2.4.2.14) from an obscure fungal organism (Cladobotryum sp.) without database access would be non-trivial; the sequence lacks a single unmistakable signature motif that uniquely distinguishes it from other GAT-domain proteins. The Mg(2+) annotation is itself transferred by similarity (ECO:0000250) rather than directly measured for this protein.",
    "reason": "While precise protein identification benefits from database lookup, the question is answerable through general biological reasoning: recognizing GAT-domain/transferase features in the sequence, knowing that phosphorylated-substrate transferases require Mg(2+), and eliminating heme, tungstopterin, and Na(+) as implausible for this enzyme class. The distractors are sufficiently eliminable by broad enzymology knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt also annotates a [4Fe-4S] cluster as a cofactor, this option is absent from the choices. Among A (Na+), B (heme), C (Mg2+), and D (tungstopterin), only Mg(2+) is consistent with the enzyme's annotated cofactor and with general transferase biochemistry. No ambiguity among the provided options."
  },
  "important_caveats": [
    "The Mg(2+) cofactor annotation is ECO:0000250 (similarity-based transfer from E. coli PurF P00497), not direct experimental evidence for FrzK itself.",
    "The protein also has a [4Fe-4S] cluster annotation (also similarity-based), which is not offered as a choice; this does not invalidate Mg(2+) as the correct answer among the given options.",
    "The EC 2.4.2.14 assignment is experimentally supported (ECO:0000269), but the cofactor assignment for this specific protein is computational.",
    "The protein is from Cladobotryum sp. (a mycoparasitic fungus) and is involved in FR901483 immunosuppressant biosynthesis, making it an unusual and obscure entry; identification from sequence alone without database access is challenging."
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

**Accession:** `A0A7T8J1U7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis clusters protein K"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Glutamine phosphoribosylpyrophosphate amidotransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"2.4.2.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Phosphoribosylpyrophosphate amidotransferase FrzK"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"ATase FrzK"}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:51.826168+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P00497","source":"UniProtKB"}],"name":"Mg(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P00497","source":"UniProtKB"}],"value":"Binds 1 Mg(2+) ion per subunit."}]}}
```

Source SHA-256: `56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
DE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};
DE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};
DE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};
DE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)  
**Locator:** `lines 44-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-02T04:25:55.036238+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:P00497};
CC       Note=Binds 1 Mg(2+) ion per subunit. {ECO:0000250|UniProtKB:P00497};
```

Source SHA-256: `578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 45. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
