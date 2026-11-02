# pathway_0166

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **D** — Steroid biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSWPLIGAYALLAFVAIIALNVTYQFLFRLLNKTRPPLVFHWIPFIGSTIHYGMDPYGFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQTALEAHVPLIEKEVEDYLAMSPNFHGTSGEVDITAAMAEITIFTAGSALQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRNAGDNVPEKLDMIGNLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSISSWIMLRLASQPAVVEELYQEQLANLERTGPNNSLAPLQYKDFDNLPLHQNVIRETLRLNSSIHSLMRKVKNPLPVPGTPYVIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPKENDKDDIVDYGYGAISKGTSSPYLPFGAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDGQTGVPATDYSSLFSGPMKPARIRWERRAAKSG

[Multiple Choices]
A. L-histidine biosynthesis
B. Amino-acid degradation
C. chorismate biosynthesis
D. Steroid biosynthesis
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact matched sequence is annotated as sterol 14-alpha demethylase rstn2, with the pathway listed as steroid/sterol biosynthesis. The enzyme annotation cites experimental evidence, while the pathway annotation is transferred by similarity; this supports D without establishing that the pathway assignment itself was experimentally demonstrated for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region and sequence features may suggest a membrane-associated enzyme such as a cytochrome P450, but that broad inference does not distinguish steroid biosynthesis from other possible pathways for such enzymes.


**Missing item-specific fact**

> Identifying this particular protein as sterol 14-alpha demethylase rstn2, and knowing its sterol-biosynthesis role, is needed to select D.


**Reason**

> The sequence is provided without organism or functional annotation. The reviewer-only database match supports the key but is not information supplied to the evaluated model; recognizing the exact protein or its pathway requires an item-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> For the matched protein, the available annotation supports steroid/sterol biosynthesis, corresponding to D. The other options are not supported by the protein-specific evidence.


### Important caveats

- The reviewed historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.
- The pathway annotation is transferred by similarity (ECO:0000250); the cited experimental evidence for the enzyme annotation does not by itself establish direct experimental validation of the pathway assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region and sequence features may suggest a membrane-associated enzyme such as a cytochrome P450, but that broad inference does not distinguish steroid biosynthesis from other possible pathways for such enzymes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this particular protein as sterol 14-alpha demethylase rstn2, and knowing its sterol-biosynthesis role, is needed to select D.",
    "reason": "The sequence is provided without organism or functional annotation. The reviewer-only database match supports the key but is not information supplied to the evaluated model; recognizing the exact protein or its pathway requires an item-specific fact."
  },
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as sterol 14-alpha demethylase rstn2, with the pathway listed as steroid/sterol biosynthesis. The enzyme annotation cites experimental evidence, while the pathway annotation is transferred by similarity; this supports D without establishing that the pathway assignment itself was experimentally demonstrated for this protein."
  },
  "important_caveats": [
    "The reviewed historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is transferred by similarity (ECO:0000250); the cited experimental evidence for the enzyme annotation does not by itself establish direct experimental validation of the pathway assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the matched protein, the available annotation supports steroid/sterol biosynthesis, corresponding to D. The other options are not supported by the protein-specific evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matched sequence is annotated as sterol 14-alpha demethylase rstn2, with the pathway listed as steroid/sterol biosynthesis. The enzyme annotation cites experimental evidence, while the pathway annotation is transferred by similarity; this supports D without establishing that the pathway assignment itself was experimentally demonstrated for this protein.",
    "evidence_ids": ["C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region and sequence features may suggest a membrane-associated enzyme such as a cytochrome P450, but that broad inference does not distinguish steroid biosynthesis from other possible pathways for such enzymes.",
    "missing_item_specific_fact": "Identifying this particular protein as sterol 14-alpha demethylase rstn2, and knowing its sterol-biosynthesis role, is needed to select D.",
    "reason": "The sequence is provided without organism or functional annotation. The reviewer-only database match supports the key but is not information supplied to the evaluated model; recognizing the exact protein or its pathway requires an item-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "For the matched protein, the available annotation supports steroid/sterol biosynthesis, corresponding to D. The other options are not supported by the protein-specific evidence."
  },
  "important_caveats": [
    "The reviewed historical and current UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The pathway annotation is transferred by similarity (ECO:0000250); the cited experimental evidence for the enzyme annotation does not by itself establish direct experimental validation of the pathway assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H3) explicitly assigns this protein (A0A0L1JEW4, Sterol 14-alpha demethylase rstn2, EC 1.14.14.154) to 'Steroid biosynthesis; sterol biosynthesis.' The protein is a cytochrome P450 monooxygenase involved in ergosterol biosynthesis in Aspergillus nomiae. The EC number 1.14.14.154 corresponds to ergosterol 14-alpha demethylase activity, a key step in the sterol/ergosterol biosynthetic pathway. Note that the pathway annotation carries evidence code ECO:0000250 (similarity to Q4WNT5), indicating transfer by homology rather than direct experimental pathway assignment for this specific protein, though the functional characterization (CYP51 activity) was experimentally supported by PubMed 33857369.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable cytochrome P450 heme-binding region ('GAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDG' near the C-terminus, with the conserved heme-ligating Cys in the 'RCIG' motif) and an N-terminal hydrophobic membrane anchor typical of microsomal P450s. Among the four choices, only steroid/ergosterol biosynthesis is a well-known P450-dependent pathway in fungi (CYP51, CYP61, CYP512, etc.). Histidine biosynthesis (A), amino-acid degradation (B), and chorismate/shikimate biosynthesis (C) are not characteristically P450-dependent pathways. Thus, identifying the P450 fold and knowing fungal P450 pathway associations provides a valid reasoning chain to D.


**Missing item-specific fact**

> None strictly required. The P450 heme-binding motif is identifiable from the sequence, and the pathway association is general fungal biochemistry knowledge. However, recognizing the slightly non-canonical heme-binding motif variant in this fungal P450 requires specialized sequence knowledge.


**Reason**

> A model with knowledge of P450 structural motifs and fungal sterol biosynthesis can reason from the sequence features (membrane anchor, heme-binding Cys region, overall P450 domain architecture) to eliminate non-P450 pathways (A, B, C) and select D. This does not require memorizing this specific protein's UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given P450 identification, only steroid biosynthesis (D) is a P450-dependent pathway among the four choices. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis do not involve cytochrome P450 enzymes as a defining feature. No other option is defensible once the P450 identity is established.


### Important caveats

- The pathway annotation in UniProt uses evidence code ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is transferred by homology rather than directly experimentally proven for this specific protein.
- The protein is also described as part of the 'restricticin biosynthesis cluster,' a specialized natural product pathway. The UniProt pathway annotation places it under sterol biosynthesis because of its CYP51-like demethylase activity, but its biological role in the fungus may be in producing a CYP51 inhibitor (restricticin) rather than in primary ergosterol synthesis.
- The P450 heme-binding motif in this sequence is a slightly non-canonical variant of the FxxGxxxCxG pattern, which may make motif recognition less straightforward for some models.
- All reviewer-only evidence was absent from the evaluated model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding region ('GAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDG' near the C-terminus, with the conserved heme-ligating Cys in the 'RCIG' motif) and an N-terminal hydrophobic membrane anchor typical of microsomal P450s. Among the four choices, only steroid/ergosterol biosynthesis is a well-known P450-dependent pathway in fungi (CYP51, CYP61, CYP512, etc.). Histidine biosynthesis (A), amino-acid degradation (B), and chorismate/shikimate biosynthesis (C) are not characteristically P450-dependent pathways. Thus, identifying the P450 fold and knowing fungal P450 pathway associations provides a valid reasoning chain to D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The P450 heme-binding motif is identifiable from the sequence, and the pathway association is general fungal biochemistry knowledge. However, recognizing the slightly non-canonical heme-binding motif variant in this fungal P450 requires specialized sequence knowledge.",
    "reason": "A model with knowledge of P450 structural motifs and fungal sterol biosynthesis can reason from the sequence features (membrane anchor, heme-binding Cys region, overall P450 domain architecture) to eliminate non-P450 pathways (A, B, C) and select D. This does not require memorizing this specific protein's UniProt entry."
  },
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly assigns this protein (A0A0L1JEW4, Sterol 14-alpha demethylase rstn2, EC 1.14.14.154) to 'Steroid biosynthesis; sterol biosynthesis.' The protein is a cytochrome P450 monooxygenase involved in ergosterol biosynthesis in Aspergillus nomiae. The EC number 1.14.14.154 corresponds to ergosterol 14-alpha demethylase activity, a key step in the sterol/ergosterol biosynthetic pathway. Note that the pathway annotation carries evidence code ECO:0000250 (similarity to Q4WNT5), indicating transfer by homology rather than direct experimental pathway assignment for this specific protein, though the functional characterization (CYP51 activity) was experimentally supported by PubMed 33857369."
  },
  "important_caveats": [
    "The pathway annotation in UniProt uses evidence code ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is transferred by homology rather than directly experimentally proven for this specific protein.",
    "The protein is also described as part of the 'restricticin biosynthesis cluster,' a specialized natural product pathway. The UniProt pathway annotation places it under sterol biosynthesis because of its CYP51-like demethylase activity, but its biological role in the fungus may be in producing a CYP51 inhibitor (restricticin) rather than in primary ergosterol synthesis.",
    "The P450 heme-binding motif in this sequence is a slightly non-canonical variant of the FxxGxxxCxG pattern, which may make motif recognition less straightforward for some models.",
    "All reviewer-only evidence was absent from the evaluated model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given P450 identification, only steroid biosynthesis (D) is a P450-dependent pathway among the four choices. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis do not involve cytochrome P450 enzymes as a defining feature. No other option is defensible once the P450 identity is established."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0166",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H3) explicitly assigns this protein (A0A0L1JEW4, Sterol 14-alpha demethylase rstn2, EC 1.14.14.154) to 'Steroid biosynthesis; sterol biosynthesis.' The protein is a cytochrome P450 monooxygenase involved in ergosterol biosynthesis in Aspergillus nomiae. The EC number 1.14.14.154 corresponds to ergosterol 14-alpha demethylase activity, a key step in the sterol/ergosterol biosynthetic pathway. Note that the pathway annotation carries evidence code ECO:0000250 (similarity to Q4WNT5), indicating transfer by homology rather than direct experimental pathway assignment for this specific protein, though the functional characterization (CYP51 activity) was experimentally supported by PubMed 33857369.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable cytochrome P450 heme-binding region ('GAGRHRCIGEKFAYLNLAVIVATMVRHLRFSNLDG' near the C-terminus, with the conserved heme-ligating Cys in the 'RCIG' motif) and an N-terminal hydrophobic membrane anchor typical of microsomal P450s. Among the four choices, only steroid/ergosterol biosynthesis is a well-known P450-dependent pathway in fungi (CYP51, CYP61, CYP512, etc.). Histidine biosynthesis (A), amino-acid degradation (B), and chorismate/shikimate biosynthesis (C) are not characteristically P450-dependent pathways. Thus, identifying the P450 fold and knowing fungal P450 pathway associations provides a valid reasoning chain to D.",
    "missing_item_specific_fact": "None strictly required. The P450 heme-binding motif is identifiable from the sequence, and the pathway association is general fungal biochemistry knowledge. However, recognizing the slightly non-canonical heme-binding motif variant in this fungal P450 requires specialized sequence knowledge.",
    "reason": "A model with knowledge of P450 structural motifs and fungal sterol biosynthesis can reason from the sequence features (membrane anchor, heme-binding Cys region, overall P450 domain architecture) to eliminate non-P450 pathways (A, B, C) and select D. This does not require memorizing this specific protein's UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given P450 identification, only steroid biosynthesis (D) is a P450-dependent pathway among the four choices. Histidine biosynthesis, amino-acid degradation, and chorismate biosynthesis do not involve cytochrome P450 enzymes as a defining feature. No other option is defensible once the P450 identity is established."
  },
  "important_caveats": [
    "The pathway annotation in UniProt uses evidence code ECO:0000250 (similarity to Q4WNT5), meaning the pathway assignment is transferred by homology rather than directly experimentally proven for this specific protein.",
    "The protein is also described as part of the 'restricticin biosynthesis cluster,' a specialized natural product pathway. The UniProt pathway annotation places it under sterol biosynthesis because of its CYP51-like demethylase activity, but its biological role in the fungus may be in producing a CYP51 inhibitor (restricticin) rather than in primary ergosterol synthesis.",
    "The P450 heme-binding motif in this sequence is a slightly non-canonical variant of the FxxGxxxCxG pattern, which may make motif recognition less straightforward for some models.",
    "All reviewer-only evidence was absent from the evaluated model input."
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

**Accession:** `A0A0L1JEW4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Cytochrome P450 monooxygenase rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Ergosterol biosynthesis protein rstn2"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 2"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"1.14.14.154"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Sterol 14-alpha demethylase rstn2"}}}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/comments/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q4WNT5","source":"UniProtKB"}],"value":"Steroid biosynthesis; sterol biosynthesis"}]}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JEW4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:12.364317+00:00.  

```json
{"citation":{"authors":["Liu N.","Abramyan E.D.","Cheng W.","Perlatti B.","Harvey C.J.B.","Bills G.F.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33857369"},{"database":"DOI","id":"10.1021/jacs.1c01516"}],"citationType":"journal article","firstPage":"6043","id":"33857369","journal":"J. Am. Chem. Soc.","lastPage":"6047","publicationDate":"2021","title":"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.","volume":"143"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `d02dbb89f818b7eb87df130d530379b150615f58a7786d959f158367f6e7dbef`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 1-17`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
ID   RSTN2_ASPN3             Reviewed;         513 AA.
AC   A0A0L1JEW4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   11-NOV-2015, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Sterol 14-alpha demethylase rstn2 {ECO:0000303|PubMed:33857369};
DE            EC=1.14.14.154 {ECO:0000269|PubMed:33857369};
DE   AltName: Full=Cytochrome P450 monooxygenase rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Ergosterol biosynthesis protein rstn2 {ECO:0000303|PubMed:33857369};
DE   AltName: Full=Restricticin biosynthesis cluster protein 2 {ECO:0000303|PubMed:33857369};
GN   Name=rstn2 {ECO:0000303|PubMed:33857369}; ORFNames=ANOM_001443;
OS   Aspergillus nomiae NRRL (strain ATCC 15546 / NRRL 13137 / CBS 260.88 /
OS   M93).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=1509407;
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 26-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
RN   [2]
RP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.
RX   PubMed=33857369; DOI=10.1021/jacs.1c01516;
RA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,
RA   Tang Y.;
RT   "Targeted genome mining reveals the biosynthetic gene clusters of natural
RT   product CYP51 inhibitors.";
RL   J. Am. Chem. Soc. 143:6043-6047(2021).
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JEW4?format=txt&versions=38)  
**Locator:** `lines 166-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:14.653166+00:00.  

```text
CC   -!- PATHWAY: Steroid biosynthesis; sterol biosynthesis.
CC       {ECO:0000250|UniProtKB:Q4WNT5}.
```

Source SHA-256: `6c3d64c65d2f83b7569168450886015fb66b6ae6595088f32ba80d12e66f79e5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 166. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
