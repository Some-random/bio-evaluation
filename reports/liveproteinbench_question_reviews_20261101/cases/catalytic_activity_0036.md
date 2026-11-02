# catalytic_activity_0036

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **C** — ATP + H2O = ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAPAATAAASSGKGSFDLATLFVADKAARDEAGLALADAVKKSGVEFFTQIGFNDAIVKALNDKKSQSAREGACEVISTLCENGAAQLLEPHVISSAENTPFPALLEAFADKVAAVKTAAIAAVKAIVQSMNPWASFVLLPALLNLIRTSGKWQIKAGSLEILQQLITSAPFQMGEAMPDLVPVLAEAVWDTKSDVKKAAKATLEKAVSLVENKDIEKFVPALVKSLLNPIEEVPKTISLLSATTFVSEVTAPTISLIAPLLIRGLDERPTATKRKVCVIADNMSKLVDSEYTVRPFLPQLLPRLIKTSETIADPEARSVANRAIVTLRRIGKVPAESDGSDLPPLPVAEGPHLATNFVALVKKHGGVSVEQTNPGLAYAGVLAASLVNHHNFDQKTWESTLPPYLKLALPSYDSLPAVRELLQKKADEAETDDAKFPDEEEGEDLCNIEQFNLAYGAKILLHHANMRLKRGHRYGLCGRNGSGKSTLMNAIINNQVEGFPPPTEVRTFYVQHDIDGSEAEISILDWVLGDKRLLATPDEIKSTLESVGFDEVKQKNSIGSLSGGWKMKLALARAILFKADILLLDEPTNHLDVLNVDWLINYLTSLTRCTSIIVSHDSDFLNRTVTDVLHLNNFKLKRYPGNLEDFVQHVPEAKSYYQLDVAEDYQFKLPNPPLLDGVKTKEKSLLKMRNVSFQYPGSSIQQLYDISLQVSLSSRVAILGPNGSGKSTLVKLLTGETEPNLGGQVWKHPNLVIGYVAQHAFHHIDNHLDSTPLEYMLWRYQTGEDLEEMHKANRVMTEAEIAKMKEGATVIKDGVKRIIDELVARKKLKQSYEYEVSFKGMSSAENIWISRDELVARGFEKKVMELDTREAQRLGLMRPLVRREIEKHFEDFGLDAEFVSHNSMRGLSGGQKVKVVLGAATWRRPHIICLDEPTNYLDRESLAALIAALKNFEGGVLIITHNREFSESICTEVWAMREGYLEASGHNWVEGQGSGERIDKKAADDDEVEYDALGNPIVKAKKEKKLSAADKRKAKKDRMARRKRGEEVFSDEEL

[Multiple Choices]
A. vinorine + reduced [NADPH--hemoprotein reductase] + O2 = vomilenine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
B. 2,2-dihydroxyspirilloxanthin = 2-oxospirilloxanthin + H2O
C. ATP + H2O = ADP + phosphate + H(+)
D. alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies the protein as elongation factor 3 and lists ATP hydrolysis as its catalytic activity. The reaction annotation is transferred by similarity from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple P-loop NTPase-like motifs, including GPNGSGKST, together with associated ATPase-domain motifs. These provide a concrete basis to favor ATP hydrolysis over the specialized transformations in A, B, and D.


**Missing item-specific fact**

> No protein-specific annotation is supplied; the reviewer-only annotation identifies the protein as elongation factor 3 and reports ATP hydrolysis, with that activity transferred by similarity.


**Reason**

> The motifs support ATPase activity from the sequence itself, making choice C meaningfully distinguishable from the alternatives. The reviewer-only database evidence supports the expected answer but is not needed as input to that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the sequence's ATPase-like motifs favor the ATP hydrolysis option.


### Important caveats

- The cited UniProt catalytic-activity evidence is transferred by similarity, not direct experimental evidence for this sequence.
- Sequence motifs support an ATPase inference but do not independently verify the exact reaction annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple P-loop NTPase-like motifs, including GPNGSGKST, together with associated ATPase-domain motifs. These provide a concrete basis to favor ATP hydrolysis over the specialized transformations in A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is supplied; the reviewer-only annotation identifies the protein as elongation factor 3 and reports ATP hydrolysis, with that activity transferred by similarity.",
    "reason": "The motifs support ATPase activity from the sequence itself, making choice C meaningfully distinguishable from the alternatives. The reviewer-only database evidence supports the expected answer but is not needed as input to that inference."
  },
  "case_id": "catalytic_activity_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as elongation factor 3 and lists ATP hydrolysis as its catalytic activity. The reaction annotation is transferred by similarity from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity evidence is transferred by similarity, not direct experimental evidence for this sequence.",
    "Sequence motifs support an ATPase inference but do not independently verify the exact reaction annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the sequence's ATPase-like motifs favor the ATP hydrolysis option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as elongation factor 3 and lists ATP hydrolysis as its catalytic activity. The reaction annotation is transferred by similarity from another UniProt entry (ECO:0000250), so this supports the key as a database annotation rather than establishing direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple P-loop NTPase-like motifs, including GPNGSGKST, together with associated ATPase-domain motifs. These provide a concrete basis to favor ATP hydrolysis over the specialized transformations in A, B, and D.",
    "missing_item_specific_fact": "No protein-specific annotation is supplied; the reviewer-only annotation identifies the protein as elongation factor 3 and reports ATP hydrolysis, with that activity transferred by similarity.",
    "reason": "The motifs support ATPase activity from the sequence itself, making choice C meaningfully distinguishable from the alternatives. The reviewer-only database evidence supports the expected answer but is not needed as input to that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the sequence's ATPase-like motifs favor the ATP hydrolysis option."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity evidence is transferred by similarity, not direct experimental evidence for this sequence.",
    "Sequence motifs support an ATPase inference but do not independently verify the exact reaction annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VQZ9 (EF3_CRYN9, Cryptococcus neoformans Elongation Factor 3) annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' with EC 3.6.4.-. The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation evidence code is ECO:0000250 (inferred by similarity to Q5KIM6), which is computational/transferred rather than direct experimental, but the ATPase activity of EF-3 family proteins is well-established in the literature and the reaction is the canonical activity for this protein family. Both the current (v68) and historical (v66) records confirm this annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two clear Walker A / P-loop motifs ('GSGKST' in 'GLCGRNGSGKSTLMN' and 'GPNGSGKSTLVK') and Walker B motifs ('DEPT' / 'DEPTN' in 'LLDEPTNHLDVL' and 'CLDEPTNYLDRE'), which are hallmark signatures of ATP-binding and ATP-hydrolyzing proteins (AAA+ ATPases, ABC transporters, helicases). Among the four choices, only C (ATP + H2O = ADP + phosphate + H+) corresponds to ATP hydrolysis. The other three options require entirely different enzyme classes: A requires a cytochrome P450 heme-binding motif (FxxGxxxCxG), B requires a carotenoid-cleaving oxygenase domain, and D requires a TIM-barrel isomerase fold with specific active-site residues. None of these motifs are present. A biologist familiar with P-loop and Walker B motifs can identify the protein as an ATPase and select C without knowing the specific protein identity.


**Missing item-specific fact**

> None critical. Exact protein identity (EF-3 vs. another ATPase) is not needed because the question asks for the catalytic reaction, and only one option matches ATP hydrolysis.


**Reason**

> The presence of multiple GSGKST (Walker A) and DEPT (Walker B) motifs is general biochemical knowledge that directly implicates ATP hydrolysis. The distractors represent unrelated enzyme classes with no sequence support. The reasoning path from recognizable sequence motifs to the correct answer is concrete and does not require memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option C is consistent with the ATP-binding motifs visible in the sequence. Options A, B, and D require enzyme classes (P450, carotenoid oxygenase, sugar isomerase) whose defining sequence signatures are entirely absent. No ambiguity exists among the choices.


### Important caveats

- The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity to Q5KIM6), not direct experimental evidence. However, EF-3 ATPase activity is broadly supported in the literature.
- The sequence could in principle belong to another ATPase family (e.g., ABC transporter), but this does not affect the answer because the question asks for the catalytic reaction, and only C involves ATP hydrolysis.
- The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning argument relies solely on motifs visible in the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two clear Walker A / P-loop motifs ('GSGKST' in 'GLCGRNGSGKSTLMN' and 'GPNGSGKSTLVK') and Walker B motifs ('DEPT' / 'DEPTN' in 'LLDEPTNHLDVL' and 'CLDEPTNYLDRE'), which are hallmark signatures of ATP-binding and ATP-hydrolyzing proteins (AAA+ ATPases, ABC transporters, helicases). Among the four choices, only C (ATP + H2O = ADP + phosphate + H+) corresponds to ATP hydrolysis. The other three options require entirely different enzyme classes: A requires a cytochrome P450 heme-binding motif (FxxGxxxCxG), B requires a carotenoid-cleaving oxygenase domain, and D requires a TIM-barrel isomerase fold with specific active-site residues. None of these motifs are present. A biologist familiar with P-loop and Walker B motifs can identify the protein as an ATPase and select C without knowing the specific protein identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Exact protein identity (EF-3 vs. another ATPase) is not needed because the question asks for the catalytic reaction, and only one option matches ATP hydrolysis.",
    "reason": "The presence of multiple GSGKST (Walker A) and DEPT (Walker B) motifs is general biochemical knowledge that directly implicates ATP hydrolysis. The distractors represent unrelated enzyme classes with no sequence support. The reasoning path from recognizable sequence motifs to the correct answer is concrete and does not require memorizing this specific protein's database entry."
  },
  "case_id": "catalytic_activity_0036",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VQZ9 (EF3_CRYN9, Cryptococcus neoformans Elongation Factor 3) annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' with EC 3.6.4.-. The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation evidence code is ECO:0000250 (inferred by similarity to Q5KIM6), which is computational/transferred rather than direct experimental, but the ATPase activity of EF-3 family proteins is well-established in the literature and the reaction is the canonical activity for this protein family. Both the current (v68) and historical (v66) records confirm this annotation."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity to Q5KIM6), not direct experimental evidence. However, EF-3 ATPase activity is broadly supported in the literature.",
    "The sequence could in principle belong to another ATPase family (e.g., ABC transporter), but this does not affect the answer because the question asks for the catalytic reaction, and only C involves ATP hydrolysis.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning argument relies solely on motifs visible in the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the ATP-binding motifs visible in the sequence. Options A, B, and D require enzyme classes (P450, carotenoid oxygenase, sugar isomerase) whose defining sequence signatures are entirely absent. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0036",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VQZ9 (EF3_CRYN9, Cryptococcus neoformans Elongation Factor 3) annotates the catalytic activity as 'ATP + H2O = ADP + phosphate + H(+)' with EC 3.6.4.-. The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation evidence code is ECO:0000250 (inferred by similarity to Q5KIM6), which is computational/transferred rather than direct experimental, but the ATPase activity of EF-3 family proteins is well-established in the literature and the reaction is the canonical activity for this protein family. Both the current (v68) and historical (v66) records confirm this annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two clear Walker A / P-loop motifs ('GSGKST' in 'GLCGRNGSGKSTLMN' and 'GPNGSGKSTLVK') and Walker B motifs ('DEPT' / 'DEPTN' in 'LLDEPTNHLDVL' and 'CLDEPTNYLDRE'), which are hallmark signatures of ATP-binding and ATP-hydrolyzing proteins (AAA+ ATPases, ABC transporters, helicases). Among the four choices, only C (ATP + H2O = ADP + phosphate + H+) corresponds to ATP hydrolysis. The other three options require entirely different enzyme classes: A requires a cytochrome P450 heme-binding motif (FxxGxxxCxG), B requires a carotenoid-cleaving oxygenase domain, and D requires a TIM-barrel isomerase fold with specific active-site residues. None of these motifs are present. A biologist familiar with P-loop and Walker B motifs can identify the protein as an ATPase and select C without knowing the specific protein identity.",
    "missing_item_specific_fact": "None critical. Exact protein identity (EF-3 vs. another ATPase) is not needed because the question asks for the catalytic reaction, and only one option matches ATP hydrolysis.",
    "reason": "The presence of multiple GSGKST (Walker A) and DEPT (Walker B) motifs is general biochemical knowledge that directly implicates ATP hydrolysis. The distractors represent unrelated enzyme classes with no sequence support. The reasoning path from recognizable sequence motifs to the correct answer is concrete and does not require memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option C is consistent with the ATP-binding motifs visible in the sequence. Options A, B, and D require enzyme classes (P450, carotenoid oxygenase, sugar isomerase) whose defining sequence signatures are entirely absent. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The UniProt catalytic activity annotation carries evidence code ECO:0000250 (inferred by similarity to Q5KIM6), not direct experimental evidence. However, EF-3 ATPase activity is broadly supported in the literature.",
    "The sequence could in principle belong to another ATPase family (e.g., ABC transporter), but this does not affect the answer because the question asks for the catalytic reaction, and only C involves ATP hydrolysis.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; the reasoning argument relies solely on motifs visible in the supplied sequence."
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

**Accession:** `J9VQZ9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 66. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.554047+00:00.  

```json
"J9VQZ9"
```

Source SHA-256: `0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.554047+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Eukaryotic elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"eEF3"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5KIM6","source":"UniProtKB"}],"value":"3.6.4.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Elongation factor 3"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"EF-3"}]}}
```

Source SHA-256: `0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VQZ9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.554047+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q5KIM6","source":"UniProtKB"}],"name":"ATP + H2O = ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:13065"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `0718e489935e5ae6b72d7188aab9702900c159d1e74b27c93bd83d8e8d269bd9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 2.  
**Retrieved:** 2026-11-01T06:28:11.511490+00:00.  

```text
ID   EF3_CRYN9               Reviewed;        1055 AA.
AC   J9VQZ9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-NOV-2013, sequence version 2.
DT   28-JAN-2026, entry version 66.
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000250|UniProtKB:Q5KIM6};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
GN   Name=TEF3 {ECO:0000305}; ORFNames=CNAG_01117 {ECO:0000312|EMBL:AFR95029.2};
OS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)
OS   (Cryptococcus neoformans var. grubii serotype A).
OC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;
OC   Tremellales; Cryptococcaceae; Cryptococcus;
OC   Cryptococcus neoformans species complex.
OX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR95029.2, ECO:0000312|Proteomes:UP000010091};
```

Source SHA-256: `a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 2.  
**Retrieved:** 2026-11-01T06:28:11.511490+00:00.  

```text
DE   RecName: Full=Elongation factor 3 {ECO:0000305};
DE            Short=EF-3 {ECO:0000305};
DE            EC=3.6.4.- {ECO:0000250|UniProtKB:Q5KIM6};
DE   AltName: Full=Eukaryotic elongation factor 3 {ECO:0000305};
DE            Short=eEF3 {ECO:0000305};
```

Source SHA-256: `a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VQZ9?format=txt&versions=66)  
**Locator:** `lines 55-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 66 / 2.  
**Retrieved:** 2026-11-01T06:28:11.511490+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=ATP + H2O = ADP + phosphate + H(+); Xref=Rhea:RHEA:13065,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:456216;
CC         Evidence={ECO:0000250|UniProtKB:Q5KIM6};
```

Source SHA-256: `a7573f1eb27ed3976b103711b49783a1b1b870f6216c255c67bfd6b86729ee7d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 36. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
