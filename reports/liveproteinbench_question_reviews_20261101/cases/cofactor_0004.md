# cofactor_0004

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDMNTFPANTYCDSIVRFLDAIEYHDDNLTHDERVEGLRHVHSRTAQYFTEPLPRKVLKDVAPRRIAAVTRTISHFIVYCWSKLPREAQVDVSIYLSIINVLDDEISSEPSTQMATFWTDLVQGKQQKHPFWVLFNSHLPRLLRHYDSFCSFNIMRCTFDYFEGCWIEQHNFQGYPGADCYPLFLRRLNCLGGAVAGTIFPAAKFDEQKLFAEISCVMAQIDGPVALVNDLFSFYKEYDQDEANLVTNWCTVDGITMDQALTRLTDDTIHACVRILEILKDKDPDMLATIRGFIHGYVTWHICDFRYRLREIYDREDLGGSSAKFRDYFDTAINVGWVDVEEWTCQVQGFEVDGPVPKGSEIQAYRTNAFGFSVDTRRPHNMDYVGSSIISMFEWVTGYLKGKSR

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Mg(2+)
C. heme
D. Fe(2+)
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

> The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The supplied sequence alone does not provide a sufficiently specific, clear basis for distinguishing Mg(2+) from the other options.


**Missing item-specific fact**

> The protein is annotated as terpene cyclase pbrA and has an Mg(2+) cofactor annotation transferred by similarity; neither fact is provided in the question.


**Reason**

> The supporting cofactor annotation is protein-specific external information. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched database annotation supports Mg(2+); the evidence provided does not support another listed option.


### Important caveats

- The historical and current database records match the supplied sequence.
- The cited cofactor annotation is similarity-based, not a direct experimental demonstration for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence alone does not provide a sufficiently specific, clear basis for distinguishing Mg(2+) from the other options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein is annotated as terpene cyclase pbrA and has an Mg(2+) cofactor annotation transferred by similarity; neither fact is provided in the question.",
    "reason": "The supporting cofactor annotation is protein-specific external information. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "cofactor_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The historical and current database records match the supplied sequence.",
    "The cited cofactor annotation is similarity-based, not a direct experimental demonstration for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports Mg(2+); the evidence provided does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with Mg(2+) as a cofactor. The annotation is transferred by similarity (ECO:0000250), so it supports the key as a database annotation but is not direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The supplied sequence alone does not provide a sufficiently specific, clear basis for distinguishing Mg(2+) from the other options.",
    "missing_item_specific_fact": "The protein is annotated as terpene cyclase pbrA and has an Mg(2+) cofactor annotation transferred by similarity; neither fact is provided in the question.",
    "reason": "The supporting cofactor annotation is protein-specific external information. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation supports Mg(2+); the evidence provided does not support another listed option."
  },
  "important_caveats": [
    "The historical and current database records match the supplied sequence.",
    "The cited cofactor annotation is similarity-based, not a direct experimental demonstration for this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates this protein (A0A0F7TWX5, terpene cyclase pbrA, EC 4.2.3.-) with Mg(2+) as its cofactor (ChEBI:18420). The annotation evidence is ECO:0000250 (similarity to P13513), i.e., computational transfer rather than direct experimental measurement on this specific protein. However, the biochemistry of terpene cyclases (EC 4.2.3.-) universally involves a divalent metal ion (Mg2+ or Mn2+) coordinating the diphosphate substrate and facilitating ionization of the leaving group. The EC assignment 4.2.3.- is supported by the 2024 Zhou et al. paper (PubMed:39511739). Thus Mg(2+) is well-supported as the cofactor for a terpene cyclase, even though the specific annotation here is by similarity.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If the model could positively identify the sequence as a terpene cyclase, then Mg(2+) is the well-established cofactor for the diphosphate-ionization mechanism. Partial elimination reasoning is possible: no pantetheine-binding ACP domain (rules out A), no obvious heme-ligand His/Cys geometry (weakly rules out C), and no canonical 2-His-1-carboxylate facial triad (weakly rules out D). However, the positive identification step—recognizing a 405-aa sequence as a terpene cyclase—is the critical bottleneck, and the canonical DDxxD aspartate-rich metal-binding motif is NOT present in recognizable form (the closest matches are DDEIS and DDTIH, neither of which is DDxxD). Without this motif or a database match, the sequence provides no strong positive signal for terpene cyclase identity.


**Missing item-specific fact**

> The specific identification of this 405-aa sequence as terpene cyclase pbrA (or any terpene cyclase) cannot be reliably made from the raw sequence alone. The canonical DDxxD motif is absent or highly degenerate. Identification requires BLAST/database lookup or memorization of this particular entry. The 2024 characterization paper (PubMed:39511739) established the terpene cyclase function, but this is not inferable from sequence features visible in the input.


**Reason**

> The reasoning chain requires: (1) identify protein as terpene cyclase → (2) know terpene cyclases use Mg2+. Step 2 is general biological knowledge, but step 1 is essentially a lookup problem. The absence of the canonical DDxxD motif and the lack of other unmistakable terpene-cyclase-specific sequence features mean a model cannot reliably reach step 2 from the sequence alone. The elimination of distractors A and C is somewhat plausible by absence of their signature motifs, but elimination of D (Fe2+) is weak since Fe2+ and Mg2+ are both common divalent cation cofactors. The question effectively requires recognizing this specific protein's identity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given correct identification as a terpene cyclase, Mg(2+) is the clear and unambiguous answer. The distractors (pantetheine 4'-phosphate, heme, Fe2+) correspond to mechanistically distinct enzyme classes and are not plausible alternatives for a terpene cyclase. No ambiguity in the correct answer once the protein identity is established.


### Important caveats

- The UniProt cofactor annotation is by similarity (ECO:0000250, transferred from P13513), not direct experimental evidence on pbrA itself. However, the general biochemistry of terpene cyclases strongly supports Mg2+.
- The canonical DDxxD aspartate-rich motif is not clearly present in this sequence, making sequence-based identification of the terpene cyclase fold difficult without database access.
- The protein was first functionally characterized in 2024 (PubMed:39511739), so this is a relatively recent annotation.
- The reviewer-only evidence was not available to the evaluated model; the model must work from the raw sequence and choices alone.
- The EC number is 4.2.3.- (incomplete), meaning the specific terpene cyclase subclass is not fully resolved in the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If the model could positively identify the sequence as a terpene cyclase, then Mg(2+) is the well-established cofactor for the diphosphate-ionization mechanism. Partial elimination reasoning is possible: no pantetheine-binding ACP domain (rules out A), no obvious heme-ligand His/Cys geometry (weakly rules out C), and no canonical 2-His-1-carboxylate facial triad (weakly rules out D). However, the positive identification step—recognizing a 405-aa sequence as a terpene cyclase—is the critical bottleneck, and the canonical DDxxD aspartate-rich metal-binding motif is NOT present in recognizable form (the closest matches are DDEIS and DDTIH, neither of which is DDxxD). Without this motif or a database match, the sequence provides no strong positive signal for terpene cyclase identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this 405-aa sequence as terpene cyclase pbrA (or any terpene cyclase) cannot be reliably made from the raw sequence alone. The canonical DDxxD motif is absent or highly degenerate. Identification requires BLAST/database lookup or memorization of this particular entry. The 2024 characterization paper (PubMed:39511739) established the terpene cyclase function, but this is not inferable from sequence features visible in the input.",
    "reason": "The reasoning chain requires: (1) identify protein as terpene cyclase → (2) know terpene cyclases use Mg2+. Step 2 is general biological knowledge, but step 1 is essentially a lookup problem. The absence of the canonical DDxxD motif and the lack of other unmistakable terpene-cyclase-specific sequence features mean a model cannot reliably reach step 2 from the sequence alone. The elimination of distractors A and C is somewhat plausible by absence of their signature motifs, but elimination of D (Fe2+) is weak since Fe2+ and Mg2+ are both common divalent cation cofactors. The question effectively requires recognizing this specific protein's identity."
  },
  "case_id": "cofactor_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates this protein (A0A0F7TWX5, terpene cyclase pbrA, EC 4.2.3.-) with Mg(2+) as its cofactor (ChEBI:18420). The annotation evidence is ECO:0000250 (similarity to P13513), i.e., computational transfer rather than direct experimental measurement on this specific protein. However, the biochemistry of terpene cyclases (EC 4.2.3.-) universally involves a divalent metal ion (Mg2+ or Mn2+) coordinating the diphosphate substrate and facilitating ionization of the leaving group. The EC assignment 4.2.3.- is supported by the 2024 Zhou et al. paper (PubMed:39511739). Thus Mg(2+) is well-supported as the cofactor for a terpene cyclase, even though the specific annotation here is by similarity."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250, transferred from P13513), not direct experimental evidence on pbrA itself. However, the general biochemistry of terpene cyclases strongly supports Mg2+.",
    "The canonical DDxxD aspartate-rich motif is not clearly present in this sequence, making sequence-based identification of the terpene cyclase fold difficult without database access.",
    "The protein was first functionally characterized in 2024 (PubMed:39511739), so this is a relatively recent annotation.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work from the raw sequence and choices alone.",
    "The EC number is 4.2.3.- (incomplete), meaning the specific terpene cyclase subclass is not fully resolved in the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given correct identification as a terpene cyclase, Mg(2+) is the clear and unambiguous answer. The distractors (pantetheine 4'-phosphate, heme, Fe2+) correspond to mechanistically distinct enzyme classes and are not plausible alternatives for a terpene cyclase. No ambiguity in the correct answer once the protein identity is established."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates this protein (A0A0F7TWX5, terpene cyclase pbrA, EC 4.2.3.-) with Mg(2+) as its cofactor (ChEBI:18420). The annotation evidence is ECO:0000250 (similarity to P13513), i.e., computational transfer rather than direct experimental measurement on this specific protein. However, the biochemistry of terpene cyclases (EC 4.2.3.-) universally involves a divalent metal ion (Mg2+ or Mn2+) coordinating the diphosphate substrate and facilitating ionization of the leaving group. The EC assignment 4.2.3.- is supported by the 2024 Zhou et al. paper (PubMed:39511739). Thus Mg(2+) is well-supported as the cofactor for a terpene cyclase, even though the specific annotation here is by similarity.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If the model could positively identify the sequence as a terpene cyclase, then Mg(2+) is the well-established cofactor for the diphosphate-ionization mechanism. Partial elimination reasoning is possible: no pantetheine-binding ACP domain (rules out A), no obvious heme-ligand His/Cys geometry (weakly rules out C), and no canonical 2-His-1-carboxylate facial triad (weakly rules out D). However, the positive identification step—recognizing a 405-aa sequence as a terpene cyclase—is the critical bottleneck, and the canonical DDxxD aspartate-rich metal-binding motif is NOT present in recognizable form (the closest matches are DDEIS and DDTIH, neither of which is DDxxD). Without this motif or a database match, the sequence provides no strong positive signal for terpene cyclase identity.",
    "missing_item_specific_fact": "The specific identification of this 405-aa sequence as terpene cyclase pbrA (or any terpene cyclase) cannot be reliably made from the raw sequence alone. The canonical DDxxD motif is absent or highly degenerate. Identification requires BLAST/database lookup or memorization of this particular entry. The 2024 characterization paper (PubMed:39511739) established the terpene cyclase function, but this is not inferable from sequence features visible in the input.",
    "reason": "The reasoning chain requires: (1) identify protein as terpene cyclase → (2) know terpene cyclases use Mg2+. Step 2 is general biological knowledge, but step 1 is essentially a lookup problem. The absence of the canonical DDxxD motif and the lack of other unmistakable terpene-cyclase-specific sequence features mean a model cannot reliably reach step 2 from the sequence alone. The elimination of distractors A and C is somewhat plausible by absence of their signature motifs, but elimination of D (Fe2+) is weak since Fe2+ and Mg2+ are both common divalent cation cofactors. The question effectively requires recognizing this specific protein's identity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given correct identification as a terpene cyclase, Mg(2+) is the clear and unambiguous answer. The distractors (pantetheine 4'-phosphate, heme, Fe2+) correspond to mechanistically distinct enzyme classes and are not plausible alternatives for a terpene cyclase. No ambiguity in the correct answer once the protein identity is established."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is by similarity (ECO:0000250, transferred from P13513), not direct experimental evidence on pbrA itself. However, the general biochemistry of terpene cyclases strongly supports Mg2+.",
    "The canonical DDxxD aspartate-rich motif is not clearly present in this sequence, making sequence-based identification of the terpene cyclase fold difficult without database access.",
    "The protein was first functionally characterized in 2024 (PubMed:39511739), so this is a relatively recent annotation.",
    "The reviewer-only evidence was not available to the evaluated model; the model must work from the raw sequence and choices alone.",
    "The EC number is 4.2.3.- (incomplete), meaning the specific terpene cyclase subclass is not fully resolved in the annotation."
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

**Accession:** `A0A0F7TWX5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Aspterric acid biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39511739","source":"PubMed"}],"value":"4.2.3.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39511739","source":"PubMed"}],"value":"Terpene cyclase pbrA"}}}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:18420"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P13513","source":"UniProtKB"}],"name":"Mg(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWX5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.624982+00:00.  

```json
{"citation":{"authors":["Zhou Z.","Zhang Y.","Wu Q.","Hou X.","Zhang B."],"citationCrossReferences":[{"database":"PubMed","id":"39511739"},{"database":"DOI","id":"10.1021/acs.jafc.4c08468"}],"citationType":"journal article","firstPage":"25755","id":"39511739","journal":"J. Agric. Food Chem.","lastPage":"25766","publicationDate":"2024","title":"Yeast synthesis and herbicidal activity evaluation of aspterric acid.","volume":"72"},"referenceNumber":2,"referencePositions":["FUNCTION","PATHWAY","BIOTECHNOLOGY"]}
```

Source SHA-256: `e5c7bc5d6c9449056bcb179284140dfad029fb97ea3206db0ebed6688d6396d9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
DE   RecName: Full=Terpene cyclase pbrA {ECO:0000303|PubMed:39511739};
DE            EC=4.2.3.- {ECO:0000305|PubMed:39511739};
DE   AltName: Full=Aspterric acid biosynthesis cluster protein A {ECO:0000303|PubMed:39511739};
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 22-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
RN   [2]
RP   FUNCTION, PATHWAY, AND BIOTECHNOLOGY.
RX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;
RA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;
RT   "Yeast synthesis and herbicidal activity evaluation of aspterric acid.";
RL   J. Agric. Food Chem. 72:25755-25766(2024).
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWX5?format=txt&versions=30)  
**Locator:** `lines 37-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:17.746470+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;
CC         Evidence={ECO:0000250|UniProtKB:P13513};
```

Source SHA-256: `384a95ec3352046b0f3464b2a89ebb41f2b203da008eaf15f997962c8728120c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 4. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
