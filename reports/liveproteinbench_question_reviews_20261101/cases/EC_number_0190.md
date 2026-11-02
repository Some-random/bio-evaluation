# EC_number_0190

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.2.19

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRSFLYMLSQRPKLACLCGKSIIIWPGKRTNLPENAFTQRMLQECGQMAKPDASVDLDNFKAISEQSPAEFGIDSCRVKAQPEDRSDRIREQIASAYPVIHERTLLLFISFLEHKLTFGSEQEKAIYKDMTVVDLVQRLLAKRCVWFFGANDYYRTMQGNIGNEGFEAVGTPAEKEPLTLTSVLSYDEIKLSALLYVSCHSEFINNGSRVNGGEVLQNKDTIEREGVVIGLIGARFERPDVMEYQDIMITKTQNTEANGYGFDLEQISSETVTPASDLRRIWREFYEEPRDFIYADTPYDTTRFEEVSQGIFDHQVMRKRYAISFDTLLLEAQDRAFKAGKPAYIHVVGIGLGVWKAARQQERTFLESFEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV

[Multiple Choices]
A. 3.2.2.19
B. 3.2.2.5
C. 1.11.1.24
D. 2.8.1.7
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact 508-aa sequence matches UniProt Q9W4J9, which is annotated as EC 3.2.2.19. Its catalytic-activity annotation links that EC to a PubMed source with experimental evidence (ECO:0000269); the cited study is also associated with a structure and function/catalytic-activity evidence. This supports A, though the primary paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a sufficiently specific, defensible way to distinguish the arginine-specific ADP-ribosyl hydrolase activity in A from the other candidate EC activities.


**Missing item-specific fact**

> The protein-specific substrate specificity and corresponding experimentally supported EC annotation are absent from the input.


**Reason**

> Identifying the exact EC requires knowledge of this protein’s characterized catalytic activity or an item-specific functional annotation; general sequence reasoning does not establish that precise reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and catalytic-activity evidence support A; the supplied evidence does not establish another listed choice as a competing activity.


### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The UniProt annotation cites experimental evidence, but the primary publication was not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible way to distinguish the arginine-specific ADP-ribosyl hydrolase activity in A from the other candidate EC activities.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate specificity and corresponding experimentally supported EC annotation are absent from the input.",
    "reason": "Identifying the exact EC requires knowledge of this protein’s characterized catalytic activity or an item-specific functional annotation; general sequence reasoning does not establish that precise reaction."
  },
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 508-aa sequence matches UniProt Q9W4J9, which is annotated as EC 3.2.2.19. Its catalytic-activity annotation links that EC to a PubMed source with experimental evidence (ECO:0000269); the cited study is also associated with a structure and function/catalytic-activity evidence. This supports A, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the primary publication was not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and catalytic-activity evidence support A; the supplied evidence does not establish another listed choice as a competing activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 508-aa sequence matches UniProt Q9W4J9, which is annotated as EC 3.2.2.19. Its catalytic-activity annotation links that EC to a PubMed source with experimental evidence (ECO:0000269); the cited study is also associated with a structure and function/catalytic-activity evidence. This supports A, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a sufficiently specific, defensible way to distinguish the arginine-specific ADP-ribosyl hydrolase activity in A from the other candidate EC activities.",
    "missing_item_specific_fact": "The protein-specific substrate specificity and corresponding experimentally supported EC annotation are absent from the input.",
    "reason": "Identifying the exact EC requires knowledge of this protein’s characterized catalytic activity or an item-specific functional annotation; general sequence reasoning does not establish that precise reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and catalytic-activity evidence support A; the supplied evidence does not establish another listed choice as a competing activity."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The UniProt annotation cites experimental evidence, but the primary publication was not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA) matches the supplied sequence exactly (SHA256 confirmed). The EC number 3.2.2.19 (ADP-ribosylarginine hydrolase) is annotated with evidence code ECO:0000269 (direct assay, PubMed:38503748) and corroborated by X-ray crystallography (PDB 8DMU, 2.00 Å, ECO:0007744). The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-&#91;protein&#93; + H2O = ADP-D-ribose + L-arginyl-&#91;protein&#93; is explicitly assigned to EC 3.2.2.19. This is experimental evidence, not mere computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a recognizable macrodomain motif (GTPAEKEP at ~residues 130-140), which is a well-known ADP-ribose-binding module. This could weakly steer a knowledgeable reader toward ADP-ribose-related glycosylases (EC 3.2.2.x) over peroxidase (1.11.1.24) or sulfurtransferase (2.8.1.7). However, distinguishing EC 3.2.2.19 (ADP-ribosylarginine hydrolase) from EC 3.2.2.5 (NAD+ glycohydrolase) requires knowing the specific substrate specificity of this protein—whether it hydrolyzes the N-glycosidic bond in ADP-ribosylarginine or in NAD+. The macrodomain fold is shared across multiple ADP-ribose-processing enzymes and does not by itself resolve the 4th digit.


**Missing item-specific fact**

> The specific catalytic substrate preference of this Drosophila macrodomain protein (ADP-ribosylarginine vs. NAD+), established experimentally in PubMed:38503748 and PDB 8DMU, is required to choose 3.2.2.19 over 3.2.2.5. No general sequence heuristic or fold-level reasoning uniquely determines the 4th EC digit here.


**Reason**

> While the macrodomain provides a structural hint toward ADP-ribose metabolism (eliminating C and D), the critical A-vs-B distinction (3.2.2.19 vs. 3.2.2.5) depends on item-specific experimental knowledge of this protein's exact catalytic activity, not on generalizable sequence-to-function inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both 3.2.2.19 and 3.2.2.5 belong to the same glycosylase subclass (EC 3.2.2) and involve N-glycosidic bond hydrolysis in NAD+/ADP-ribose chemistry. Without the specific experimental data showing arginine-specific ADP-ribosyl bond cleavage, a model relying only on the macrodomain fold could reasonably consider 3.2.2.5 as well. Options C (peroxidase) and D (sulfurtransferase) are clearly eliminable by fold and motif analysis.


### Important caveats

- The UniProt annotation for EC 3.2.2.19 was added on 2025-02-05 (entry first public date), supported by a 2024 Nature Communications paper and PDB 8DMU. If the benchmark was constructed before this date, the annotation may not have existed in the author's source snapshot.
- The identity of the protein (Q9W4J9) was inferred by the reviewer from dataset metadata, not from the evaluated model's input.
- The macrodomain GTP motif is visible in the sequence but its identification requires specialized structural biology knowledge; it is not obvious from primary sequence alone without domain-database lookup.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable macrodomain motif (GTPAEKEP at ~residues 130-140), which is a well-known ADP-ribose-binding module. This could weakly steer a knowledgeable reader toward ADP-ribose-related glycosylases (EC 3.2.2.x) over peroxidase (1.11.1.24) or sulfurtransferase (2.8.1.7). However, distinguishing EC 3.2.2.19 (ADP-ribosylarginine hydrolase) from EC 3.2.2.5 (NAD+ glycohydrolase) requires knowing the specific substrate specificity of this protein—whether it hydrolyzes the N-glycosidic bond in ADP-ribosylarginine or in NAD+. The macrodomain fold is shared across multiple ADP-ribose-processing enzymes and does not by itself resolve the 4th digit.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific catalytic substrate preference of this Drosophila macrodomain protein (ADP-ribosylarginine vs. NAD+), established experimentally in PubMed:38503748 and PDB 8DMU, is required to choose 3.2.2.19 over 3.2.2.5. No general sequence heuristic or fold-level reasoning uniquely determines the 4th EC digit here.",
    "reason": "While the macrodomain provides a structural hint toward ADP-ribose metabolism (eliminating C and D), the critical A-vs-B distinction (3.2.2.19 vs. 3.2.2.5) depends on item-specific experimental knowledge of this protein's exact catalytic activity, not on generalizable sequence-to-function inference."
  },
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA) matches the supplied sequence exactly (SHA256 confirmed). The EC number 3.2.2.19 (ADP-ribosylarginine hydrolase) is annotated with evidence code ECO:0000269 (direct assay, PubMed:38503748) and corroborated by X-ray crystallography (PDB 8DMU, 2.00 Å, ECO:0007744). The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is explicitly assigned to EC 3.2.2.19. This is experimental evidence, not mere computational inference."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.2.19 was added on 2025-02-05 (entry first public date), supported by a 2024 Nature Communications paper and PDB 8DMU. If the benchmark was constructed before this date, the annotation may not have existed in the author's source snapshot.",
    "The identity of the protein (Q9W4J9) was inferred by the reviewer from dataset metadata, not from the evaluated model's input.",
    "The macrodomain GTP motif is visible in the sequence but its identification requires specialized structural biology knowledge; it is not obvious from primary sequence alone without domain-database lookup."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both 3.2.2.19 and 3.2.2.5 belong to the same glycosylase subclass (EC 3.2.2) and involve N-glycosidic bond hydrolysis in NAD+/ADP-ribose chemistry. Without the specific experimental data showing arginine-specific ADP-ribosyl bond cleavage, a model relying only on the macrodomain fold could reasonably consider 3.2.2.5 as well. Options C (peroxidase) and D (sulfurtransferase) are clearly eliminable by fold and motif analysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster, 508 AA) matches the supplied sequence exactly (SHA256 confirmed). The EC number 3.2.2.19 (ADP-ribosylarginine hydrolase) is annotated with evidence code ECO:0000269 (direct assay, PubMed:38503748) and corroborated by X-ray crystallography (PDB 8DMU, 2.00 Å, ECO:0007744). The catalytic reaction N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein] is explicitly assigned to EC 3.2.2.19. This is experimental evidence, not mere computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a recognizable macrodomain motif (GTPAEKEP at ~residues 130-140), which is a well-known ADP-ribose-binding module. This could weakly steer a knowledgeable reader toward ADP-ribose-related glycosylases (EC 3.2.2.x) over peroxidase (1.11.1.24) or sulfurtransferase (2.8.1.7). However, distinguishing EC 3.2.2.19 (ADP-ribosylarginine hydrolase) from EC 3.2.2.5 (NAD+ glycohydrolase) requires knowing the specific substrate specificity of this protein—whether it hydrolyzes the N-glycosidic bond in ADP-ribosylarginine or in NAD+. The macrodomain fold is shared across multiple ADP-ribose-processing enzymes and does not by itself resolve the 4th digit.",
    "missing_item_specific_fact": "The specific catalytic substrate preference of this Drosophila macrodomain protein (ADP-ribosylarginine vs. NAD+), established experimentally in PubMed:38503748 and PDB 8DMU, is required to choose 3.2.2.19 over 3.2.2.5. No general sequence heuristic or fold-level reasoning uniquely determines the 4th EC digit here.",
    "reason": "While the macrodomain provides a structural hint toward ADP-ribose metabolism (eliminating C and D), the critical A-vs-B distinction (3.2.2.19 vs. 3.2.2.5) depends on item-specific experimental knowledge of this protein's exact catalytic activity, not on generalizable sequence-to-function inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both 3.2.2.19 and 3.2.2.5 belong to the same glycosylase subclass (EC 3.2.2) and involve N-glycosidic bond hydrolysis in NAD+/ADP-ribose chemistry. Without the specific experimental data showing arginine-specific ADP-ribosyl bond cleavage, a model relying only on the macrodomain fold could reasonably consider 3.2.2.5 as well. Options C (peroxidase) and D (sulfurtransferase) are clearly eliminable by fold and motif analysis."
  },
  "important_caveats": [
    "The UniProt annotation for EC 3.2.2.19 was added on 2025-02-05 (entry first public date), supported by a 2024 Nature Communications paper and PDB 8DMU. If the benchmark was constructed before this date, the annotation may not have existed in the author's source snapshot.",
    "The identity of the protein (Q9W4J9) was inferred by the reviewer from dataset metadata, not from the evaluated model's input.",
    "The macrodomain GTP motif is visible in the sequence but its identification requires specialized structural biology knowledge; it is not obvious from primary sequence alone without domain-database lookup."
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

**Accession:** `Q9W4J9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 153. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
"Q9W4J9"
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"value":"3.2.2.19"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"ADP-ribosylarginine hydrolase CG3568"}}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:14885"},{"database":"Rhea","id":"RHEA-COMP:10532"},{"database":"Rhea","id":"RHEA-COMP:15087"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29965"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:142554"}]}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.2.19","evidences":[{"evidenceCode":"ECO:0000269","id":"38503748","source":"PubMed"}],"name":"N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20784"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:32682"},{"database":"ChEBI","id":"CHEBI:57967"},{"database":"ChEBI","id":"CHEBI:60267"}]}}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:51.239752+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Fu J.","Rack J.G.M.","Li C.","Voorneveld J.","Filippov D.V.","Ahel I.","Luo Z.Q.","Das C."],"citationCrossReferences":[{"database":"PubMed","id":"38503748"},{"database":"DOI","id":"10.1038/s41467-024-46649-2"}],"citationType":"journal article","firstPage":"2452","id":"38503748","journal":"Nat. Commun.","lastPage":"2452","publicationDate":"2024","title":"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.","volume":"15"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8DMU","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 25-508","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
ID   ADPR2_DROME             Reviewed;         508 AA.
AC   Q9W4J9;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-OCT-2002, sequence version 2.
DT   28-JAN-2026, entry version 153.
DE   RecName: Full=ADP-ribosylarginine hydrolase CG3568 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
GN   ORFNames=CG3568 {ECO:0000312|FlyBase:FBgn0029710};
OS   Drosophila melanogaster (Fruit fly).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;
OC   Drosophilidae; Drosophila; Sophophora.
OX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
DE   RecName: Full=ADP-ribosylarginine hydrolase CG3568 {ECO:0000305};
DE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 77-85`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
RN   [4] {ECO:0007744|PDB:8DMU}
RP   X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 25-508, FUNCTION, AND CATALYTIC
RP   ACTIVITY.
RX   PubMed=38503748; DOI=10.1038/s41467-024-46649-2;
RA   Zhang Z., Fu J., Rack J.G.M., Li C., Voorneveld J., Filippov D.V., Ahel I.,
RA   Luo Z.Q., Das C.;
RT   "Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a
RT   conserved arginine-specific macrodomain.";
RL   Nat. Commun. 15:2452-2452(2024).
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 89-94`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-
CC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-
CC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;
CC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)  
**Locator:** `lines 95-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 2.  
**Retrieved:** 2026-11-02T04:33:55.177738+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-
CC         arginine; Xref=Rhea:RHEA:20784, ChEBI:CHEBI:15377, ChEBI:CHEBI:32682,
CC         ChEBI:CHEBI:57967, ChEBI:CHEBI:60267; EC=3.2.2.19;
CC         Evidence={ECO:0000269|PubMed:38503748};
CC   ---------------------------------------------------------------------------
CC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms
CC   Distributed under the Creative Commons Attribution (CC BY 4.0) License
CC   ---------------------------------------------------------------------------
```

Source SHA-256: `9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
