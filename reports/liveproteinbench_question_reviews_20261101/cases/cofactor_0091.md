# cofactor_0091

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — Ca(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVLTRRAALLLCPWVIQLVIKRTLAGDILPNEGKKEKDDVHKIISELRFLQKVETILESSNMSVSDVEADANAYNPDRDAPKEELQKLQDQQETPSKQPNNLRNSPQKRAEKKESPGKNKKSLRLIVSENHATSPSFFEESLLQEDVVSFIQSKGKLSNLKNLKSMIIDLNSDMTDEELAEYISLLERKGALIESDKLVGADDVSLASVKDAVRRGESSVNWGKLRSTMLEVPSGESPPSHAASSGSPFDDDDDLLSEAALHREEAHLAGSKTTKGYKFNDEYRNLQWGLDLARLDETQDLINANRVSVTKICVIDSGIDYNHPDLRNNIDVNVKELHGRKGVDDDSNGVVDDVYGANFVNNSGDPMDDNYHGTHVSGIISAVGNNGIGIVGVDGHSKLVICKALDQHKLGRLGDMFKCIDYCISRQAHMINGSFSFDEYSNIFNASVEHLRSLGILFFVSASNCAHDKLSKPDIAKCDLAVNHRYPPILSKTHNNVIAVANLKRDLDESYSLSVNSFYSNIYCQLAAPGTNIYSTTPMNNYRKLNGTSMASPHVAAIASIVRSINPNLTYLQIVEILRNAIVKLPSLTERVSWGGYVDILRAVNLAIDSKAAPYIKSHSWFRWKQGSRR

[Multiple Choices]
A. Fe(2+)
B. Mg(2+)
C. Cu(2+)
D. Ca(2+)
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

> The exact sequence matches the Plasmodium vivax subtilisin-like protease SUB1, whose UniProt record explicitly annotates Ca(2+) as a cofactor with experimental evidence. Structural references also report SUB1 complexes containing calcium. This supports choice D, though the supplied excerpts do not independently establish that calcium is strictly essential for catalytic activity rather than stabilizing the enzyme.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Recognizing a subtilisin-like protease can suggest a serine-protease mechanism rather than a transition-metal-dependent catalytic mechanism, and calcium can stabilize subtilases. But those general considerations do not establish that this particular protein uses Ca(2+) or distinguish its specific calcium dependence from sequence alone.


**Missing item-specific fact**

> The protein-specific SUB1 cofactor annotation and experimental or structural evidence for calcium association.


**Reason**

> The supplied input gives only sequence and ion choices. It does not provide the protein identity, a calcium-binding assay, or a cofactor annotation; the exact choice depends on that item-specific information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports calcium as the annotated cofactor, and no alternative listed ion is supported. However, the excerpts do not fully resolve whether calcium is strictly required for catalytic activity or has a stabilizing role.


### Important caveats

- The sequence match and protein identity are established by reviewer-only evidence, not information supplied to the evaluated model.
- The database cofactor annotation cites experimental evidence, but the excerpts do not independently show an activity measurement demonstrating calcium essentiality.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Recognizing a subtilisin-like protease can suggest a serine-protease mechanism rather than a transition-metal-dependent catalytic mechanism, and calcium can stabilize subtilases. But those general considerations do not establish that this particular protein uses Ca(2+) or distinguish its specific calcium dependence from sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific SUB1 cofactor annotation and experimental or structural evidence for calcium association.",
    "reason": "The supplied input gives only sequence and ion choices. It does not provide the protein identity, a calcium-binding assay, or a cofactor annotation; the exact choice depends on that item-specific information."
  },
  "case_id": "cofactor_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C8",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium vivax subtilisin-like protease SUB1, whose UniProt record explicitly annotates Ca(2+) as a cofactor with experimental evidence. Structural references also report SUB1 complexes containing calcium. This supports choice D, though the supplied excerpts do not independently establish that calcium is strictly essential for catalytic activity rather than stabilizing the enzyme."
  },
  "important_caveats": [
    "The sequence match and protein identity are established by reviewer-only evidence, not information supplied to the evaluated model.",
    "The database cofactor annotation cites experimental evidence, but the excerpts do not independently show an activity measurement demonstrating calcium essentiality."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports calcium as the annotated cofactor, and no alternative listed ion is supported. However, the excerpts do not fully resolve whether calcium is strictly required for catalytic activity or has a stabilizing role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium vivax subtilisin-like protease SUB1, whose UniProt record explicitly annotates Ca(2+) as a cofactor with experimental evidence. Structural references also report SUB1 complexes containing calcium. This supports choice D, though the supplied excerpts do not independently establish that calcium is strictly essential for catalytic activity rather than stabilizing the enzyme.",
    "evidence_ids": ["C1", "C4", "C5", "C8", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Recognizing a subtilisin-like protease can suggest a serine-protease mechanism rather than a transition-metal-dependent catalytic mechanism, and calcium can stabilize subtilases. But those general considerations do not establish that this particular protein uses Ca(2+) or distinguish its specific calcium dependence from sequence alone.",
    "missing_item_specific_fact": "The protein-specific SUB1 cofactor annotation and experimental or structural evidence for calcium association.",
    "reason": "The supplied input gives only sequence and ion choices. It does not provide the protein identity, a calcium-binding assay, or a cofactor annotation; the exact choice depends on that item-specific information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports calcium as the annotated cofactor, and no alternative listed ion is supported. However, the excerpts do not fully resolve whether calcium is strictly required for catalytic activity or has a stabilizing role."
  },
  "important_caveats": [
    "The sequence match and protein identity are established by reviewer-only evidence, not information supplied to the evaluated model.",
    "The database cofactor annotation cites experimental evidence, but the excerpts do not independently show an activity measurement demonstrating calcium essentiality."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E6Y8B9 (Plasmodium vivax Subtilisin-like protease 1, SUB1) explicitly annotates Ca(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:25204226). Multiple X-ray crystal structures (PDB 4TR2 at 2.70 Å, 8COY/8COZ at 1.44 Å, 8QKE/8QKG at 1.50 Å) confirm Ca(2+) bound to the protein. The sequence matches the benchmark exactly (SHA-256 identical, 630 residues).

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs characteristic of the subtilisin/subtilase family (serine protease fold with catalytic triad region). Subtilases are serine proteases, not metalloproteases, which argues against metals typically associated with hydrolytic metal coordination in metalloproteases. Among the four choices, Ca(2+) is the classic structural cofactor for subtilases (well-documented in biochemistry textbooks for Bacillus subtilisins and homologs). Fe(2+) is associated with redox/oxygen-transport proteins, Cu(2+) with oxidases/SOD, and Mg(2+) with nucleotide-binding enzymes (kinases, polymerases, GTPases). The sequence also contains clusters of Asp and Asn residues (e.g., 'DDDDDLL', 'DDDSNGVVDDVYGANFVNNSGDPMDDNYHGTH', 'GIDYNHPDLRNNIDVNVKELHGRKGVDDDSNG') consistent with Ca(2+) coordination geometry (irregular, 6-8 ligands from carboxylate/amide oxygens). Eliminating the other three metals based on enzyme class (serine protease vs. redox/oxidase/phosphate-transfer) and identifying the subtilase family provides a defensible reasoning path to Ca(2+).


**Missing item-specific fact**

> None strictly required. The reasoning relies on family-level knowledge (subtilases commonly bind Ca(2+)) and elimination of metals by enzyme class, both within general biochemistry. Exact PDB structures or the specific PubMed 25204226 paper are confirmatory but not necessary for the inference.


**Reason**

> A knowledgeable model can (1) recognize subtilase family features in the sequence, (2) recall that subtilases are serine proteases that commonly use Ca(2+) as a structural cofactor, (3) eliminate Fe(2+)/Cu(2+) as redox/oxidase metals incompatible with protease function, and (4) eliminate Mg(2+) as primarily associated with phosphate-transfer enzymes. The Asp/Asn-rich clusters further support Ca(2+) coordination. This constitutes a concrete biological argument distinguishing the choices without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While Mg(2+) and Ca(2+) are both divalent cations that could in principle coordinate Asp/Asn clusters, the subtilase family association with Ca(2+) specifically (rather than Mg(2+)) is well-established. Fe(2+) and Cu(2+) are clearly inappropriate for a serine protease. The four options are sufficiently distinct that the subtilase-Ca(2+) link provides a clear discriminator.


### Important caveats

- The subtilase-Ca(2+) association is a family-level generalization; not every subtilase binds Ca(2+). However, among the four provided choices, Ca(2+) is the most defensible for a subtilase.
- Distinguishing Ca(2+) from Mg(2+) purely from sequence is inherently difficult; the argument relies on family-level knowledge rather than de novo coordination-geometry prediction from sequence.
- The UniProt annotation (ECO:0000269) is backed by direct experimental evidence (crystallography and activity assays), not merely computational prediction.
- The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence recognition and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the subtilisin/subtilase family (serine protease fold with catalytic triad region). Subtilases are serine proteases, not metalloproteases, which argues against metals typically associated with hydrolytic metal coordination in metalloproteases. Among the four choices, Ca(2+) is the classic structural cofactor for subtilases (well-documented in biochemistry textbooks for Bacillus subtilisins and homologs). Fe(2+) is associated with redox/oxygen-transport proteins, Cu(2+) with oxidases/SOD, and Mg(2+) with nucleotide-binding enzymes (kinases, polymerases, GTPases). The sequence also contains clusters of Asp and Asn residues (e.g., 'DDDDDLL', 'DDDSNGVVDDVYGANFVNNSGDPMDDNYHGTH', 'GIDYNHPDLRNNIDVNVKELHGRKGVDDDSNG') consistent with Ca(2+) coordination geometry (irregular, 6-8 ligands from carboxylate/amide oxygens). Eliminating the other three metals based on enzyme class (serine protease vs. redox/oxidase/phosphate-transfer) and identifying the subtilase family provides a defensible reasoning path to Ca(2+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The reasoning relies on family-level knowledge (subtilases commonly bind Ca(2+)) and elimination of metals by enzyme class, both within general biochemistry. Exact PDB structures or the specific PubMed 25204226 paper are confirmatory but not necessary for the inference.",
    "reason": "A knowledgeable model can (1) recognize subtilase family features in the sequence, (2) recall that subtilases are serine proteases that commonly use Ca(2+) as a structural cofactor, (3) eliminate Fe(2+)/Cu(2+) as redox/oxidase metals incompatible with protease function, and (4) eliminate Mg(2+) as primarily associated with phosphate-transfer enzymes. The Asp/Asn-rich clusters further support Ca(2+) coordination. This constitutes a concrete biological argument distinguishing the choices without requiring memorization of this specific protein's database entry."
  },
  "case_id": "cofactor_0091",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C9",
      "C10",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (Plasmodium vivax Subtilisin-like protease 1, SUB1) explicitly annotates Ca(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:25204226). Multiple X-ray crystal structures (PDB 4TR2 at 2.70 Å, 8COY/8COZ at 1.44 Å, 8QKE/8QKG at 1.50 Å) confirm Ca(2+) bound to the protein. The sequence matches the benchmark exactly (SHA-256 identical, 630 residues)."
  },
  "important_caveats": [
    "The subtilase-Ca(2+) association is a family-level generalization; not every subtilase binds Ca(2+). However, among the four provided choices, Ca(2+) is the most defensible for a subtilase.",
    "Distinguishing Ca(2+) from Mg(2+) purely from sequence is inherently difficult; the argument relies on family-level knowledge rather than de novo coordination-geometry prediction from sequence.",
    "The UniProt annotation (ECO:0000269) is backed by direct experimental evidence (crystallography and activity assays), not merely computational prediction.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence recognition and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Mg(2+) and Ca(2+) are both divalent cations that could in principle coordinate Asp/Asn clusters, the subtilase family association with Ca(2+) specifically (rather than Mg(2+)) is well-established. Fe(2+) and Cu(2+) are clearly inappropriate for a serine protease. The four options are sufficiently distinct that the subtilase-Ca(2+) link provides a clear discriminator."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0091",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E6Y8B9 (Plasmodium vivax Subtilisin-like protease 1, SUB1) explicitly annotates Ca(2+) as the cofactor with experimental evidence (ECO:0000269|PubMed:25204226). Multiple X-ray crystal structures (PDB 4TR2 at 2.70 Å, 8COY/8COZ at 1.44 Å, 8QKE/8QKG at 1.50 Å) confirm Ca(2+) bound to the protein. The sequence matches the benchmark exactly (SHA-256 identical, 630 residues).",
    "evidence_ids": ["C5", "C8", "C9", "C10", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs characteristic of the subtilisin/subtilase family (serine protease fold with catalytic triad region). Subtilases are serine proteases, not metalloproteases, which argues against metals typically associated with hydrolytic metal coordination in metalloproteases. Among the four choices, Ca(2+) is the classic structural cofactor for subtilases (well-documented in biochemistry textbooks for Bacillus subtilisins and homologs). Fe(2+) is associated with redox/oxygen-transport proteins, Cu(2+) with oxidases/SOD, and Mg(2+) with nucleotide-binding enzymes (kinases, polymerases, GTPases). The sequence also contains clusters of Asp and Asn residues (e.g., 'DDDDDLL', 'DDDSNGVVDDVYGANFVNNSGDPMDDNYHGTH', 'GIDYNHPDLRNNIDVNVKELHGRKGVDDDSNG') consistent with Ca(2+) coordination geometry (irregular, 6-8 ligands from carboxylate/amide oxygens). Eliminating the other three metals based on enzyme class (serine protease vs. redox/oxidase/phosphate-transfer) and identifying the subtilase family provides a defensible reasoning path to Ca(2+).",
    "missing_item_specific_fact": "None strictly required. The reasoning relies on family-level knowledge (subtilases commonly bind Ca(2+)) and elimination of metals by enzyme class, both within general biochemistry. Exact PDB structures or the specific PubMed 25204226 paper are confirmatory but not necessary for the inference.",
    "reason": "A knowledgeable model can (1) recognize subtilase family features in the sequence, (2) recall that subtilases are serine proteases that commonly use Ca(2+) as a structural cofactor, (3) eliminate Fe(2+)/Cu(2+) as redox/oxidase metals incompatible with protease function, and (4) eliminate Mg(2+) as primarily associated with phosphate-transfer enzymes. The Asp/Asn-rich clusters further support Ca(2+) coordination. This constitutes a concrete biological argument distinguishing the choices without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While Mg(2+) and Ca(2+) are both divalent cations that could in principle coordinate Asp/Asn clusters, the subtilase family association with Ca(2+) specifically (rather than Mg(2+)) is well-established. Fe(2+) and Cu(2+) are clearly inappropriate for a serine protease. The four options are sufficiently distinct that the subtilase-Ca(2+) link provides a clear discriminator."
  },
  "important_caveats": [
    "The subtilase-Ca(2+) association is a family-level generalization; not every subtilase binds Ca(2+). However, among the four provided choices, Ca(2+) is the most defensible for a subtilase.",
    "Distinguishing Ca(2+) from Mg(2+) purely from sequence is inherently difficult; the argument relies on family-level knowledge rather than de novo coordination-geometry prediction from sequence.",
    "The UniProt annotation (ECO:0000269) is backed by direct experimental evidence (crystallography and activity assays), not merely computational prediction.",
    "The reviewer-only evidence was absent from the evaluated model's input; the model must rely on sequence recognition and general knowledge."
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

**Accession:** `E6Y8B9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 78. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
"E6Y8B9"
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"PvS1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"PvSUB1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"SUB1 protease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25204226","source":"PubMed"}],"value":"Subtilase SUB1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38503166","source":"PubMed"}],"value":"3.4.21.62"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37428845","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38386597","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"38503166","source":"PubMed"}],"value":"Subtilisin-like protease 1"}}}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29108"},"evidences":[{"evidenceCode":"ECO:0000269","id":"25204226","source":"PubMed"}],"name":"Ca(2+)"}],"commentType":"COFACTOR"}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/references/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"citation":{"authors":["Giganti D.","Bouillon A.","Tawk L.","Robert F.","Martinez M.","Crublet E.","Weber P.","Girard-Blanc C.","Petres S.","Haouz A.","Hernandez J.F.","Mercereau-Puijalon O.","Alzari P.M.","Barale J.C."],"citationCrossReferences":[{"database":"PubMed","id":"25204226"},{"database":"DOI","id":"10.1038/ncomms5833"}],"citationType":"journal article","firstPage":"4833","id":"25204226","journal":"Nat. Commun.","lastPage":"4833","publicationDate":"2014","title":"A novel Plasmodium-specific prodomain fold regulates the malaria drug target SUB1 subtilase.","volume":"5"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4TR2","source":"PDB"}],"referenceNumber":5,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","SUBUNIT","PROTEOLYTIC CLEAVAGE","CLEAVAGE SITE","DISULFIDE BONDS"]}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"citation":{"authors":["Martinez M.","Batista F.A.","Maurel M.","Bouillon A.","Ortega Varga L.","Wehenkel A.M.","Le Chevalier-Sontag L.","Blondel A.","Haouz A.","Hernandez J.F.","Alzari P.M.","Barale J.C."],"citationCrossReferences":[{"database":"PubMed","id":"37428845"},{"database":"DOI","id":"10.1107/s2059798323004710"}],"citationType":"journal article","firstPage":"721","id":"37428845","journal":"Acta Crystallogr. D Struct. Biol.","lastPage":"734","publicationDate":"2023","title":"3D structures of the Plasmodium vivax subtilisin-like drug target SUB1 reveal conformational changes to accommodate a substrate-derived alpha-ketoamide inhibitor.","volume":"79"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8COY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8COZ","source":"PDB"}],"referenceNumber":6,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITOR","CATALYTIC ACTIVITY","ACTIVITY REGULATION","PROTEOLYTIC CLEAVAGE","GLYCOSYLATION","GLYCOSYLATION AT ASN-546","DISULFIDE BONDS","MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445"]}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E6Y8B9.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:01.366318+00:00.  

```json
{"citation":{"authors":["Legru A.","Batista F.A.","Puszko A.K.","Bouillon A.","Maurel M.","Martinez M.","Ejjoummany A.","Ortega Varga L.","Adler P.","Mechaly A.","Hadjadj M.","Sosnowski P.","Hopfgartner G.","Alzari P.M.","Blondel A.","Haouz A.","Barale J.C.","Hernandez J.F."],"citationCrossReferences":[{"database":"PubMed","id":"38503166"},{"database":"DOI","id":"10.1016/j.ejmech.2024.116308"}],"citationType":"journal article","firstPage":"116308","id":"38503166","journal":"Eur. J. Med. Chem.","lastPage":"116308","publicationDate":"2024","title":"Insights from structure-activity relationships and the binding mode of peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-like SUB1.","volume":"269"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8QKE","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"8QKG","source":"PDB"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND PEPTIDE INHIBITORS","CATALYTIC ACTIVITY","ACTIVITY REGULATION","GLYCOSYLATION AT ASN-546","DISULFIDE BONDS"]}
```

Source SHA-256: `e9b4af9865155585e28a933302308978b5c5a92dbbd9ce2df61bef40af1c012b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 50-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
RN   [5] {ECO:0007744|PDB:4TR2}
RP   X-RAY CRYSTALLOGRAPHY (2.70 ANGSTROMS) OF 26-630 IN COMPLEX WITH CALCIUM,
RP   CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION, SUBUNIT, PROTEOLYTIC
RP   CLEAVAGE, CLEAVAGE SITE, AND DISULFIDE BONDS.
RX   PubMed=25204226; DOI=10.1038/ncomms5833;
RA   Giganti D., Bouillon A., Tawk L., Robert F., Martinez M., Crublet E.,
RA   Weber P., Girard-Blanc C., Petres S., Haouz A., Hernandez J.F.,
RA   Mercereau-Puijalon O., Alzari P.M., Barale J.C.;
RT   "A novel Plasmodium-specific prodomain fold regulates the malaria drug
RT   target SUB1 subtilase.";
RL   Nat. Commun. 5:4833-4833(2014).
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 61-73`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
RN   [6] {ECO:0007744|PDB:8COY, ECO:0007744|PDB:8COZ}
RP   X-RAY CRYSTALLOGRAPHY (1.44 ANGSTROMS) OF 273-617 IN COMPLEX WITH CA(2+)
RP   AND PEPTIDE INHIBITOR, CATALYTIC ACTIVITY, ACTIVITY REGULATION, PROTEOLYTIC
RP   CLEAVAGE, GLYCOSYLATION, GLYCOSYLATION AT ASN-546, DISULFIDE BONDS, AND
RP   MUTAGENESIS OF ASN-361; ASN-432 AND ASN-445.
RX   PubMed=37428845; DOI=10.1107/s2059798323004710;
RA   Martinez M., Batista F.A., Maurel M., Bouillon A., Ortega Varga L.,
RA   Wehenkel A.M., Le Chevalier-Sontag L., Blondel A., Haouz A.,
RA   Hernandez J.F., Alzari P.M., Barale J.C.;
RT   "3D structures of the Plasmodium vivax subtilisin-like drug target SUB1
RT   reveal conformational changes to accommodate a substrate-derived alpha-
RT   ketoamide inhibitor.";
RL   Acta Crystallogr. D Struct. Biol. 79:721-734(2023).
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 74-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
RN   [7] {ECO:0007744|PDB:8QKE, ECO:0007744|PDB:8QKG}
RP   X-RAY CRYSTALLOGRAPHY (1.50 ANGSTROMS) OF 26-630 IN COMPLEX WITH CA(2+) AND
RP   PEPTIDE INHIBITORS, CATALYTIC ACTIVITY, ACTIVITY REGULATION, GLYCOSYLATION
RP   AT ASN-546, AND DISULFIDE BONDS.
RX   PubMed=38503166; DOI=10.1016/j.ejmech.2024.116308;
RA   Legru A., Batista F.A., Puszko A.K., Bouillon A., Maurel M., Martinez M.,
RA   Ejjoummany A., Ortega Varga L., Adler P., Mechaly A., Hadjadj M.,
RA   Sosnowski P., Hopfgartner G., Alzari P.M., Blondel A., Haouz A.,
RA   Barale J.C., Hernandez J.F.;
RT   "Insights from structure-activity relationships and the binding mode of
RT   peptidic alpha-ketoamide inhibitors of the malaria drug target subtilisin-
RT   like SUB1.";
RL   Eur. J. Med. Chem. 269:116308-116308(2024).
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E6Y8B9?format=txt&versions=78)  
**Locator:** `lines 98-100`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 78 / 1.  
**Retrieved:** 2026-11-02T04:28:06.789132+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Ca(2+); Xref=ChEBI:CHEBI:29108;
CC         Evidence={ECO:0000269|PubMed:25204226};
```

Source SHA-256: `8339b9ac9ad20c1f768a45190d5d148406d577b6def1d323a6b83af3754d12d0`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 91. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
