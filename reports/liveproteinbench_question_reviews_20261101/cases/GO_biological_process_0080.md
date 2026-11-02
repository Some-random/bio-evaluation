# GO_biological_process_0080

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — proteolysis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | uncertain | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | uncertain | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRRAILLILTLTVGTSLAAGFSQKDTPINTRYRETPEEAAAREFKEHTAELPPLPDAHSDGWFDIYVDENYGKQPKILLDSLQIMPAPDGSIRYILNIRSDKGYDNLTAEGIFCARSSIGFGNGKLSSYKVFGYGDTVNSRWIQPRNAEWKPIGGTLGRNDALRAVLYQAFCEGGVPADTQGLVQRLKERAGRYAPSMKPHDK

[Multiple Choices]
A. iron import into the mitochondrion
B. DNA topological change
C. proteolysis
D. vascular endothelial growth factor signaling pathway
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

### Expected-answer support: uncertain

> The supplied evidence matches the sequence to a Neisseria protein described as a precursor, but provides no functional annotation or experimental result establishing proteolysis. The cited possible-subcellular-location reference does not establish that process. This leaves the key unresolved; lack of support here does not show it is false.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with export, making a secreted proteolytic role plausible; bacterial context also makes mitochondrial iron import and VEGF signaling unlikely. But these clues do not distinguish proteolysis from DNA topological change.


**Missing item-specific fact**

> A protein-specific functional annotation or experimental evidence identifying this protein’s biological process.


**Reason**

> The sequence and choices do not provide a reliable basis to choose between the plausible bacterial processes. Identifying the exact protein and recalling its function would depend on an external, item-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The supplied sequence/context does not establish either DNA topological change or proteolysis. Both remain possible, while the export-like N-terminus alone is not diagnostic of proteolysis.


### Important caveats

- The reviewer-only evidence identifies a sequence-matched Neisseria protein, but that identity and its database record were not provided to the evaluated model.
- The cited database and publication excerpts do not independently validate the author key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with export, making a secreted proteolytic role plausible; bacterial context also makes mitochondrial iron import and VEGF signaling unlikely. But these clues do not distinguish proteolysis from DNA topological change.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental evidence identifying this protein’s biological process.",
    "reason": "The sequence and choices do not provide a reliable basis to choose between the plausible bacterial processes. Identifying the exact protein and recalling its function would depend on an external, item-specific fact."
  },
  "case_id": "GO_biological_process_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "H2"
    ],
    "judgment": "cannot_determine",
    "reason": "The supplied evidence matches the sequence to a Neisseria protein described as a precursor, but provides no functional annotation or experimental result establishing proteolysis. The cited possible-subcellular-location reference does not establish that process. This leaves the key unresolved; lack of support here does not show it is false."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched Neisseria protein, but that identity and its database record were not provided to the evaluated model.",
    "The cited database and publication excerpts do not independently validate the author key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The supplied sequence/context does not establish either DNA topological change or proteolysis. Both remain possible, while the export-like N-terminus alone is not diagnostic of proteolysis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0080",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The supplied evidence matches the sequence to a Neisseria protein described as a precursor, but provides no functional annotation or experimental result establishing proteolysis. The cited possible-subcellular-location reference does not establish that process. This leaves the key unresolved; lack of support here does not show it is false.",
    "evidence_ids": ["C1", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with export, making a secreted proteolytic role plausible; bacterial context also makes mitochondrial iron import and VEGF signaling unlikely. But these clues do not distinguish proteolysis from DNA topological change.",
    "missing_item_specific_fact": "A protein-specific functional annotation or experimental evidence identifying this protein’s biological process.",
    "reason": "The sequence and choices do not provide a reliable basis to choose between the plausible bacterial processes. Identifying the exact protein and recalling its function would depend on an external, item-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The supplied sequence/context does not establish either DNA topological change or proteolysis. Both remain possible, while the export-like N-terminus alone is not diagnostic of proteolysis."
  },
  "important_caveats": [
    "The reviewer-only evidence identifies a sequence-matched Neisseria protein, but that identity and its database record were not provided to the evaluated model.",
    "The cited database and publication excerpts do not independently validate the author key."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: uncertain

> The protein Q5F9Y4 is explicitly named 'Cryptic neisserial protein 1' (Cnp1), indicating its function is not well characterized. The provided evidence shows only annotations for gene name and possible subcellular location (ECO:0000305, ECO:0000303). No protease catalytic motifs (Ser-His-Asp triad, HExxH metalloprotease motif, aspartic protease motifs) are evident in the 203-aa sequence. The 'Precursor' flag indicates the protein may be a substrate of processing, not an agent of proteolysis. The supplied evidence excerpts do not include GO annotations for this entry, so neither support nor contradiction of 'proteolysis' can be definitively established from the available data. However, the 'cryptic' designation and absence of any protease-like features in the sequence make the expected answer poorly supported by the evidence at hand.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Three options can be eliminated by general biological reasoning: (A) iron import into mitochondrion is impossible for Neisseria, a bacterium lacking mitochondria; (B) DNA topological change requires topoisomerase/gyrase motifs absent from this sequence; (D) VEGF signaling is a eukaryotic receptor-tyrosine-kinase pathway irrelevant to a bacterial protein. However, positively identifying 'proteolysis' for a protein explicitly designated 'cryptic' (function unknown) cannot be achieved from the sequence alone—no protease catalytic motifs are present.


**Missing item-specific fact**

> The specific UniProt/GO annotation assigning this particular protein to proteolysis (GO:0006508), or experimental evidence demonstrating its proteolytic activity, which is absent from both the sequence and the provided evidence excerpts. The protein's function is described as 'cryptic' in its very name.


**Reason**

> While elimination of A, B, and D is achievable through general biology (bacterium → no mitochondria, no eukaryotic signaling, no topoisomerase motifs), the positive selection of 'proteolysis' requires knowing the item-specific database annotation for this cryptic protein. The sequence itself provides no protease motifs or catalytic features to justify this assignment independently.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D are clearly inapplicable to a Neisseria gonorrhoeae protein by basic biological reasoning (bacterium, no mitochondria, no eukaryotic VEGF pathway, no topoisomerase motifs). Only C remains after elimination, so the question is not truly ambiguous in terms of distractor plausibility. However, the correctness of C itself is questionable given the protein's 'cryptic' designation.


### Important caveats

- The protein is explicitly named 'Cryptic neisserial protein 1,' strongly suggesting its function was unknown at the time of characterization.
- The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, very recently; the benchmark author's source snapshot is unknown.
- The 'Precursor' flag indicates the protein may be cleaved during maturation, but being a substrate of proteolysis is distinct from performing proteolysis.
- The provided evidence excerpts do not include the full GO annotation set for Q5F9Y4; a GO:0006508 annotation may or may not exist in the complete entry.
- The sequence-match confirms the protein identity but does not validate the functional annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three options can be eliminated by general biological reasoning: (A) iron import into mitochondrion is impossible for Neisseria, a bacterium lacking mitochondria; (B) DNA topological change requires topoisomerase/gyrase motifs absent from this sequence; (D) VEGF signaling is a eukaryotic receptor-tyrosine-kinase pathway irrelevant to a bacterial protein. However, positively identifying 'proteolysis' for a protein explicitly designated 'cryptic' (function unknown) cannot be achieved from the sequence alone—no protease catalytic motifs are present.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt/GO annotation assigning this particular protein to proteolysis (GO:0006508), or experimental evidence demonstrating its proteolytic activity, which is absent from both the sequence and the provided evidence excerpts. The protein's function is described as 'cryptic' in its very name.",
    "reason": "While elimination of A, B, and D is achievable through general biology (bacterium → no mitochondria, no eukaryotic signaling, no topoisomerase motifs), the positive selection of 'proteolysis' requires knowing the item-specific database annotation for this cryptic protein. The sequence itself provides no protease motifs or catalytic features to justify this assignment independently."
  },
  "case_id": "GO_biological_process_0080",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "cannot_determine",
    "reason": "The protein Q5F9Y4 is explicitly named 'Cryptic neisserial protein 1' (Cnp1), indicating its function is not well characterized. The provided evidence shows only annotations for gene name and possible subcellular location (ECO:0000305, ECO:0000303). No protease catalytic motifs (Ser-His-Asp triad, HExxH metalloprotease motif, aspartic protease motifs) are evident in the 203-aa sequence. The 'Precursor' flag indicates the protein may be a substrate of processing, not an agent of proteolysis. The supplied evidence excerpts do not include GO annotations for this entry, so neither support nor contradiction of 'proteolysis' can be definitively established from the available data. However, the 'cryptic' designation and absence of any protease-like features in the sequence make the expected answer poorly supported by the evidence at hand."
  },
  "important_caveats": [
    "The protein is explicitly named 'Cryptic neisserial protein 1,' strongly suggesting its function was unknown at the time of characterization.",
    "The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, very recently; the benchmark author's source snapshot is unknown.",
    "The 'Precursor' flag indicates the protein may be cleaved during maturation, but being a substrate of proteolysis is distinct from performing proteolysis.",
    "The provided evidence excerpts do not include the full GO annotation set for Q5F9Y4; a GO:0006508 annotation may or may not exist in the complete entry.",
    "The sequence-match confirms the protein identity but does not validate the functional annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly inapplicable to a Neisseria gonorrhoeae protein by basic biological reasoning (bacterium, no mitochondria, no eukaryotic VEGF pathway, no topoisomerase motifs). Only C remains after elimination, so the question is not truly ambiguous in terms of distractor plausibility. However, the correctness of C itself is questionable given the protein's 'cryptic' designation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0080",
  "expected_answer_check": {
    "judgment": "cannot_determine",
    "reason": "The protein Q5F9Y4 is explicitly named 'Cryptic neisserial protein 1' (Cnp1), indicating its function is not well characterized. The provided evidence shows only annotations for gene name and possible subcellular location (ECO:0000305, ECO:0000303). No protease catalytic motifs (Ser-His-Asp triad, HExxH metalloprotease motif, aspartic protease motifs) are evident in the 203-aa sequence. The 'Precursor' flag indicates the protein may be a substrate of processing, not an agent of proteolysis. The supplied evidence excerpts do not include GO annotations for this entry, so neither support nor contradiction of 'proteolysis' can be definitively established from the available data. However, the 'cryptic' designation and absence of any protease-like features in the sequence make the expected answer poorly supported by the evidence at hand.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Three options can be eliminated by general biological reasoning: (A) iron import into mitochondrion is impossible for Neisseria, a bacterium lacking mitochondria; (B) DNA topological change requires topoisomerase/gyrase motifs absent from this sequence; (D) VEGF signaling is a eukaryotic receptor-tyrosine-kinase pathway irrelevant to a bacterial protein. However, positively identifying 'proteolysis' for a protein explicitly designated 'cryptic' (function unknown) cannot be achieved from the sequence alone—no protease catalytic motifs are present.",
    "missing_item_specific_fact": "The specific UniProt/GO annotation assigning this particular protein to proteolysis (GO:0006508), or experimental evidence demonstrating its proteolytic activity, which is absent from both the sequence and the provided evidence excerpts. The protein's function is described as 'cryptic' in its very name.",
    "reason": "While elimination of A, B, and D is achievable through general biology (bacterium → no mitochondria, no eukaryotic signaling, no topoisomerase motifs), the positive selection of 'proteolysis' requires knowing the item-specific database annotation for this cryptic protein. The sequence itself provides no protease motifs or catalytic features to justify this assignment independently."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D are clearly inapplicable to a Neisseria gonorrhoeae protein by basic biological reasoning (bacterium, no mitochondria, no eukaryotic VEGF pathway, no topoisomerase motifs). Only C remains after elimination, so the question is not truly ambiguous in terms of distractor plausibility. However, the correctness of C itself is questionable given the protein's 'cryptic' designation."
  },
  "important_caveats": [
    "The protein is explicitly named 'Cryptic neisserial protein 1,' strongly suggesting its function was unknown at the time of characterization.",
    "The UniProt entry was only integrated into Swiss-Prot on 2025-06-18, very recently; the benchmark author's source snapshot is unknown.",
    "The 'Precursor' flag indicates the protein may be cleaved during maturation, but being a substrate of proteolysis is distinct from performing proteolysis.",
    "The provided evidence excerpts do not include the full GO annotation set for Q5F9Y4; a GO:0006508 annotation may or may not exist in the complete entry.",
    "The sequence-match confirms the protein identity but does not validate the functional annotation."
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

**Accession:** `Q5F9Y4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 69. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F9Y4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:13.224939+00:00.  

```json
"Q5F9Y4"
```

Source SHA-256: `c89af3196822eefd98375ed9491fb32d38d06e18363f92b8d8f182bcf9d03afd`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F9Y4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:13.224939+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Betaproteobacteria","Neisseriales","Neisseriaceae","Neisseria"],"scientificName":"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)","taxonId":242231}
```

Source SHA-256: `c89af3196822eefd98375ed9491fb32d38d06e18363f92b8d8f182bcf9d03afd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F9Y4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:13.224939+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"1541538","source":"PubMed"}],"value":"Cryptic neisserial protein 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"1541538","source":"PubMed"}],"value":"Cnp1"}]}}
```

Source SHA-256: `c89af3196822eefd98375ed9491fb32d38d06e18363f92b8d8f182bcf9d03afd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F9Y4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:13.224939+00:00.  

```json
{"citation":{"authors":["Seifert H.S.","Wilson D."],"citationCrossReferences":[{"database":"PubMed","id":"1541538"},{"database":"DOI","id":"10.1128/iai.60.3.1232-1236.1992"}],"citationType":"journal article","firstPage":"1232","id":"1541538","journal":"Infect. Immun.","lastPage":"1236","publicationDate":"1992","title":"Characterization of a cryptic gene pair from Neisseria gonorrhoeae that is common to pathogenic Neisseria species.","volume":"60"},"referenceComments":[{"type":"STRAIN","value":"MS11"}],"referenceNumber":2,"referencePositions":["POSSIBLE SUBCELLULAR LOCATION"]}
```

Source SHA-256: `c89af3196822eefd98375ed9491fb32d38d06e18363f92b8d8f182bcf9d03afd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F9Y4?format=txt&versions=69)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:17.396618+00:00.  

```text
ID   CNP1_NEIG1              Reviewed;         203 AA.
AC   Q5F9Y4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-MAR-2005, sequence version 1.
DT   28-JAN-2026, entry version 69.
DE   RecName: Full=Cryptic neisserial protein 1 {ECO:0000305|PubMed:1541538};
DE            Short=Cnp1 {ECO:0000305|PubMed:1541538};
DE   Flags: Precursor;
GN   Name=cnp1 {ECO:0000303|PubMed:1541538, ECO:0000303|PubMed:8144473};
GN   ORFNames=NGO_0250 {ECO:0000312|EMBL:AAW89003.1};
OS   Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;
OC   Neisseriaceae; Neisseria.
OX   NCBI_TaxID=242231;
```

Source SHA-256: `5f22a6bcb154d8b6bffc1a0f41ba4606fdcc6c154e56196ad6e6aca6b2da9f1b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F9Y4?format=txt&versions=69)  
**Locator:** `lines 24-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:17.396618+00:00.  

```text
RN   [2]
RP   POSSIBLE SUBCELLULAR LOCATION.
RC   STRAIN=MS11;
RX   PubMed=1541538; DOI=10.1128/iai.60.3.1232-1236.1992;
RA   Seifert H.S., Wilson D.;
RT   "Characterization of a cryptic gene pair from Neisseria gonorrhoeae that is
RT   common to pathogenic Neisseria species.";
RL   Infect. Immun. 60:1232-1236(1992).
```

Source SHA-256: `5f22a6bcb154d8b6bffc1a0f41ba4606fdcc6c154e56196ad6e6aca6b2da9f1b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F9Y4?format=txt&versions=69)  
**Locator:** `lines 32-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:31:17.396618+00:00.  

```text
RN   [3]
RP   GENE NAME.
RC   STRAIN=ATCC 700825 / FA 1090;
RX   PubMed=8144473; DOI=10.1128/jb.176.7.2055-2060.1994;
RA   Dempsey J.A., Cannon J.G.;
RT   "Locations of genetic markers on the physical map of the chromosome of
RT   Neisseria gonorrhoeae FA1090.";
RL   J. Bacteriol. 176:2055-2060(1994).
```

Source SHA-256: `5f22a6bcb154d8b6bffc1a0f41ba4606fdcc6c154e56196ad6e6aca6b2da9f1b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 80. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
