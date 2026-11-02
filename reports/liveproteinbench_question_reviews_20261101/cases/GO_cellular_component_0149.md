# GO_cellular_component_0149

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nuclear membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKYTLEGSNARVIAKAVQSLSKVGKEMFIEIDQQSLQMRAINATQSAVGSISFKRSMFEVYDMPPHSDFYCKISMKGCLAVFRNMNEVEYCELNLLDNQTNLQVNLRCKLETTKEATISIIDDQNINTNINTDQMPNIIRGDHKLLTDISNNFNSSEEELTLEANSGSVVAKNYIEGARVNDKFMRTQLKLKPSEFEQYQVTKETVITFCIKEFRAFLLFAECLNASLTLEFDEAGMPFLLKIKKHGEIECLLIMSTLSPDDISFSEDYCQKDLTVQDEDVRAAAAKRKSSVSKPNVTNKRKGSSSEPAAVQPKRRVEETQLESSLDNPLFQFRDSEAPSVQHPRILAEVDTVVLIEDEAEQEALMLAAADAALEASMAPAPEPPNSTEVCFINTDDSQQPKPAKSSSDEDETIPQSPERPNKVLGVLLGLLQGCVSRLKTMLRLDEHLISGYELL

[Multiple Choices]
A. ribonucleoprotein complex
B. phosphopantothenoylcysteine decarboxylase complex
C. trans-Golgi network membrane
D. nuclear membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches the Drosophila Rad9 record. Its experimentally supported localization is the nuclear envelope, and the cited study specifically concerns localization to the nuclear membrane, supporting choice D. The evidence is a literature-based experimental annotation, not merely a computational prediction.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C10](#evidence-c10), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The basic sequence region may be consistent with nuclear targeting, but that does not establish localization at the nuclear membrane rather than elsewhere in the nucleus. The sequence provides no decisive membrane-localization signal.


**Missing item-specific fact**

> The protein-specific experimental finding that Drosophila Rad9 colocalizes with lamin at the nuclear periphery.


**Reason**

> Distinguishing the nuclear membrane option requires knowledge of Rad9's experimentally reported localization. General sequence reasoning does not establish that particular subcellular location.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The experimental nuclear-envelope localization supports D; the other choices describe unrelated complexes or a different organelle membrane. The nuclear membrane is a component of the nuclear envelope.


### Important caveats

- The cited annotation distinguishes isoforms: isoform A is reported at the nuclear envelope, while isoform B is reported in the nucleus.
- The reported targeting to the nuclear periphery can be disrupted by persistent double-strand-break DNA damage.
- The sequence matches the historical and current UniProt records, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The basic sequence region may be consistent with nuclear targeting, but that does not establish localization at the nuclear membrane rather than elsewhere in the nucleus. The sequence provides no decisive membrane-localization signal.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimental finding that Drosophila Rad9 colocalizes with lamin at the nuclear periphery.",
    "reason": "Distinguishing the nuclear membrane option requires knowledge of Rad9's experimentally reported localization. General sequence reasoning does not establish that particular subcellular location."
  },
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C10",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Rad9 record. Its experimentally supported localization is the nuclear envelope, and the cited study specifically concerns localization to the nuclear membrane, supporting choice D. The evidence is a literature-based experimental annotation, not merely a computational prediction."
  },
  "important_caveats": [
    "The cited annotation distinguishes isoforms: isoform A is reported at the nuclear envelope, while isoform B is reported in the nucleus.",
    "The reported targeting to the nuclear periphery can be disrupted by persistent double-strand-break DNA damage.",
    "The sequence matches the historical and current UniProt records, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental nuclear-envelope localization supports D; the other choices describe unrelated complexes or a different organelle membrane. The nuclear membrane is a component of the nuclear envelope."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the Drosophila Rad9 record. Its experimentally supported localization is the nuclear envelope, and the cited study specifically concerns localization to the nuclear membrane, supporting choice D. The evidence is a literature-based experimental annotation, not merely a computational prediction.",
    "evidence_ids": ["C5", "C8", "C10", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The basic sequence region may be consistent with nuclear targeting, but that does not establish localization at the nuclear membrane rather than elsewhere in the nucleus. The sequence provides no decisive membrane-localization signal.",
    "missing_item_specific_fact": "The protein-specific experimental finding that Drosophila Rad9 colocalizes with lamin at the nuclear periphery.",
    "reason": "Distinguishing the nuclear membrane option requires knowledge of Rad9's experimentally reported localization. General sequence reasoning does not establish that particular subcellular location."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The experimental nuclear-envelope localization supports D; the other choices describe unrelated complexes or a different organelle membrane. The nuclear membrane is a component of the nuclear envelope."
  },
  "important_caveats": [
    "The cited annotation distinguishes isoforms: isoform A is reported at the nuclear envelope, while isoform B is reported in the nucleus.",
    "The reported targeting to the nuclear periphery can be disrupted by persistent double-strand-break DNA damage.",
    "The sequence matches the historical and current UniProt records, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Drosophila melanogaster Rad9 (O96533), a 9-1-1 checkpoint clamp component. Isoform A (the canonical 456-AA sequence matching the input) is experimentally annotated to 'Nucleus envelope' (GO:0005635) with ECO:0000269 (PubMed:22666434), noting colocalization with lamin at the nuclear periphery. GO:0031965 'nuclear membrane' is defined as the lipid bilayers forming the nuclear envelope and is part_of GO:0005635. The supporting paper title explicitly uses 'nuclear membrane.' The annotation is experimental (EXP/IDA), not merely computational. While the UniProt comment uses 'Nucleus envelope' rather than the narrower 'nuclear membrane,' the experimental data (lamin colocalization at the periphery) and the paper title directly support the nuclear membrane as the primary localization.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [H2](#evidence-h2), [H3](#evidence-h3), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks signal peptides, transmembrane helices, or mitochondrial targeting sequences (eliminating C: trans-Golgi network membrane). It contains no recognizable RNA-binding domains such as RRM, KH, or zinc-knuckle motifs (arguing against A: ribonucleoprotein complex). It does not match the fold or active-site residues of phosphopantothenoylcysteine decarboxylase (eliminating B). The C-terminal region contains clusters of basic residues (e.g., KRKSSVSKPNVTNKRKGSSSEPAAVQPKRR) consistent with nuclear localization signals, and the protein's small size (~456 AA) and checkpoint-clamp fold are consistent with a nuclear DNA-repair-associated protein. Among the four choices, only D (nuclear membrane) is a nuclear compartment, making it the sole viable option after elimination.


**Missing item-specific fact**

> The specific experimental finding that Rad9 localizes to the nuclear periphery (rather than the nucleoplasm) is not derivable from sequence alone; however, since 'nucleus' is not offered as a competing option, this distinction does not affect the answerable question.


**Reason**

> The three distractors belong to functionally unrelated categories (RNA complex, CoA biosynthesis enzyme, secretory-pathway membrane) and can be eliminated by the absence of their defining sequence features. The remaining option D is the only nuclear compartment among the choices, and basic-region clusters provide positive sequence evidence for nuclear targeting. The reasoning path is achievable through general biological knowledge without memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct subcellular categories (RNP, cytoplasmic enzyme complex, secretory membrane, nuclear membrane). Only one is nuclear, and the sequence provides no features supporting the other three. No ambiguity among options is apparent.


### Important caveats

- The UniProt annotation uses 'Nucleus envelope' (GO:0005635) rather than the narrower 'Nuclear membrane' (GO:0031965). The paper title uses 'nuclear membrane,' and GO:0031965 is part_of GO:0005635, so the expected answer is consistent but slightly narrower than the primary UniProt annotation.
- Isoform B is annotated to 'Nucleus' (GO:0005634) without membrane specificity. The canonical 456-AA sequence corresponds to Isoform A, for which the nuclear-envelope annotation applies.
- The identity of the protein (Rad9, Drosophila) is not provided in the model input; the reviewer-only evidence confirms sequence match to O96533.
- The GO term 'nuclear membrane' (GO:0031965) is not directly annotated in UniProt for this entry; the annotation is to 'nuclear envelope' (GO:0005635). The mapping from envelope to membrane is supported by GO ontology structure (part_of) and the paper title.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks signal peptides, transmembrane helices, or mitochondrial targeting sequences (eliminating C: trans-Golgi network membrane). It contains no recognizable RNA-binding domains such as RRM, KH, or zinc-knuckle motifs (arguing against A: ribonucleoprotein complex). It does not match the fold or active-site residues of phosphopantothenoylcysteine decarboxylase (eliminating B). The C-terminal region contains clusters of basic residues (e.g., KRKSSVSKPNVTNKRKGSSSEPAAVQPKRR) consistent with nuclear localization signals, and the protein's small size (~456 AA) and checkpoint-clamp fold are consistent with a nuclear DNA-repair-associated protein. Among the four choices, only D (nuclear membrane) is a nuclear compartment, making it the sole viable option after elimination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental finding that Rad9 localizes to the nuclear periphery (rather than the nucleoplasm) is not derivable from sequence alone; however, since 'nucleus' is not offered as a competing option, this distinction does not affect the answerable question.",
    "reason": "The three distractors belong to functionally unrelated categories (RNA complex, CoA biosynthesis enzyme, secretory-pathway membrane) and can be eliminated by the absence of their defining sequence features. The remaining option D is the only nuclear compartment among the choices, and basic-region clusters provide positive sequence evidence for nuclear targeting. The reasoning path is achievable through general biological knowledge without memorizing this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C9",
      "C10",
      "H2",
      "H3",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster Rad9 (O96533), a 9-1-1 checkpoint clamp component. Isoform A (the canonical 456-AA sequence matching the input) is experimentally annotated to 'Nucleus envelope' (GO:0005635) with ECO:0000269 (PubMed:22666434), noting colocalization with lamin at the nuclear periphery. GO:0031965 'nuclear membrane' is defined as the lipid bilayers forming the nuclear envelope and is part_of GO:0005635. The supporting paper title explicitly uses 'nuclear membrane.' The annotation is experimental (EXP/IDA), not merely computational. While the UniProt comment uses 'Nucleus envelope' rather than the narrower 'nuclear membrane,' the experimental data (lamin colocalization at the periphery) and the paper title directly support the nuclear membrane as the primary localization."
  },
  "important_caveats": [
    "The UniProt annotation uses 'Nucleus envelope' (GO:0005635) rather than the narrower 'Nuclear membrane' (GO:0031965). The paper title uses 'nuclear membrane,' and GO:0031965 is part_of GO:0005635, so the expected answer is consistent but slightly narrower than the primary UniProt annotation.",
    "Isoform B is annotated to 'Nucleus' (GO:0005634) without membrane specificity. The canonical 456-AA sequence corresponds to Isoform A, for which the nuclear-envelope annotation applies.",
    "The identity of the protein (Rad9, Drosophila) is not provided in the model input; the reviewer-only evidence confirms sequence match to O96533.",
    "The GO term 'nuclear membrane' (GO:0031965) is not directly annotated in UniProt for this entry; the annotation is to 'nuclear envelope' (GO:0005635). The mapping from envelope to membrane is supported by GO ontology structure (part_of) and the paper title."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct subcellular categories (RNP, cytoplasmic enzyme complex, secretory membrane, nuclear membrane). Only one is nuclear, and the sequence provides no features supporting the other three. No ambiguity among options is apparent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Drosophila melanogaster Rad9 (O96533), a 9-1-1 checkpoint clamp component. Isoform A (the canonical 456-AA sequence matching the input) is experimentally annotated to 'Nucleus envelope' (GO:0005635) with ECO:0000269 (PubMed:22666434), noting colocalization with lamin at the nuclear periphery. GO:0031965 'nuclear membrane' is defined as the lipid bilayers forming the nuclear envelope and is part_of GO:0005635. The supporting paper title explicitly uses 'nuclear membrane.' The annotation is experimental (EXP/IDA), not merely computational. While the UniProt comment uses 'Nucleus envelope' rather than the narrower 'nuclear membrane,' the experimental data (lamin colocalization at the periphery) and the paper title directly support the nuclear membrane as the primary localization.",
    "evidence_ids": ["C5", "C8", "C9", "C10", "H2", "H3", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks signal peptides, transmembrane helices, or mitochondrial targeting sequences (eliminating C: trans-Golgi network membrane). It contains no recognizable RNA-binding domains such as RRM, KH, or zinc-knuckle motifs (arguing against A: ribonucleoprotein complex). It does not match the fold or active-site residues of phosphopantothenoylcysteine decarboxylase (eliminating B). The C-terminal region contains clusters of basic residues (e.g., KRKSSVSKPNVTNKRKGSSSEPAAVQPKRR) consistent with nuclear localization signals, and the protein's small size (~456 AA) and checkpoint-clamp fold are consistent with a nuclear DNA-repair-associated protein. Among the four choices, only D (nuclear membrane) is a nuclear compartment, making it the sole viable option after elimination.",
    "missing_item_specific_fact": "The specific experimental finding that Rad9 localizes to the nuclear periphery (rather than the nucleoplasm) is not derivable from sequence alone; however, since 'nucleus' is not offered as a competing option, this distinction does not affect the answerable question.",
    "reason": "The three distractors belong to functionally unrelated categories (RNA complex, CoA biosynthesis enzyme, secretory-pathway membrane) and can be eliminated by the absence of their defining sequence features. The remaining option D is the only nuclear compartment among the choices, and basic-region clusters provide positive sequence evidence for nuclear targeting. The reasoning path is achievable through general biological knowledge without memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct subcellular categories (RNP, cytoplasmic enzyme complex, secretory membrane, nuclear membrane). Only one is nuclear, and the sequence provides no features supporting the other three. No ambiguity among options is apparent."
  },
  "important_caveats": [
    "The UniProt annotation uses 'Nucleus envelope' (GO:0005635) rather than the narrower 'Nuclear membrane' (GO:0031965). The paper title uses 'nuclear membrane,' and GO:0031965 is part_of GO:0005635, so the expected answer is consistent but slightly narrower than the primary UniProt annotation.",
    "Isoform B is annotated to 'Nucleus' (GO:0005634) without membrane specificity. The canonical 456-AA sequence corresponds to Isoform A, for which the nuclear-envelope annotation applies.",
    "The identity of the protein (Rad9, Drosophila) is not provided in the model input; the reviewer-only evidence confirms sequence match to O96533.",
    "The GO term 'nuclear membrane' (GO:0031965) is not directly annotated in UniProt for this entry; the annotation is to 'nuclear envelope' (GO:0005635). The mapping from envelope to membrane is supported by GO ontology structure (part_of) and the paper title."
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

**Accession:** `O96533` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 171. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:20.443840+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","molecule":"Isoform A","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"value":"Colocalizes with lamin at the nuclear periphery (PubMed:22666434). Targets the other components of the 9-1-1 complex, Rad1 and Hus1-like to the nuclear periphery (PubMed:22666434). Targeting to the nuclear periphery is disrupted in the presence of persistent double stranded break DNA damage (PubMed:22666434)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"id":"SL-0178","value":"Nucleus envelope"}}]}
```

Source SHA-256: `bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)  
**Locator:** `/uniProtKBCrossReferences/37`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:20.443840+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"22666434","source":"PubMed"}],"id":"GO:0005635","properties":[{"key":"GoTerm","value":"C:nuclear envelope"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)  
**Locator:** `/uniProtKBCrossReferences/38`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:20.443840+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"22666434","source":"PubMed"}],"id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IDA:FlyBase"}]}
```

Source SHA-256: `bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O96533.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:20.443840+00:00.  

```json
{"citation":{"authors":["Kadir R.","Bakhrat A.","Tokarsky R.","Abdu U."],"citationCrossReferences":[{"database":"PubMed","id":"22666434"},{"database":"DOI","id":"10.1371/journal.pone.0038010"}],"citationType":"journal article","firstPage":"e38010","id":"22666434","journal":"PLoS ONE","lastPage":"e38010","publicationDate":"2012","title":"Localization of the Drosophila Rad9 protein to the nuclear membrane is regulated by the C-terminal region and is affected in the meiotic checkpoint.","volume":"7"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":8,"referencePositions":["FUNCTION","INTERACTION WITH RAD1 AND HUS1","SUBCELLULAR LOCATION","ALTERNATIVE SPLICING","DEVELOPMENTAL STAGE","NUCLEAR LOCALIZATION SIGNAL","MUTAGENESIS OF 287-LYS--LYS-289; 300-LYS--LYS-302 AND 314-LYS--ARG-316"]}
```

Source SHA-256: `bb99e71f5e8a793ade93b27d828f52cb97398645ffefb83e64700635ebcbf030`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)  
**Locator:** `lines 104-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:29:22.754069+00:00.  

```text
RN   [8] {ECO:0000305}
RP   FUNCTION, INTERACTION WITH RAD1 AND HUS1, SUBCELLULAR LOCATION, ALTERNATIVE
RP   SPLICING, DEVELOPMENTAL STAGE, NUCLEAR LOCALIZATION SIGNAL, AND MUTAGENESIS
RP   OF 287-LYS--LYS-289; 300-LYS--LYS-302 AND 314-LYS--ARG-316.
RX   PubMed=22666434; DOI=10.1371/journal.pone.0038010;
RA   Kadir R., Bakhrat A., Tokarsky R., Abdu U.;
RT   "Localization of the Drosophila Rad9 protein to the nuclear membrane is
RT   regulated by the C-terminal region and is affected in the meiotic
RT   checkpoint.";
RL   PLoS ONE 7:e38010-e38010(2012).
```

Source SHA-256: `382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)  
**Locator:** `lines 130-136`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:29:22.754069+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: [Isoform A]: Nucleus envelope
CC       {ECO:0000269|PubMed:22666434}. Note=Colocalizes with lamin at the
CC       nuclear periphery (PubMed:22666434). Targets the other components of
CC       the 9-1-1 complex, Rad1 and Hus1-like to the nuclear periphery
CC       (PubMed:22666434). Targeting to the nuclear periphery is disrupted in
CC       the presence of persistent double stranded break DNA damage
CC       (PubMed:22666434). {ECO:0000269|PubMed:22666434}.
```

Source SHA-256: `382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O96533?format=txt&versions=171)  
**Locator:** `lines 194-194`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 171 / 1.  
**Retrieved:** 2026-11-02T04:29:22.754069+00:00.  

```text
DR   GO; GO:0005635; C:nuclear envelope; IEA:UniProtKB-SubCell.
```

Source SHA-256: `382fa0ff4b386f2a325cd0f8b4b5cfa06539582a3119d8a8b62f942b38c935a2`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 181475-181483`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0031965
name: nuclear membrane
namespace: cellular_component
def: "Either of the lipid bilayers that surround the nucleus and form the nuclear envelope; excludes the intermembrane space." [GOC:mah, GOC:pz]
xref: NIF_Subcellular:sao1687101204
is_a: GO:0031090 ! organelle membrane
relationship: part_of GO:0005635 ! nuclear envelope

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
