# GO_biological_process_0163

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — symbiont-mediated suppression of host innate immune response

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIEIFKDTGATHDLVYHSKINTFVWDVEFDIVLSDSKELNKCYFVKCFNPYRINGKCDFAVSSIDIFSEGKRLLIENEFNFKITKAVHVATSKDVTEIVLHLSERISSPFPIVKEVVYLD

[Multiple Choices]
A. neuron projection maintenance
B. DNA damage checkpoint signaling
C. extracellular matrix organization
D. symbiont-mediated suppression of host innate immune response
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

> The supplied sequence exactly matches the UniProt entry for a Bacillus phage protein. Its curated function says it counteracts the host DSR2 defense system by inhibiting its NADase activity, supporting the selected process. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned, while the function annotation cites experimental evidence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C5](#evidence-c5), [C6](#evidence-c6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices name very different processes, but the 120-residue sequence alone provides no clear, general biological feature that identifies a phage protein suppressing host defense rather than the other options.


**Missing item-specific fact**

> The protein-specific identity and functional evidence that this phage protein counteracts host DSR2 defense are absent from the model input.


**Reason**

> The key is supported by reviewer-only annotation and cited functional studies, but that information was not supplied to the evaluated model. Inferring the precise process would require an item-specific protein identification or functional annotation, not general sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewed function supports D; the other choices describe unrelated processes and are not supported by the supplied reviewer evidence.


### Important caveats

- The sequence match and protein identity come from reviewer-only sources, not the original question.
- The GO term annotation is computationally assigned (IEA:UniProtKB-KW); the separate curated function statement cites experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices name very different processes, but the 120-residue sequence alone provides no clear, general biological feature that identifies a phage protein suppressing host defense rather than the other options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and functional evidence that this phage protein counteracts host DSR2 defense are absent from the model input.",
    "reason": "The key is supported by reviewer-only annotation and cited functional studies, but that information was not supplied to the evaluated model. Inferring the precise process would require an item-specific protein identification or functional annotation, not general sequence reasoning."
  },
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C5",
      "C6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a Bacillus phage protein. Its curated function says it counteracts the host DSR2 defense system by inhibiting its NADase activity, supporting the selected process. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned, while the function annotation cites experimental evidence."
  },
  "important_caveats": [
    "The sequence match and protein identity come from reviewer-only sources, not the original question.",
    "The GO term annotation is computationally assigned (IEA:UniProtKB-KW); the separate curated function statement cites experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewed function supports D; the other choices describe unrelated processes and are not supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry for a Bacillus phage protein. Its curated function says it counteracts the host DSR2 defense system by inhibiting its NADase activity, supporting the selected process. The GO annotation itself is IEA:UniProtKB-KW, so it is computationally assigned, while the function annotation cites experimental evidence.",
    "evidence_ids": ["C1", "C3", "C5", "C6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices name very different processes, but the 120-residue sequence alone provides no clear, general biological feature that identifies a phage protein suppressing host defense rather than the other options.",
    "missing_item_specific_fact": "The protein-specific identity and functional evidence that this phage protein counteracts host DSR2 defense are absent from the model input.",
    "reason": "The key is supported by reviewer-only annotation and cited functional studies, but that information was not supplied to the evaluated model. Inferring the precise process would require an item-specific protein identification or functional annotation, not general sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewed function supports D; the other choices describe unrelated processes and are not supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The sequence match and protein identity come from reviewer-only sources, not the original question.",
    "The GO term annotation is computationally assigned (IEA:UniProtKB-KW); the separate curated function statement cites experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt O64191 (DSAD1_BPSPB, 'DSR anti-defense 1') from Bacillus phage SPbeta. The experimentally supported function (ECO:0000269, multiple PubMed references) is that this phage protein counteracts the host DSR2 defense system by inhibiting its NADase activity, thereby suppressing the host's innate immune response. GO:0052170 ('symbiont-mediated suppression of host innate immune response') is annotated to this entry. While the GO annotation carries an IEA:UniProtKB-KW evidence code, the underlying function is supported by direct experimental evidence (ECO:0000269) from at least five independent publications including cryo-EM structural studies. The GO term definition precisely matches: a symbiont (phage) inhibiting the host's (Bacillus) innate defense system (DSR2).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO3](#evidence-go3), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> None derivable from the supplied input. The 120-residue sequence contains no recognizable catalytic motifs, signal peptides, transmembrane helices, or domain architectures that would allow a scientist to infer that this protein functions as a phage-encoded anti-defense protein targeting a bacterial sirtuin NADase. Without organism or context information, the sequence is essentially uncharacterizable by general biological reasoning.


**Missing item-specific fact**

> The identity of the protein as a Bacillus phage SPbeta-encoded anti-defense protein (DSAD1) and its specific interaction with the host DSR2 NADase defense system. This requires either recognizing the exact sequence from a database or knowing the specific experimental literature (Garb et al. 2022, Wang et al. 2024, etc.).


**Reason**

> The question provides only a raw amino acid sequence with no organism, no functional context, and no structural information. To select option D over A, B, or C, one must know that this is a bacteriophage protein that suppresses a host defense system. No general biological reasoning from the sequence alone distinguishes a phage anti-defense protein from a hypothetical neuronal maintenance factor, a DNA damage checkpoint component, or an extracellular matrix protein. The answer depends entirely on database lookup or memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different biological contexts (neuronal, DNA repair, extracellular matrix, phage-host interaction). If the organism context (bacteriophage) were provided, D would be the only plausible choice. However, from the sequence alone, no option is more defensible than the others through reasoning. The distractors are not truly ambiguous with the key—they are simply unanswerable without external knowledge.


### Important caveats

- The GO annotation evidence code is IEA:UniProtKB-KW (inferred from keyword), not a direct experimental GO assignment. However, the underlying molecular function is supported by ECO:0000269 (direct assay) evidence from multiple independent studies.
- The UniProt entry was only first publicly released on 2025-02-05. The benchmark author's source snapshot date is unknown, raising questions about whether this annotation was available at question-construction time.
- The GO term 'symbiont-mediated suppression of host innate immune response' was originally designed for pathogen-host interactions (e.g., bacterial pathogens suppressing animal immunity). Its application to a bacteriophage suppressing a bacterial anti-phage defense system is a semantic extension, though UniProt and GO have accepted this usage.
- The protein is only 120 residues long, making it extremely difficult to identify by sequence-based reasoning without database access.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "None derivable from the supplied input. The 120-residue sequence contains no recognizable catalytic motifs, signal peptides, transmembrane helices, or domain architectures that would allow a scientist to infer that this protein functions as a phage-encoded anti-defense protein targeting a bacterial sirtuin NADase. Without organism or context information, the sequence is essentially uncharacterizable by general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the protein as a Bacillus phage SPbeta-encoded anti-defense protein (DSAD1) and its specific interaction with the host DSR2 NADase defense system. This requires either recognizing the exact sequence from a database or knowing the specific experimental literature (Garb et al. 2022, Wang et al. 2024, etc.).",
    "reason": "The question provides only a raw amino acid sequence with no organism, no functional context, and no structural information. To select option D over A, B, or C, one must know that this is a bacteriophage protein that suppresses a host defense system. No general biological reasoning from the sequence alone distinguishes a phage anti-defense protein from a hypothetical neuronal maintenance factor, a DNA damage checkpoint component, or an extracellular matrix protein. The answer depends entirely on database lookup or memorization of this specific protein's annotation."
  },
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "GO3",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt O64191 (DSAD1_BPSPB, 'DSR anti-defense 1') from Bacillus phage SPbeta. The experimentally supported function (ECO:0000269, multiple PubMed references) is that this phage protein counteracts the host DSR2 defense system by inhibiting its NADase activity, thereby suppressing the host's innate immune response. GO:0052170 ('symbiont-mediated suppression of host innate immune response') is annotated to this entry. While the GO annotation carries an IEA:UniProtKB-KW evidence code, the underlying function is supported by direct experimental evidence (ECO:0000269) from at least five independent publications including cryo-EM structural studies. The GO term definition precisely matches: a symbiont (phage) inhibiting the host's (Bacillus) innate defense system (DSR2)."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:UniProtKB-KW (inferred from keyword), not a direct experimental GO assignment. However, the underlying molecular function is supported by ECO:0000269 (direct assay) evidence from multiple independent studies.",
    "The UniProt entry was only first publicly released on 2025-02-05. The benchmark author's source snapshot date is unknown, raising questions about whether this annotation was available at question-construction time.",
    "The GO term 'symbiont-mediated suppression of host innate immune response' was originally designed for pathogen-host interactions (e.g., bacterial pathogens suppressing animal immunity). Its application to a bacteriophage suppressing a bacterial anti-phage defense system is a semantic extension, though UniProt and GO have accepted this usage.",
    "The protein is only 120 residues long, making it extremely difficult to identify by sequence-based reasoning without database access."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological contexts (neuronal, DNA repair, extracellular matrix, phage-host interaction). If the organism context (bacteriophage) were provided, D would be the only plausible choice. However, from the sequence alone, no option is more defensible than the others through reasoning. The distractors are not truly ambiguous with the key—they are simply unanswerable without external knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt O64191 (DSAD1_BPSPB, 'DSR anti-defense 1') from Bacillus phage SPbeta. The experimentally supported function (ECO:0000269, multiple PubMed references) is that this phage protein counteracts the host DSR2 defense system by inhibiting its NADase activity, thereby suppressing the host's innate immune response. GO:0052170 ('symbiont-mediated suppression of host innate immune response') is annotated to this entry. While the GO annotation carries an IEA:UniProtKB-KW evidence code, the underlying function is supported by direct experimental evidence (ECO:0000269) from at least five independent publications including cryo-EM structural studies. The GO term definition precisely matches: a symbiont (phage) inhibiting the host's (Bacillus) innate defense system (DSR2).",
    "evidence_ids": ["C4", "C5", "C6", "GO3", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "None derivable from the supplied input. The 120-residue sequence contains no recognizable catalytic motifs, signal peptides, transmembrane helices, or domain architectures that would allow a scientist to infer that this protein functions as a phage-encoded anti-defense protein targeting a bacterial sirtuin NADase. Without organism or context information, the sequence is essentially uncharacterizable by general biological reasoning.",
    "missing_item_specific_fact": "The identity of the protein as a Bacillus phage SPbeta-encoded anti-defense protein (DSAD1) and its specific interaction with the host DSR2 NADase defense system. This requires either recognizing the exact sequence from a database or knowing the specific experimental literature (Garb et al. 2022, Wang et al. 2024, etc.).",
    "reason": "The question provides only a raw amino acid sequence with no organism, no functional context, and no structural information. To select option D over A, B, or C, one must know that this is a bacteriophage protein that suppresses a host defense system. No general biological reasoning from the sequence alone distinguishes a phage anti-defense protein from a hypothetical neuronal maintenance factor, a DNA damage checkpoint component, or an extracellular matrix protein. The answer depends entirely on database lookup or memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological contexts (neuronal, DNA repair, extracellular matrix, phage-host interaction). If the organism context (bacteriophage) were provided, D would be the only plausible choice. However, from the sequence alone, no option is more defensible than the others through reasoning. The distractors are not truly ambiguous with the key—they are simply unanswerable without external knowledge."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:UniProtKB-KW (inferred from keyword), not a direct experimental GO assignment. However, the underlying molecular function is supported by ECO:0000269 (direct assay) evidence from multiple independent studies.",
    "The UniProt entry was only first publicly released on 2025-02-05. The benchmark author's source snapshot date is unknown, raising questions about whether this annotation was available at question-construction time.",
    "The GO term 'symbiont-mediated suppression of host innate immune response' was originally designed for pathogen-host interactions (e.g., bacterial pathogens suppressing animal immunity). Its application to a bacteriophage suppressing a bacterial anti-phage defense system is a semantic extension, though UniProt and GO have accepted this usage.",
    "The protein is only 120 residues long, making it extremely difficult to identify by sequence-based reasoning without database access."
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

**Accession:** `O64191` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:15.584566+00:00.  

```json
"O64191"
```

Source SHA-256: `e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:15.584566+00:00.  

```json
{"commonName":"Bacillus phage SPBc2","lineage":["Viruses","Duplodnaviria","Heunggongvirae","Uroviricota","Caudoviricetes","Caudoviricetes incertae sedis","Spbetavirus","Spbetavirus SPbeta"],"scientificName":"Bacillus phage SPbeta","synonyms":["Bacteriophage SP-beta"],"taxonId":2932878}
```

Source SHA-256: `e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:15.584566+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36192536","source":"PubMed"}],"value":"DSR anti-defense 1"},"shortNames":[{"value":"DSAD1"}]}}
```

Source SHA-256: `e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:15.584566+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36192536","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38538592","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38555355","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38729958","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"39039073","source":"PubMed"}],"value":"Counteracts the defense-associated sirtuin 2 (DSR2) defense system of the host (PubMed:36192536, PubMed:38538592, PubMed:38555355, PubMed:38729958, PubMed:39039073). Inhibits the NADase activity of host DSR2 by competing with the tail tube protein that normally activates DSR2 (PubMed:38538592, PubMed:39039073)"}]}
```

Source SHA-256: `e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O64191.json)  
**Locator:** `/uniProtKBCrossReferences/36`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:15.584566+00:00.  

```json
{"database":"GO","id":"GO:0052170","properties":[{"key":"GoTerm","value":"P:symbiont-mediated suppression of host innate immune response"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-KW"}]}
```

Source SHA-256: `e2873aded3b55dcdc6f5a72a98daedf2e00b71fe4d98b516085e87f0efa0ad7d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)  
**Locator:** `lines 78-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:29:17.658870+00:00.  

```text
CC   -!- FUNCTION: Counteracts the defense-associated sirtuin 2 (DSR2) defense
CC       system of the host (PubMed:36192536, PubMed:38538592, PubMed:38555355,
CC       PubMed:38729958, PubMed:39039073). Inhibits the NADase activity of host
CC       DSR2 by competing with the tail tube protein that normally activates
CC       DSR2 (PubMed:38538592, PubMed:39039073). {ECO:0000269|PubMed:36192536,
CC       ECO:0000269|PubMed:38538592, ECO:0000269|PubMed:38555355,
CC       ECO:0000269|PubMed:38729958, ECO:0000269|PubMed:39039073}.
```

Source SHA-256: `a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O64191?format=txt&versions=55)  
**Locator:** `lines 131-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:29:17.658870+00:00.  

```text
DR   GO; GO:0052170; P:symbiont-mediated suppression of host innate immune response; IEA:UniProtKB-KW.
```

Source SHA-256: `a86a594cfc7c1b43e8061d61eb4f3756aec96678c3bdfe1b96d55f6e48c7ac11`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 334843-334862`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0052170
name: symbiont-mediated suppression of host innate immune response
namespace: biological_process
alt_id: GO:0052309
def: "A process in which a symbiont inhibits or disrupts the normal execution of the innate immune response of the host organism, the host's first line of defense against infection. The host is defined as the larger of the organisms involved in a symbiotic interaction." [GOC:mtg_pamgo_17jul06]
synonym: "down regulation by symbiont of host innate immunity" EXACT []
synonym: "down-regulation by symbiont of host innate immunity" EXACT []
synonym: "downregulation by symbiont of host innate immunity" EXACT []
synonym: "inhibition by symbiont of host innate immunity" NARROW []
synonym: "negative regulation by symbiont of host innate immune response" EXACT []
synonym: "negative regulation by symbiont of host innate immunity" EXACT [GOC:pg]
synonym: "negative regulation of host innate immune response" EXACT []
synonym: "negative regulation of innate immune response in other organism" BROAD []
synonym: "suppression by symbiont of host innate immune response" EXACT []
synonym: "suppression of host innate immune response" EXACT []
xref: Reactome:R-HSA-9637687 "Suppression of phagosomal maturation"
is_a: GO:0052167 ! symbiont-mediated perturbation of host innate immune response
is_a: GO:0052562 ! symbiont-mediated suppression of host immune response

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
