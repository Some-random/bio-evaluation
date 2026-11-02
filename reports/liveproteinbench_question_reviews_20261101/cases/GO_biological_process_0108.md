# GO_biological_process_0108

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — proteolysis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRTVFIYACIISLVLRTIPAHNDLMSKEKENKEKDVHKIIEDLRFLEKVDAILENSNMTIDDVKADADAYNPDEDAPKEELNKIEMEKKKAEEEAKNSKKKILERYLLDEKKKKSLRLIVSENHATSPSFFEESLIQEDFMSFIQSKGEIVNLKNLKSMIIELNSDMTDKELEAYITLLKKKGAHVESDELVGADSIYVDIIKDAVKRGDTSINFKKMQSNMLEVENKTYEKLNNNLKKSKNSYKKSFFNDEYRNLQWGLDLARLDDAQEMITTNSVETTKICVIDSGIDYNHPDLKGNIYVNLNELNGKEGIDDDNNGIIDDIYGVNYVNNTGDPWDDHNHGSHVSGIISAIGNNSIGVVGVNPSSKLVICKALDDKKLGRLGNIFKCIDYCINKKVNIINGSFSFDEYSTIFSSTIEYLARLGILFVVSSSNCSHPPSSIPDITRCDLSVNSKYPSVLSTQYDNMVVVANLKKKINGEYDISINSFYSDIYCQVSAPGANIYSTASRGSYMELSGTSMAAPHVAGIASIILSINPDLTYKQVVNILKNSVVKLSSHKNKIAWGGYIDILNAVKNAISSKNSYIRFQGIRMWKSKKRN

[Multiple Choices]
A. positive regulation of transcription by RNA polymerase II
B. embryonic development via the syncytial blastoderm
C. proteolysis
D. angiogenesis
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

### Expected-answer support: supported

> The exact sequence matches the Plasmodium berghei SUB1 entry. Its annotation identifies it as a subtilisin-like protease, and cited experimental evidence reports proteolytic maturation of other proteins. The GO proteolysis annotation is computationally inferred, but the functional evidence independently supports choice C.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region and a downstream protease-like catalytic domain, including conserved catalytic-residue patterns consistent with a secreted subtilisin-family serine protease. That supports proteolysis over the transcriptional, syncytial-blastoderm, and angiogenesis choices.


**Missing item-specific fact**

> No exact accession or database annotation is necessary to distinguish the broad proteolysis choice; exact parasite-specific substrates and developmental roles would require external information.


**Reason**

> The sequence offers a defensible enzyme-family and catalytic-function inference, rather than requiring recognition of the exact database entry. The reviewer-only annotations corroborate the key but are not needed as input to the reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Proteolysis is the only listed option that fits the sequence-supported protease function. The other choices are substantially more specific or concern unrelated biological processes.


### Important caveats

- The identity and experimental functional evidence come from reviewer-only sources; they were not supplied to the evaluated model.
- The direct GO annotation for proteolysis is computationally inferred, while the cited functional annotation reports experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a downstream protease-like catalytic domain, including conserved catalytic-residue patterns consistent with a secreted subtilisin-family serine protease. That supports proteolysis over the transcriptional, syncytial-blastoderm, and angiogenesis choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No exact accession or database annotation is necessary to distinguish the broad proteolysis choice; exact parasite-specific substrates and developmental roles would require external information.",
    "reason": "The sequence offers a defensible enzyme-family and catalytic-function inference, rather than requiring recognition of the exact database entry. The reviewer-only annotations corroborate the key but are not needed as input to the reasoning."
  },
  "case_id": "GO_biological_process_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium berghei SUB1 entry. Its annotation identifies it as a subtilisin-like protease, and cited experimental evidence reports proteolytic maturation of other proteins. The GO proteolysis annotation is computationally inferred, but the functional evidence independently supports choice C."
  },
  "important_caveats": [
    "The identity and experimental functional evidence come from reviewer-only sources; they were not supplied to the evaluated model.",
    "The direct GO annotation for proteolysis is computationally inferred, while the cited functional annotation reports experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Proteolysis is the only listed option that fits the sequence-supported protease function. The other choices are substantially more specific or concern unrelated biological processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Plasmodium berghei SUB1 entry. Its annotation identifies it as a subtilisin-like protease, and cited experimental evidence reports proteolytic maturation of other proteins. The GO proteolysis annotation is computationally inferred, but the functional evidence independently supports choice C.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region and a downstream protease-like catalytic domain, including conserved catalytic-residue patterns consistent with a secreted subtilisin-family serine protease. That supports proteolysis over the transcriptional, syncytial-blastoderm, and angiogenesis choices.",
    "missing_item_specific_fact": "No exact accession or database annotation is necessary to distinguish the broad proteolysis choice; exact parasite-specific substrates and developmental roles would require external information.",
    "reason": "The sequence offers a defensible enzyme-family and catalytic-function inference, rather than requiring recognition of the exact database entry. The reviewer-only annotations corroborate the key but are not needed as input to the reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Proteolysis is the only listed option that fits the sequence-supported protease function. The other choices are substantially more specific or concern unrelated biological processes."
  },
  "important_caveats": [
    "The identity and experimental functional evidence come from reviewer-only sources; they were not supplied to the evaluated model.",
    "The direct GO annotation for proteolysis is computationally inferred, while the cited functional annotation reports experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Plasmodium berghei Subtilisin-like protease 1 (PbSUB1, EC 3.4.21.62), experimentally confirmed (ECO:0000269, PubMed:23653352, 24089525, 24348254, 30941868) to mediate proteolytic maturation of SERA3 and MSP1. GO:0006508 (proteolysis) is assigned in the UniProt entry. The protein name, EC number, and function comments all confirm its primary molecular activity is proteolysis.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H6](#evidence-h6), [H7](#evidence-h7), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable subtilisin-family catalytic triad motifs: 'GADSIY' (catalytic Asp), 'HPDL' (catalytic His), and 'GSH' (catalytic Ser) — textbook signatures of S8 subtilisin-like serine proteases. Additionally, the distractors are eliminable by general biological reasoning: (B) 'embryonic development via the syncytial blastoderm' is a Drosophila-specific GO term inapplicable to a protozoan parasite; (D) angiogenesis is a vertebrate-specific process (blood vessel formation) with no analogue in Plasmodium; (A) positive regulation of Pol II transcription requires DNA-binding/transactivation domains absent from this sequence. The only option consistent with a secreted subtilisin-like protease is proteolysis.


**Missing item-specific fact**

> None critical. The catalytic triad motifs are identifiable from the raw sequence by standard protease-family biochemistry knowledge, and the organism context (protozoan) eliminates vertebrate- and insect-specific options.


**Reason**

> A biologist familiar with subtilisin catalytic motifs (GADSIY…HPD…GSH) can identify the protein as a serine protease from the sequence alone, and the three distractors are eliminable through general organismal and domain-level reasoning without needing to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (Drosophila-specific), D (vertebrate-specific), and A (transcription factor) are all clearly inapplicable to a protozoan subtilisin-like protease. Only C (proteolysis) is consistent with the enzyme's catalytic mechanism and molecular function.


### Important caveats

- The GO:0006508 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB-KW, not a direct experimental GO annotation; however, the underlying proteolytic function is experimentally validated (ECO:0000269).
- The protein also participates in higher-order biological processes (parasite egress, liver-stage development, gamete egress), but the question asks for the primary biological process, which for a protease is proteolysis.
- The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, though the historical archived version (entry v30, sequence matched) confirms the annotation was present before the benchmark cutoff.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable subtilisin-family catalytic triad motifs: 'GADSIY' (catalytic Asp), 'HPDL' (catalytic His), and 'GSH' (catalytic Ser) — textbook signatures of S8 subtilisin-like serine proteases. Additionally, the distractors are eliminable by general biological reasoning: (B) 'embryonic development via the syncytial blastoderm' is a Drosophila-specific GO term inapplicable to a protozoan parasite; (D) angiogenesis is a vertebrate-specific process (blood vessel formation) with no analogue in Plasmodium; (A) positive regulation of Pol II transcription requires DNA-binding/transactivation domains absent from this sequence. The only option consistent with a secreted subtilisin-like protease is proteolysis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The catalytic triad motifs are identifiable from the raw sequence by standard protease-family biochemistry knowledge, and the organism context (protozoan) eliminates vertebrate- and insect-specific options.",
    "reason": "A biologist familiar with subtilisin catalytic motifs (GADSIY…HPD…GSH) can identify the protein as a serine protease from the sequence alone, and the three distractors are eliminable through general organismal and domain-level reasoning without needing to recall this specific protein's database entry."
  },
  "case_id": "GO_biological_process_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H6",
      "H7",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The protein is Plasmodium berghei Subtilisin-like protease 1 (PbSUB1, EC 3.4.21.62), experimentally confirmed (ECO:0000269, PubMed:23653352, 24089525, 24348254, 30941868) to mediate proteolytic maturation of SERA3 and MSP1. GO:0006508 (proteolysis) is assigned in the UniProt entry. The protein name, EC number, and function comments all confirm its primary molecular activity is proteolysis."
  },
  "important_caveats": [
    "The GO:0006508 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB-KW, not a direct experimental GO annotation; however, the underlying proteolytic function is experimentally validated (ECO:0000269).",
    "The protein also participates in higher-order biological processes (parasite egress, liver-stage development, gamete egress), but the question asks for the primary biological process, which for a protease is proteolysis.",
    "The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, though the historical archived version (entry v30, sequence matched) confirms the annotation was present before the benchmark cutoff."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (Drosophila-specific), D (vertebrate-specific), and A (transcription factor) are all clearly inapplicable to a protozoan subtilisin-like protease. Only C (proteolysis) is consistent with the enzyme's catalytic mechanism and molecular function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Plasmodium berghei Subtilisin-like protease 1 (PbSUB1, EC 3.4.21.62), experimentally confirmed (ECO:0000269, PubMed:23653352, 24089525, 24348254, 30941868) to mediate proteolytic maturation of SERA3 and MSP1. GO:0006508 (proteolysis) is assigned in the UniProt entry. The protein name, EC number, and function comments all confirm its primary molecular activity is proteolysis.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H6", "H7", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable subtilisin-family catalytic triad motifs: 'GADSIY' (catalytic Asp), 'HPDL' (catalytic His), and 'GSH' (catalytic Ser) — textbook signatures of S8 subtilisin-like serine proteases. Additionally, the distractors are eliminable by general biological reasoning: (B) 'embryonic development via the syncytial blastoderm' is a Drosophila-specific GO term inapplicable to a protozoan parasite; (D) angiogenesis is a vertebrate-specific process (blood vessel formation) with no analogue in Plasmodium; (A) positive regulation of Pol II transcription requires DNA-binding/transactivation domains absent from this sequence. The only option consistent with a secreted subtilisin-like protease is proteolysis.",
    "missing_item_specific_fact": "None critical. The catalytic triad motifs are identifiable from the raw sequence by standard protease-family biochemistry knowledge, and the organism context (protozoan) eliminates vertebrate- and insect-specific options.",
    "reason": "A biologist familiar with subtilisin catalytic motifs (GADSIY…HPD…GSH) can identify the protein as a serine protease from the sequence alone, and the three distractors are eliminable through general organismal and domain-level reasoning without needing to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (Drosophila-specific), D (vertebrate-specific), and A (transcription factor) are all clearly inapplicable to a protozoan subtilisin-like protease. Only C (proteolysis) is consistent with the enzyme's catalytic mechanism and molecular function."
  },
  "important_caveats": [
    "The GO:0006508 annotation carries an IEA (Inferred from Electronic Annotation) evidence code via InterPro/UniProtKB-KW, not a direct experimental GO annotation; however, the underlying proteolytic function is experimentally validated (ECO:0000269).",
    "The protein also participates in higher-order biological processes (parasite egress, liver-stage development, gamete egress), but the question asks for the primary biological process, which for a protease is proteolysis.",
    "The UniProt entry was first publicly released on 2025-04-09; the author's source snapshot date is unknown, though the historical archived version (entry v30, sequence matched) confirms the annotation was present before the benchmark cutoff."
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

**Accession:** `A0A509AM03` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
"A0A509AM03"
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23653352","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"24089525","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"24348254","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"30941868","source":"PubMed"}],"value":"PbSUB1"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23653352","source":"PubMed"}],"value":"3.4.21.62"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24348254","source":"PubMed"}],"value":"Subtilisin-like protease 1"}}}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24089525","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"24348254","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"30941868","source":"PubMed"}],"value":"Mediates the proteolytic maturation of serine protease SERA3 (PubMed:24089525, PubMed:30941868). Mediates the proteolytic maturation of MSP1, and thereby may prime the parasite cell surface for invasion of fresh erythrocytes (PubMed:24089525, PubMed:24348254). Required for completion of the parasite pre-erythrocytic stages (PubMed:24348254). Required for hepatic schizont development and merozoite formation (PubMed:24348254). Required for the egress of the hepatic merozoites from the parasitophorous vacuole (PubMed:24089525). Required for parasite infectivity during blood stages (PubMed:24089525). Required for male gamete egress (PubMed:30941868)"}]}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"database":"GO","id":"GO:0006508","properties":[{"key":"GoTerm","value":"P:proteolysis"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM03.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.276162+00:00.  

```json
{"citation":{"authors":["Bouillon A.","Giganti D.","Benedet C.","Gorgette O.","Petres S.","Crublet E.","Girard-Blanc C.","Witkowski B.","Menard D.","Nilges M.","Mercereau-Puijalon O.","Stoven V.","Barale J.C."],"citationCrossReferences":[{"database":"PubMed","id":"23653352"},{"database":"DOI","id":"10.1074/jbc.m113.456764"}],"citationType":"journal article","firstPage":"18561","id":"23653352","journal":"J. Biol. Chem.","lastPage":"18573","publicationDate":"2013","title":"In Silico screening on the three-dimensional model of the Plasmodium vivax SUB1 protease leads to the validation of a novel anti-parasite compound.","volume":"288"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","PROTEOLYTIC CLEAVAGE","CLEAVAGE SITE"]}
```

Source SHA-256: `58189b21f52a9fa91fa2e6cfc2283bebb23b54839f051ab7a55f96582d49e7b5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)  
**Locator:** `lines 62-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.257005+00:00.  

```text
CC   -!- FUNCTION: Mediates the proteolytic maturation of serine protease SERA3
CC       (PubMed:24089525, PubMed:30941868). Mediates the proteolytic maturation
CC       of MSP1, and thereby may prime the parasite cell surface for invasion
CC       of fresh erythrocytes (PubMed:24089525, PubMed:24348254). Required for
CC       completion of the parasite pre-erythrocytic stages (PubMed:24348254).
CC       Required for hepatic schizont development and merozoite formation
CC       (PubMed:24348254). Required for the egress of the hepatic merozoites
CC       from the parasitophorous vacuole (PubMed:24089525). Required for
CC       parasite infectivity during blood stages (PubMed:24089525). Required
CC       for male gamete egress (PubMed:30941868). {ECO:0000269|PubMed:24089525,
CC       ECO:0000269|PubMed:24348254, ECO:0000269|PubMed:30941868}.
```

Source SHA-256: `c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM03?format=txt&versions=30)  
**Locator:** `lines 138-138`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.257005+00:00.  

```text
DR   GO; GO:0006508; P:proteolysis; IEA:UniProtKB-KW.
```

Source SHA-256: `c0f9a4e5e66e23741f96fa610fa30c4dfac008f0d5ae074d8b0834a351f4fc02`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 66871-66884`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0006508
name: proteolysis
namespace: biological_process
def: "The hydrolysis of proteins into smaller polypeptides and/or amino acids by cleavage of their peptide bonds." [GOC:bf, GOC:mah]
comment: This term was intentionally placed under 'protein metabolic process ; GO:0019538' rather than 'protein catabolic process ; GO:0030163' to cover all processes centered on breaking peptide bonds, including those involved in protein processing.
subset: goslim_chembl
subset: goslim_metagenomics
subset: goslim_pir
synonym: "ATP-dependent proteolysis" NARROW [GOC:mah]
synonym: "peptidolysis" EXACT []
xref: Wikipedia:Proteolysis
is_a: GO:0019538 ! protein metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
