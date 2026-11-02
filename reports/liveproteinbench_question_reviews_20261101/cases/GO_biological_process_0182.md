# GO_biological_process_0182

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — fatty acid beta-oxidation

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. fatty acid beta-oxidation
B. DNA replication, synthesis of primer
C. nucleotide-binding oligomerization domain containing 2 signaling pathway
D. positive regulation of osteoclast proliferation
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

> The exact sequence match is annotated as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation. UniProt records this functional claim with experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned (IEA), so it should not be mistaken for experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a protein enzyme, while several distractors describe pathways associated with specific signaling or cell types, but the supplied sequence provides no clear general biological cue that identifies fatty acid beta-oxidation over the alternatives.


**Missing item-specific fact**

> The sequence's identity and function as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation.


**Reason**

> Distinguishing the correct process requires protein-specific functional identification, such as homology or an external annotation. The reviewer-only identity and annotations support the key but were not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein's documented function supports option A; the other choices are not supported by the supplied reviewer evidence.


### Important caveats

- The accession and functional annotations are reviewer-only; they are not input evidence for answerability.
- The GO annotation is computationally assigned, whereas the cited functional annotation carries experimental evidence; the underlying primary study was not independently evaluated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a protein enzyme, while several distractors describe pathways associated with specific signaling or cell types, but the supplied sequence provides no clear general biological cue that identifies fatty acid beta-oxidation over the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's identity and function as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation.",
    "reason": "Distinguishing the correct process requires protein-specific functional identification, such as homology or an external annotation. The reviewer-only identity and annotations support the key but were not supplied to the model."
  },
  "case_id": "GO_biological_process_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation. UniProt records this functional claim with experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned (IEA), so it should not be mistaken for experimental evidence."
  },
  "important_caveats": [
    "The accession and functional annotations are reviewer-only; they are not input evidence for answerability.",
    "The GO annotation is computationally assigned, whereas the cited functional annotation carries experimental evidence; the underlying primary study was not independently evaluated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's documented function supports option A; the other choices are not supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation. UniProt records this functional claim with experimental evidence (ECO:0000269); the GO cross-reference itself is computationally assigned (IEA), so it should not be mistaken for experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a protein enzyme, while several distractors describe pathways associated with specific signaling or cell types, but the supplied sequence provides no clear general biological cue that identifies fatty acid beta-oxidation over the alternatives.",
    "missing_item_specific_fact": "The sequence's identity and function as a dienoyl-CoA isomerase involved in fatty acid beta-oxidation.",
    "reason": "Distinguishing the correct process requires protein-specific functional identification, such as homology or an external annotation. The reviewer-only identity and annotations support the key but were not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein's documented function supports option A; the other choices are not supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The accession and functional annotations are reviewer-only; they are not input evidence for answerability.",
    "The GO annotation is computationally assigned, whereas the cited functional annotation carries experimental evidence; the underlying primary study was not independently evaluated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NCP4 (DCI1_PYRO7) is identified as Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (EC 5.3.3.21), a peroxisomal di-isomerase. The FUNCTION comment (ECO:0000269|PubMed:36774535, experimental evidence) explicitly states the protein is 'Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth.' The PATHWAY comment (also ECO:0000269, experimental) reads 'Lipid metabolism; fatty acid beta-oxidation.' The GO cross-reference GO:0006635 (fatty acid beta-oxidation) is annotated via IEA:UniPathway, but the underlying pathway assignment is grounded in experimental data from PubMed:36774535. The sequence match is confirmed (SHA-256 identical, 280 aa). The expected answer A is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is from Pyricularia oryzae, a filamentous fungus. Option C (NOD2 signaling pathway) and Option D (positive regulation of osteoclast proliferation) are mammalian-specific biological processes: NOD2 is a cytoplasmic innate immune receptor with NACHT and leucine-rich repeat domains found in mammals, and osteoclast biology is specific to vertebrate bone remodeling. A fungal protein cannot participate in either. Option B (DNA replication, synthesis of primer) requires primase-specific domains (zinc finger, OB-fold, or related motifs) and DNA-binding architecture, none of which are present in this 280-aa sequence. The sequence instead shows a hydrophobic N-terminal region consistent with peroxisomal/membrane association and lacks any nucleic-acid-binding or immune-signalling architecture. By elimination grounded in general biological knowledge (organism domain, domain architecture requirements), option A (fatty acid beta-oxidation) is the only viable choice.


**Missing item-specific fact**

> Positive identification of the specific enzyme class (dienoyl-CoA isomerase, EC 5.3.3.21) and its precise role in unsaturated fatty acid beta-oxidation from sequence alone would require knowledge of the specific catalytic motif or database lookup. However, the four-choice format allows elimination-based reasoning to reach A without this item-specific fact.


**Reason**

> The elimination of B, C, and D relies on general biological knowledge: C and D are mammalian-specific processes impossible for a fungal protein, and B requires primase domains clearly absent from the sequence. A is the sole remaining option. This constitutes a concrete biological argument from the supplied sequence and choices, not an item-specific annotation lookup. The positive mechanistic identification of the enzyme is weak from sequence alone, but the question is answerable through defensible elimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are mammalian-specific processes incompatible with a fungal protein, and B requires specific primase domains absent from the sequence. Only A remains viable. No ambiguity among the choices given the organism context and sequence features.


### Important caveats

- The GO annotation for fatty acid beta-oxidation (GO:0006635) carries an IEA evidence code (inferred from electronic annotation via UniPathway), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:36774535).
- The protein is a specialized dienoyl-CoA isomerase (EC 5.3.3.21), not one of the four core beta-oxidation enzymes; it handles unsaturated fatty acid intermediates. Positive sequence-based identification of this specific enzyme class is challenging, but the four-choice elimination is sufficient.
- The UniProt entry was first publicly released in June 2025; the exact author data-construction snapshot is unknown, though the historical record (entry version 50, released Jan 2026) contains the same functional annotations.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 280-aa sequence and the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is from Pyricularia oryzae, a filamentous fungus. Option C (NOD2 signaling pathway) and Option D (positive regulation of osteoclast proliferation) are mammalian-specific biological processes: NOD2 is a cytoplasmic innate immune receptor with NACHT and leucine-rich repeat domains found in mammals, and osteoclast biology is specific to vertebrate bone remodeling. A fungal protein cannot participate in either. Option B (DNA replication, synthesis of primer) requires primase-specific domains (zinc finger, OB-fold, or related motifs) and DNA-binding architecture, none of which are present in this 280-aa sequence. The sequence instead shows a hydrophobic N-terminal region consistent with peroxisomal/membrane association and lacks any nucleic-acid-binding or immune-signalling architecture. By elimination grounded in general biological knowledge (organism domain, domain architecture requirements), option A (fatty acid beta-oxidation) is the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the specific enzyme class (dienoyl-CoA isomerase, EC 5.3.3.21) and its precise role in unsaturated fatty acid beta-oxidation from sequence alone would require knowledge of the specific catalytic motif or database lookup. However, the four-choice format allows elimination-based reasoning to reach A without this item-specific fact.",
    "reason": "The elimination of B, C, and D relies on general biological knowledge: C and D are mammalian-specific processes impossible for a fungal protein, and B requires primase domains clearly absent from the sequence. A is the sole remaining option. This constitutes a concrete biological argument from the supplied sequence and choices, not an item-specific annotation lookup. The positive mechanistic identification of the enzyme is weak from sequence alone, but the question is answerable through defensible elimination."
  },
  "case_id": "GO_biological_process_0182",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) is identified as Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (EC 5.3.3.21), a peroxisomal di-isomerase. The FUNCTION comment (ECO:0000269|PubMed:36774535, experimental evidence) explicitly states the protein is 'Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth.' The PATHWAY comment (also ECO:0000269, experimental) reads 'Lipid metabolism; fatty acid beta-oxidation.' The GO cross-reference GO:0006635 (fatty acid beta-oxidation) is annotated via IEA:UniPathway, but the underlying pathway assignment is grounded in experimental data from PubMed:36774535. The sequence match is confirmed (SHA-256 identical, 280 aa). The expected answer A is well-supported."
  },
  "important_caveats": [
    "The GO annotation for fatty acid beta-oxidation (GO:0006635) carries an IEA evidence code (inferred from electronic annotation via UniPathway), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:36774535).",
    "The protein is a specialized dienoyl-CoA isomerase (EC 5.3.3.21), not one of the four core beta-oxidation enzymes; it handles unsaturated fatty acid intermediates. Positive sequence-based identification of this specific enzyme class is challenging, but the four-choice elimination is sufficient.",
    "The UniProt entry was first publicly released in June 2025; the exact author data-construction snapshot is unknown, though the historical record (entry version 50, released Jan 2026) contains the same functional annotations.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 280-aa sequence and the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are mammalian-specific processes incompatible with a fungal protein, and B requires specific primase domains absent from the sequence. Only A remains viable. No ambiguity among the choices given the organism context and sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0182",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7) is identified as Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase (EC 5.3.3.21), a peroxisomal di-isomerase. The FUNCTION comment (ECO:0000269|PubMed:36774535, experimental evidence) explicitly states the protein is 'Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth.' The PATHWAY comment (also ECO:0000269, experimental) reads 'Lipid metabolism; fatty acid beta-oxidation.' The GO cross-reference GO:0006635 (fatty acid beta-oxidation) is annotated via IEA:UniPathway, but the underlying pathway assignment is grounded in experimental data from PubMed:36774535. The sequence match is confirmed (SHA-256 identical, 280 aa). The expected answer A is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is from Pyricularia oryzae, a filamentous fungus. Option C (NOD2 signaling pathway) and Option D (positive regulation of osteoclast proliferation) are mammalian-specific biological processes: NOD2 is a cytoplasmic innate immune receptor with NACHT and leucine-rich repeat domains found in mammals, and osteoclast biology is specific to vertebrate bone remodeling. A fungal protein cannot participate in either. Option B (DNA replication, synthesis of primer) requires primase-specific domains (zinc finger, OB-fold, or related motifs) and DNA-binding architecture, none of which are present in this 280-aa sequence. The sequence instead shows a hydrophobic N-terminal region consistent with peroxisomal/membrane association and lacks any nucleic-acid-binding or immune-signalling architecture. By elimination grounded in general biological knowledge (organism domain, domain architecture requirements), option A (fatty acid beta-oxidation) is the only viable choice.",
    "missing_item_specific_fact": "Positive identification of the specific enzyme class (dienoyl-CoA isomerase, EC 5.3.3.21) and its precise role in unsaturated fatty acid beta-oxidation from sequence alone would require knowledge of the specific catalytic motif or database lookup. However, the four-choice format allows elimination-based reasoning to reach A without this item-specific fact.",
    "reason": "The elimination of B, C, and D relies on general biological knowledge: C and D are mammalian-specific processes impossible for a fungal protein, and B requires primase domains clearly absent from the sequence. A is the sole remaining option. This constitutes a concrete biological argument from the supplied sequence and choices, not an item-specific annotation lookup. The positive mechanistic identification of the enzyme is weak from sequence alone, but the question is answerable through defensible elimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are mammalian-specific processes incompatible with a fungal protein, and B requires specific primase domains absent from the sequence. Only A remains viable. No ambiguity among the choices given the organism context and sequence features."
  },
  "important_caveats": [
    "The GO annotation for fatty acid beta-oxidation (GO:0006635) carries an IEA evidence code (inferred from electronic annotation via UniPathway), but the underlying pathway assignment is supported by experimental evidence (ECO:0000269, PubMed:36774535).",
    "The protein is a specialized dienoyl-CoA isomerase (EC 5.3.3.21), not one of the four core beta-oxidation enzymes; it handles unsaturated fatty acid intermediates. Positive sequence-based identification of this specific enzyme class is challenging, but the four-choice elimination is sufficient.",
    "The UniProt entry was first publicly released in June 2025; the exact author data-construction snapshot is unknown, though the historical record (entry version 50, released Jan 2026) contains the same functional annotations.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on the 280-aa sequence and the four choices."
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

**Accession:** `G4NCP4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 50. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q08558","source":"UniProtKB"}],"value":"Peroxisomal di-isomerase DCI1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"36774535","source":"PubMed"}],"value":"5.3.3.21"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36774535","source":"PubMed"}],"value":"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase"}}}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"value":"Peroxisomal di-isomerase that is involved in fatty acid metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding 2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-oxidation, which is important for lipid droplets degradation and infectious growth (PubMed:36774535)"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36774535","source":"PubMed"}],"value":"Lipid metabolism; fatty acid beta-oxidation"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.351845+00:00.  

```json
{"database":"GO","id":"GO:0006635","properties":[{"key":"GoTerm","value":"P:fatty acid beta-oxidation"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniPathway"}]}
```

Source SHA-256: `18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 36-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- FUNCTION: Peroxisomal di-isomerase that is involved in fatty acid
CC       metabolism enzyme by converting 3,5-dienoyl-CoAs to the corresponding
CC       2,4-dienoyl-CoAs (PubMed:36774535). Involved in fatty acid beta-
CC       oxidation, which is important for lipid droplets degradation and
CC       infectious growth (PubMed:36774535). {ECO:0000269|PubMed:36774535}.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism; fatty acid beta-oxidation.
CC       {ECO:0000269|PubMed:36774535}.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-01T06:28:06.213875+00:00.  

```text
DR   GO; GO:0006635; P:fatty acid beta-oxidation; IEA:TreeGrafter.
```

Source SHA-256: `b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 68574-68586`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0006635
name: fatty acid beta-oxidation
namespace: biological_process
def: "A fatty acid oxidation process that results in the complete oxidation of a long-chain fatty acid. Fatty acid beta-oxidation begins with the addition of coenzyme A to a fatty acid, and occurs by successive cycles of reactions during each of which the fatty acid is shortened by a two-carbon fragment removed as acetyl coenzyme A; the cycle continues until only two or three carbons remain (as acetyl-CoA or propionyl-CoA respectively)." [GOC:mah, ISBN:0198506732]
xref: MetaCyc:PWY-5137
xref: MetaCyc:PWY-5138
xref: Reactome:R-HSA-77289 "Mitochondrial Fatty Acid Beta-Oxidation"
is_a: GO:0009062 ! fatty acid catabolic process
is_a: GO:0019395 ! fatty acid oxidation
property_value: skos:narrowMatch MetaCyc:PWY-5137
property_value: skos:narrowMatch MetaCyc:PWY-5138

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 182. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
