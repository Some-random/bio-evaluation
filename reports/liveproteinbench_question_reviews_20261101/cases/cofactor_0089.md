# cofactor_0089

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — heme b

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDTTLVEAGDPAEDAPEWPMKRDTGCPFDPPPGVRKLLAEKPLSRARIWDGSTPWVVTRHADQRALLSDPRVSHDGLRDGYPHISADFKFLSMAQPSFAGQDDPEHGRIRRMVTLPFTARRIEAMRPAIQKITDELIDGMLAGPKPVDLVEALALPVPVRVICEMLGVPYEDREFLQQNNNAMIYRDTAQGDAQKAAIAQAMYLKELVGTKLGDRGDDILSDLAVQVEAGEITQDDAAGIGMMLLGAGHETTANMIALGTLALLENPEQLAEVRDSDDPKVIVNTVEELLRYLTIAQDTVRRIAAEDIEIGGVVIKAGEGIVFPLNAANWDPDLYPEAPDRLDIHRANARRHLAFGYGVHQCLGATLARVELQIVYSTLLRRIPTLALAGTLDEIPFKHDQIAHGVYELPVTW

[Multiple Choices]
A. NAD(+)
B. Fe cation
C. heme b
D. Co(2+)
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

> The exact sequence matches the UniProt entry for cytochrome P450 GfsF. Its cofactor annotation names heme b with experimental and PDB evidence; the cited structure is a crystal structure in complex with heme b. This supports choice C for the supplied protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the characteristic cytochrome P450 heme-binding signature FxxGxxxCxG (in the segment FGYGVHQCLG). P450 enzymes use heme, and among the choices heme b is the appropriate complete cofactor; free Fe cation is not equivalent to the heme cofactor.


**Missing item-specific fact**

> No protein-specific annotation is necessary to distinguish the choices using the P450 sequence signature and standard P450 biology. The exact protein identity and direct heme-b evidence are reviewer-only corroboration.


**Reason**

> A recognizable sequence motif supports a meaningful biological inference to heme b, rather than selection requiring recall of this exact protein's database entry. The reviewer-only evidence confirms the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although heme b contains iron, the cofactor is the heme molecule, not an unbound iron cation; the options distinguish these.


### Important caveats

- The sequence match and supporting UniProt/PDB records establish evidence for this protein, but the exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the characteristic cytochrome P450 heme-binding signature FxxGxxxCxG (in the segment FGYGVHQCLG). P450 enzymes use heme, and among the choices heme b is the appropriate complete cofactor; free Fe cation is not equivalent to the heme cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish the choices using the P450 sequence signature and standard P450 biology. The exact protein identity and direct heme-b evidence are reviewer-only corroboration.",
    "reason": "A recognizable sequence motif supports a meaningful biological inference to heme b, rather than selection requiring recall of this exact protein's database entry. The reviewer-only evidence confirms the key but was not available to the evaluated model."
  },
  "case_id": "cofactor_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for cytochrome P450 GfsF. Its cofactor annotation names heme b with experimental and PDB evidence; the cited structure is a crystal structure in complex with heme b. This supports choice C for the supplied protein."
  },
  "important_caveats": [
    "The sequence match and supporting UniProt/PDB records establish evidence for this protein, but the exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although heme b contains iron, the cofactor is the heme molecule, not an unbound iron cation; the options distinguish these."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for cytochrome P450 GfsF. Its cofactor annotation names heme b with experimental and PDB evidence; the cited structure is a crystal structure in complex with heme b. This supports choice C for the supplied protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the characteristic cytochrome P450 heme-binding signature FxxGxxxCxG (in the segment FGYGVHQCLG). P450 enzymes use heme, and among the choices heme b is the appropriate complete cofactor; free Fe cation is not equivalent to the heme cofactor.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish the choices using the P450 sequence signature and standard P450 biology. The exact protein identity and direct heme-b evidence are reviewer-only corroboration.",
    "reason": "A recognizable sequence motif supports a meaningful biological inference to heme b, rather than selection requiring recall of this exact protein's database entry. The reviewer-only evidence confirms the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although heme b contains iron, the cofactor is the heme molecule, not an unbound iron cation; the options distinguish these."
  },
  "important_caveats": [
    "The sequence match and supporting UniProt/PDB records establish evidence for this protein, but the exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the cofactor as 'heme b' (ChEBI:CHEBI:60344), with evidence from experimental X-ray crystallography (PDB 5Y1I, 2.00 Å, complex WITH HEME B) and functional characterization (PubMed:28869713). The protein name itself ('Cytochrome P450') is consistent with heme b as the prosthetic group. The evidence is experimental (ECO:0000269 and ECO:0007744), not merely computational inference.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif 'FGxGxxxCxG' (visible as 'AFGYGVHQCLGATLAR' in the C-terminal region), which is the defining signature of the cytochrome P450 superfamily. All cytochrome P450 enzymes use heme b as their prosthetic group; the thiolate ligand (Cys) coordinates the iron center. This allows identification of the enzyme class from the sequence and deduction of its cofactor. Distractors are eliminable by general biochemistry: NAD(+) is a co-substrate for the P450 reductase partner, not the P450 cofactor; 'Fe cation' is a component of heme but not the cofactor itself; Co(2+) is irrelevant to P450 chemistry.


**Missing item-specific fact**

> None critical. While exact motif identification from a raw 414-aa sequence requires pattern recognition, the P450 heme-binding motif is a universally taught, general biochemical feature, not an item-specific annotation.


**Reason**

> A knowledgeable model can scan the sequence for the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and apply the general rule that all P450s require heme b. This is general biological reasoning, not memorization of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only heme b is the correct cofactor for a cytochrome P450. NAD(+) is a co-substrate for electron transfer, not a bound cofactor. Fe cation is a sub-component of heme but not the cofactor designation. Co(2+) has no role in P450 catalysis. No ambiguity exists among the four choices.


### Important caveats

- The UniProt entry was first public in Feb 2025; if the benchmark was constructed earlier, the author may have relied on PDB 5Y1I (2017) or PubMed:28869713 directly.
- Identifying the P450 motif from a raw sequence is feasible but non-trivial; a model without biochemistry training might miss the 'AFGYGVHQCLG' motif among 414 residues.
- The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning path relies on general P450 biochemistry knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif 'FGxGxxxCxG' (visible as 'AFGYGVHQCLGATLAR' in the C-terminal region), which is the defining signature of the cytochrome P450 superfamily. All cytochrome P450 enzymes use heme b as their prosthetic group; the thiolate ligand (Cys) coordinates the iron center. This allows identification of the enzyme class from the sequence and deduction of its cofactor. Distractors are eliminable by general biochemistry: NAD(+) is a co-substrate for the P450 reductase partner, not the P450 cofactor; 'Fe cation' is a component of heme but not the cofactor itself; Co(2+) is irrelevant to P450 chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While exact motif identification from a raw 414-aa sequence requires pattern recognition, the P450 heme-binding motif is a universally taught, general biochemical feature, not an item-specific annotation.",
    "reason": "A knowledgeable model can scan the sequence for the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and apply the general rule that all P450s require heme b. This is general biological reasoning, not memorization of a specific database entry."
  },
  "case_id": "cofactor_0089",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the cofactor as 'heme b' (ChEBI:CHEBI:60344), with evidence from experimental X-ray crystallography (PDB 5Y1I, 2.00 Å, complex WITH HEME B) and functional characterization (PubMed:28869713). The protein name itself ('Cytochrome P450') is consistent with heme b as the prosthetic group. The evidence is experimental (ECO:0000269 and ECO:0007744), not merely computational inference."
  },
  "important_caveats": [
    "The UniProt entry was first public in Feb 2025; if the benchmark was constructed earlier, the author may have relied on PDB 5Y1I (2017) or PubMed:28869713 directly.",
    "Identifying the P450 motif from a raw sequence is feasible but non-trivial; a model without biochemistry training might miss the 'AFGYGVHQCLG' motif among 414 residues.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning path relies on general P450 biochemistry knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only heme b is the correct cofactor for a cytochrome P450. NAD(+) is a co-substrate for electron transfer, not a bound cofactor. Fe cation is a sub-component of heme but not the cofactor designation. Co(2+) has no role in P450 catalysis. No ambiguity exists among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0089",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0D207 (Cytochrome P450 GfsF, Streptomyces halstedii) explicitly annotates the cofactor as 'heme b' (ChEBI:CHEBI:60344), with evidence from experimental X-ray crystallography (PDB 5Y1I, 2.00 Å, complex WITH HEME B) and functional characterization (PubMed:28869713). The protein name itself ('Cytochrome P450') is consistent with heme b as the prosthetic group. The evidence is experimental (ECO:0000269 and ECO:0007744), not merely computational inference.",
    "evidence_ids": ["C5", "C7", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif 'FGxGxxxCxG' (visible as 'AFGYGVHQCLGATLAR' in the C-terminal region), which is the defining signature of the cytochrome P450 superfamily. All cytochrome P450 enzymes use heme b as their prosthetic group; the thiolate ligand (Cys) coordinates the iron center. This allows identification of the enzyme class from the sequence and deduction of its cofactor. Distractors are eliminable by general biochemistry: NAD(+) is a co-substrate for the P450 reductase partner, not the P450 cofactor; 'Fe cation' is a component of heme but not the cofactor itself; Co(2+) is irrelevant to P450 chemistry.",
    "missing_item_specific_fact": "None critical. While exact motif identification from a raw 414-aa sequence requires pattern recognition, the P450 heme-binding motif is a universally taught, general biochemical feature, not an item-specific annotation.",
    "reason": "A knowledgeable model can scan the sequence for the FxxGxxxCxG heme-ligating motif, recognize the protein as a cytochrome P450, and apply the general rule that all P450s require heme b. This is general biological reasoning, not memorization of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only heme b is the correct cofactor for a cytochrome P450. NAD(+) is a co-substrate for electron transfer, not a bound cofactor. Fe cation is a sub-component of heme but not the cofactor designation. Co(2+) has no role in P450 catalysis. No ambiguity exists among the four choices."
  },
  "important_caveats": [
    "The UniProt entry was first public in Feb 2025; if the benchmark was constructed earlier, the author may have relied on PDB 5Y1I (2017) or PubMed:28869713 directly.",
    "Identifying the P450 motif from a raw sequence is feasible but non-trivial; a model without biochemistry training might miss the 'AFGYGVHQCLG' motif among 414 residues.",
    "The reviewer-only evidence confirms the key but was not available to the evaluated model; the reasoning path relies on general P450 biochemistry knowledge."
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

**Accession:** `E0D207` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 48. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
"E0D207"
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20589823","source":"PubMed"}],"value":"P450 monooxygenase GfsF"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20589823","source":"PubMed"}],"value":"1.14.-.-"}],"fullName":{"value":"Cytochrome P450 GfsF"}}}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:60344"},"evidences":[{"evidenceCode":"ECO:0000269","id":"28869713","source":"PubMed"},{"evidenceCode":"ECO:0007744","id":"5Y1I","source":"PDB"}],"name":"heme b"}],"commentType":"COFACTOR"}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"citation":{"authors":["Kudo F.","Motegi A.","Mizoue K.","Eguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"20589823"},{"database":"DOI","id":"10.1002/cbic.201000214"}],"citationType":"journal article","firstPage":"1574","id":"20589823","journal":"ChemBioChem","lastPage":"1582","publicationDate":"2010","title":"Cloning and characterization of the biosynthetic gene cluster of 16-membered macrolide antibiotic FD-891: involvement of a dual functional cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ16472.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"A-8890"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D207.json)  
**Locator:** `/references/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.759416+00:00.  

```json
{"citation":{"authors":["Miyanaga A.","Takayanagi R.","Furuya T.","Kawamata A.","Itagaki T.","Iwabuchi Y.","Kanoh N.","Kudo F.","Eguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"28869713"},{"database":"DOI","id":"10.1002/cbic.201700429"}],"citationType":"journal article","firstPage":"2179","id":"28869713","journal":"ChemBioChem","lastPage":"2187","publicationDate":"2017","title":"Substrate Recognition by a Dual-Function P450 Monooxygenase GfsF Involved in FD-891 Biosynthesis.","volume":"18"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5Y1I","source":"PDB"}],"referenceNumber":6,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 16-414 IN COMPLEX WITH HEME B","FUNCTION","SUBUNIT","MUTAGENESIS OF PHE-89 AND THR-300"]}
```

Source SHA-256: `dc5a5ddf81c1b51af907306ca972dbc709d4db40c846bfe03ce3ae8bd6cb3e37`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D207?format=txt&versions=48)  
**Locator:** `lines 54-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:27:56.758195+00:00.  

```text
RN   [6] {ECO:0007744|PDB:5Y1I}
RP   X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 16-414 IN COMPLEX WITH HEME B,
RP   FUNCTION, SUBUNIT, AND MUTAGENESIS OF PHE-89 AND THR-300.
RX   PubMed=28869713; DOI=10.1002/cbic.201700429;
RA   Miyanaga A., Takayanagi R., Furuya T., Kawamata A., Itagaki T.,
RA   Iwabuchi Y., Kanoh N., Kudo F., Eguchi T.;
RT   "Substrate Recognition by a Dual-Function P450 Monooxygenase GfsF Involved
RT   in FD-891 Biosynthesis.";
RL   ChemBioChem 18:2179-2187(2017).
```

Source SHA-256: `b7ff243274350eac91391be3b79c5530cd2a2ec42701fd8dc7b36bcbeb0f7237`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D207?format=txt&versions=48)  
**Locator:** `lines 75-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 48 / 1.  
**Retrieved:** 2026-11-02T04:27:56.758195+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=heme b; Xref=ChEBI:CHEBI:60344;
CC         Evidence={ECO:0000269|PubMed:28869713, ECO:0007744|PDB:5Y1I};
```

Source SHA-256: `b7ff243274350eac91391be3b79c5530cd2a2ec42701fd8dc7b36bcbeb0f7237`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 89. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
