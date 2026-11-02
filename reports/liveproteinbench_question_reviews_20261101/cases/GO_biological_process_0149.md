# GO_biological_process_0149

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — carbohydrate derivative metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLNDYLQWEKFILRGVEFPTRYRVDGDEVEITPSSRLYVSGMGGSGVVGDLIRDFSIVWNWDVEVTVVKDYFLRARDGLLIAVSYSGNTVETLYSVEYAKKRRIPTVAITTGGKLAQMGVPTIIIPKASAPRAALPQMLTAALHVVRKVYGIPIEIPEALEPPNDPLIHKLMEDFQKRPTIVAPETMRGVAYRVKNEFNENAKIEPSVEILPEAHHNWIEGSERPIVALTSPHIPREHQERVKATLEILGGTLYVVEMSTRGVLTFLREVGVASIKLAESRGVNPLATPRIEALKRRLQ

[Multiple Choices]
A. carbohydrate derivative metabolic process
B. calcium ion homeostasis
C. positive regulation of secondary metabolite biosynthetic process
D. positive regulation of signal transduction
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

> The exact sequence matches the UniProt protein identified as a bifunctional phosphoglucose/phosphomannose isomerase. Its annotated function is to isomerize glucose-6-phosphate and mannose-6-phosphate, supporting carbohydrate derivative metabolism. UniProt cites experimental evidence for the function; the GO annotation itself is IEA:InterPro, a computational annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> If the enzyme is identified as a phosphoglucose/phosphomannose isomerase, its transformations of phosphorylated sugars clearly support option A over the unrelated regulatory and calcium-homeostasis choices.


**Missing item-specific fact**

> The input does not identify the sequence as a phosphoglucose/phosphomannose isomerase or provide its substrate and reaction information; that protein-specific functional identification is needed to distinguish the process.


**Reason**

> The sequence alone supplies no clear, generally interpretable feature establishing this enzyme's substrates or biological role. Selecting A therefore depends on recognizing or looking up the protein's function, not merely on broad reasoning from the provided context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the protein's supported isomerase function, carbohydrate derivative metabolic process is the only listed choice that directly describes its activity.


### Important caveats

- The sequence match and associated accession are reviewer-only evidence and were not supplied to the evaluated model.
- The GO annotation is computational (IEA:InterPro); the cited UniProt functional annotation reports experimental evidence, but the primary study was not independently reviewed here.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "If the enzyme is identified as a phosphoglucose/phosphomannose isomerase, its transformations of phosphorylated sugars clearly support option A over the unrelated regulatory and calcium-homeostasis choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The input does not identify the sequence as a phosphoglucose/phosphomannose isomerase or provide its substrate and reaction information; that protein-specific functional identification is needed to distinguish the process.",
    "reason": "The sequence alone supplies no clear, generally interpretable feature establishing this enzyme's substrates or biological role. Selecting A therefore depends on recognizing or looking up the protein's function, not merely on broad reasoning from the provided context."
  },
  "case_id": "GO_biological_process_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt protein identified as a bifunctional phosphoglucose/phosphomannose isomerase. Its annotated function is to isomerize glucose-6-phosphate and mannose-6-phosphate, supporting carbohydrate derivative metabolism. UniProt cites experimental evidence for the function; the GO annotation itself is IEA:InterPro, a computational annotation."
  },
  "important_caveats": [
    "The sequence match and associated accession are reviewer-only evidence and were not supplied to the evaluated model.",
    "The GO annotation is computational (IEA:InterPro); the cited UniProt functional annotation reports experimental evidence, but the primary study was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein's supported isomerase function, carbohydrate derivative metabolic process is the only listed choice that directly describes its activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt protein identified as a bifunctional phosphoglucose/phosphomannose isomerase. Its annotated function is to isomerize glucose-6-phosphate and mannose-6-phosphate, supporting carbohydrate derivative metabolism. UniProt cites experimental evidence for the function; the GO annotation itself is IEA:InterPro, a computational annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "If the enzyme is identified as a phosphoglucose/phosphomannose isomerase, its transformations of phosphorylated sugars clearly support option A over the unrelated regulatory and calcium-homeostasis choices.",
    "missing_item_specific_fact": "The input does not identify the sequence as a phosphoglucose/phosphomannose isomerase or provide its substrate and reaction information; that protein-specific functional identification is needed to distinguish the process.",
    "reason": "The sequence alone supplies no clear, generally interpretable feature establishing this enzyme's substrates or biological role. Selecting A therefore depends on recognizing or looking up the protein's function, not merely on broad reasoning from the provided context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the protein's supported isomerase function, carbohydrate derivative metabolic process is the only listed choice that directly describes its activity."
  },
  "important_caveats": [
    "The sequence match and associated accession are reviewer-only evidence and were not supplied to the evaluated model.",
    "The GO annotation is computational (IEA:InterPro); the cited UniProt functional annotation reports experimental evidence, but the primary study was not independently reviewed here.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A3MTR6) annotates this protein with GO:1901135 (carbohydrate derivative metabolic process) via IEA:InterPro. The experimentally characterized function (PubMed:39208883, ECO:0000269) confirms it is a bifunctional phosphoglucose/phosphomannose isomerase catalyzing isomerization of glucose-6-phosphate and mannose-6-phosphate to fructose-6-phosphate. These substrates and products are phosphorylated sugars (carbohydrate derivatives), making the GO term biologically accurate. The GO term assignment itself is computational (IEA:InterPro), but the underlying biochemical function is experimentally validated and unambiguously falls within carbohydrate derivative metabolism.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~299 aa) contains glycine-rich motifs (e.g., 'SGGMGGSGVVGDL', 'GGKLAQMG') suggestive of nucleotide/cofactor-binding folds common in metabolic enzymes. Critically, the sequence lacks EF-hand or calcium-binding motifs (eliminating B: calcium ion homeostasis), lacks DNA-binding/transcriptional regulatory domains or protein-protein interaction modules typical of biosynthetic pathway regulators (eliminating C: positive regulation of secondary metabolite biosynthetic process), and lacks kinase domains, SH2/SH3 adaptors, transmembrane segments, or other signaling architectures (eliminating D: positive regulation of signal transduction). By elimination, the protein is a metabolic enzyme, and among the four options, 'carbohydrate derivative metabolic process' is the only one consistent with a small-molecule isomerase acting on phosphorylated sugars.


**Missing item-specific fact**

> Precisely recognizing the specific fold as phosphoglucose/phosphomannose isomerase (rather than, say, a generic dehydrogenase or transferase) would require either database lookup or recognition of the archaeal bifunctional PGI/PMI fold, which is not trivially deducible from primary sequence alone. However, the elimination of the three clearly wrong distractors is achievable through domain-level reasoning.


**Reason**

> Three of the four distractors describe regulatory, signaling, or ion-homeostasis functions that require specific structural domains (EF-hands, kinase domains, transcription factor motifs) entirely absent from this sequence. The remaining option (A) is a broad metabolic process category consistent with the glycine-rich nucleotide-binding-like motifs and the absence of any regulatory architecture. While positively identifying the exact enzyme class is lookup-assisted, the elimination-based reasoning is biologically sound and does not require memorizing this particular UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The other three options (B, C, D) describe fundamentally different protein classes (ion transporters/channels, transcriptional regulators, signaling components) with no structural or functional overlap with a small-molecule isomerase. No reasonable biological argument supports choosing any of them for this sequence.


### Important caveats

- The GO:1901135 annotation is IEA:InterPro (computational), not directly experimental, though the underlying catalytic activity is experimentally confirmed (ECO:0000269).
- The protein is also annotated with GO:0005975 (carbohydrate metabolic process), a parent term; the question's option A (carbohydrate derivative metabolic process) is the more specific child term and is the one annotated.
- The protein was first publicly annotated in UniProt on 2025-02-05, and its experimental characterization was published in 2024; the benchmark's author snapshot date is unknown, so the annotation available at question-creation time may have differed.
- The sequence-match is confirmed (SHA-256 identical across current and historical snapshots), so the annotation applies to the exact sequence provided.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~299 aa) contains glycine-rich motifs (e.g., 'SGGMGGSGVVGDL', 'GGKLAQMG') suggestive of nucleotide/cofactor-binding folds common in metabolic enzymes. Critically, the sequence lacks EF-hand or calcium-binding motifs (eliminating B: calcium ion homeostasis), lacks DNA-binding/transcriptional regulatory domains or protein-protein interaction modules typical of biosynthetic pathway regulators (eliminating C: positive regulation of secondary metabolite biosynthetic process), and lacks kinase domains, SH2/SH3 adaptors, transmembrane segments, or other signaling architectures (eliminating D: positive regulation of signal transduction). By elimination, the protein is a metabolic enzyme, and among the four options, 'carbohydrate derivative metabolic process' is the only one consistent with a small-molecule isomerase acting on phosphorylated sugars.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precisely recognizing the specific fold as phosphoglucose/phosphomannose isomerase (rather than, say, a generic dehydrogenase or transferase) would require either database lookup or recognition of the archaeal bifunctional PGI/PMI fold, which is not trivially deducible from primary sequence alone. However, the elimination of the three clearly wrong distractors is achievable through domain-level reasoning.",
    "reason": "Three of the four distractors describe regulatory, signaling, or ion-homeostasis functions that require specific structural domains (EF-hands, kinase domains, transcription factor motifs) entirely absent from this sequence. The remaining option (A) is a broad metabolic process category consistent with the glycine-rich nucleotide-binding-like motifs and the absence of any regulatory architecture. While positively identifying the exact enzyme class is lookup-assisted, the elimination-based reasoning is biologically sound and does not require memorizing this particular UniProt entry."
  },
  "case_id": "GO_biological_process_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A3MTR6) annotates this protein with GO:1901135 (carbohydrate derivative metabolic process) via IEA:InterPro. The experimentally characterized function (PubMed:39208883, ECO:0000269) confirms it is a bifunctional phosphoglucose/phosphomannose isomerase catalyzing isomerization of glucose-6-phosphate and mannose-6-phosphate to fructose-6-phosphate. These substrates and products are phosphorylated sugars (carbohydrate derivatives), making the GO term biologically accurate. The GO term assignment itself is computational (IEA:InterPro), but the underlying biochemical function is experimentally validated and unambiguously falls within carbohydrate derivative metabolism."
  },
  "important_caveats": [
    "The GO:1901135 annotation is IEA:InterPro (computational), not directly experimental, though the underlying catalytic activity is experimentally confirmed (ECO:0000269).",
    "The protein is also annotated with GO:0005975 (carbohydrate metabolic process), a parent term; the question's option A (carbohydrate derivative metabolic process) is the more specific child term and is the one annotated.",
    "The protein was first publicly annotated in UniProt on 2025-02-05, and its experimental characterization was published in 2024; the benchmark's author snapshot date is unknown, so the annotation available at question-creation time may have differed.",
    "The sequence-match is confirmed (SHA-256 identical across current and historical snapshots), so the annotation applies to the exact sequence provided."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options (B, C, D) describe fundamentally different protein classes (ion transporters/channels, transcriptional regulators, signaling components) with no structural or functional overlap with a small-molecule isomerase. No reasonable biological argument supports choosing any of them for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A3MTR6) annotates this protein with GO:1901135 (carbohydrate derivative metabolic process) via IEA:InterPro. The experimentally characterized function (PubMed:39208883, ECO:0000269) confirms it is a bifunctional phosphoglucose/phosphomannose isomerase catalyzing isomerization of glucose-6-phosphate and mannose-6-phosphate to fructose-6-phosphate. These substrates and products are phosphorylated sugars (carbohydrate derivatives), making the GO term biologically accurate. The GO term assignment itself is computational (IEA:InterPro), but the underlying biochemical function is experimentally validated and unambiguously falls within carbohydrate derivative metabolism.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~299 aa) contains glycine-rich motifs (e.g., 'SGGMGGSGVVGDL', 'GGKLAQMG') suggestive of nucleotide/cofactor-binding folds common in metabolic enzymes. Critically, the sequence lacks EF-hand or calcium-binding motifs (eliminating B: calcium ion homeostasis), lacks DNA-binding/transcriptional regulatory domains or protein-protein interaction modules typical of biosynthetic pathway regulators (eliminating C: positive regulation of secondary metabolite biosynthetic process), and lacks kinase domains, SH2/SH3 adaptors, transmembrane segments, or other signaling architectures (eliminating D: positive regulation of signal transduction). By elimination, the protein is a metabolic enzyme, and among the four options, 'carbohydrate derivative metabolic process' is the only one consistent with a small-molecule isomerase acting on phosphorylated sugars.",
    "missing_item_specific_fact": "Precisely recognizing the specific fold as phosphoglucose/phosphomannose isomerase (rather than, say, a generic dehydrogenase or transferase) would require either database lookup or recognition of the archaeal bifunctional PGI/PMI fold, which is not trivially deducible from primary sequence alone. However, the elimination of the three clearly wrong distractors is achievable through domain-level reasoning.",
    "reason": "Three of the four distractors describe regulatory, signaling, or ion-homeostasis functions that require specific structural domains (EF-hands, kinase domains, transcription factor motifs) entirely absent from this sequence. The remaining option (A) is a broad metabolic process category consistent with the glycine-rich nucleotide-binding-like motifs and the absence of any regulatory architecture. While positively identifying the exact enzyme class is lookup-assisted, the elimination-based reasoning is biologically sound and does not require memorizing this particular UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The other three options (B, C, D) describe fundamentally different protein classes (ion transporters/channels, transcriptional regulators, signaling components) with no structural or functional overlap with a small-molecule isomerase. No reasonable biological argument supports choosing any of them for this sequence."
  },
  "important_caveats": [
    "The GO:1901135 annotation is IEA:InterPro (computational), not directly experimental, though the underlying catalytic activity is experimentally confirmed (ECO:0000269).",
    "The protein is also annotated with GO:0005975 (carbohydrate metabolic process), a parent term; the question's option A (carbohydrate derivative metabolic process) is the more specific child term and is the one annotated.",
    "The protein was first publicly annotated in UniProt on 2025-02-05, and its experimental characterization was published in 2024; the benchmark's author snapshot date is unknown, so the annotation available at question-creation time may have differed.",
    "The sequence-match is confirmed (SHA-256 identical across current and historical snapshots), so the annotation applies to the exact sequence provided."
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

**Accession:** `A3MTR6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 74. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
"A3MTR6"
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Glucose-6-phosphate isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"GPI"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Mannose-6-phosphate isomerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.8"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"5.3.1.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39208883","source":"PubMed"}],"value":"Bifunctional phosphoglucose/phosphomannose isomerase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Bifunctional PGI/PMI"}]}}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39208883","source":"PubMed"}],"value":"Dual specificity isomerase that catalyzes the isomerization of both glucose-6-phosphate and mannose-6-phosphate to fructose-6-phosphate with nearly similar catalytic efficiency (PubMed:39208883). Also catalyzes the epimerization of mannose 6-phosphate to glucose 6-phosphate but the rate of epimerization reaction is 20-fold lower than that of isomerization reaction (PubMed:39208883)"}]}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"database":"GO","id":"GO:1901135","properties":[{"key":"GoTerm","value":"P:carbohydrate derivative metabolic process"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3MTR6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:58.786987+00:00.  

```json
{"citation":{"authors":["Maqsood A.","Shakir N.A.","Aslam M.","Rahman M.","Rashid N."],"citationCrossReferences":[{"database":"PubMed","id":"39208883"},{"database":"DOI","id":"10.1016/j.ijbiomac.2024.135127"}],"citationType":"journal article","firstPage":"135127","id":"39208883","journal":"Int. J. Biol. Macromol.","lastPage":"135127","publicationDate":"2024","title":"Structural and functional investigations of Pcal_0606, a bifunctional phosphoglucose/phosphomannose isomerase from Pyrobaculum calidifontis.","volume":"279"},"referenceComments":[{"type":"STRAIN","value":"DSM 21063 / JCM 11548 / VA1"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT"]}
```

Source SHA-256: `ab4d5d4975cecc6a04c1957b13bd9283e2ef63f3360c1922d6682cfab0917db3`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)  
**Locator:** `lines 37-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:27:04.156488+00:00.  

```text
CC   -!- FUNCTION: Dual specificity isomerase that catalyzes the isomerization
CC       of both glucose-6-phosphate and mannose-6-phosphate to fructose-6-
CC       phosphate with nearly similar catalytic efficiency (PubMed:39208883).
CC       Also catalyzes the epimerization of mannose 6-phosphate to glucose 6-
CC       phosphate but the rate of epimerization reaction is 20-fold lower than
CC       that of isomerization reaction (PubMed:39208883).
CC       {ECO:0000269|PubMed:39208883}.
```

Source SHA-256: `9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3MTR6?format=txt&versions=74)  
**Locator:** `lines 99-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 74 / 1.  
**Retrieved:** 2026-11-02T04:27:04.156488+00:00.  

```text
DR   GO; GO:1901135; P:carbohydrate derivative metabolic process; IEA:InterPro.
```

Source SHA-256: `9c472af706932a5c4dae44d3e7eaa83f12d4956caae5979ddee1e4be573d0761`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 471774-471785`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1901135
name: carbohydrate derivative metabolic process
namespace: biological_process
def: "The chemical reactions and pathways involving carbohydrate derivative." [GOC:TermGenie]
subset: goslim_agr
subset: goslim_generic
subset: goslim_mouse
subset: goslim_prokaryote
synonym: "carbohydrate derivative metabolism" EXACT [GOC:TermGenie]
is_a: GO:0008152 ! metabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
