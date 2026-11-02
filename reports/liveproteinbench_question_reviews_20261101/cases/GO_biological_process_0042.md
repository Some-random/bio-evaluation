# GO_biological_process_0042

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — biological process involved in symbiotic interaction

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQPVGLSNTPASSLLNETAELRHQTTPRQLGGIRIVGEIVDISYEPNDVVFFGVGRGVMIGDILFPGSSADIMRELLMAHSGVRGILQQQENAPSSLQTRISECTFSVSQEKLQCPEEEMRCPVTLETPEKGVFVKNSGDSSVCTLFDSSSFSRLVRDGGVHPLTREPIKASMIVSSDKCVYDNAKGNFVIKNS

[Multiple Choices]
A. oligodendrocyte development
B. response to mechanical stimulus
C. in utero embryonic development
D. biological process involved in symbiotic interaction
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

> The supplied sequence exactly matches a Citrobacter rodentium protein annotated as probable E3 ubiquitin-protein ligase NleG1. Its annotation links it to biological processes involved in symbiotic interaction, and the functional note describes a probable host-targeting effector; a bacterial deletion was also associated with less severe diarrhea in infected mice. The GO assignment itself is computational (IEA:InterPro), not direct experimental evidence for that GO term.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not give a reliable, specific indication of the protein's role in host-pathogen interaction. The options make D broadly compatible with a bacterial virulence effector, but identifying this sequence as NleG1 is needed to establish that context.


**Missing item-specific fact**

> The sequence-specific identification of this protein as a Citrobacter rodentium NleG1 effector and its host-interaction annotation or functional literature.


**Reason**

> Those identity and functional facts are absent from the prompt. General biological knowledge may make the eukaryotic-development options less plausible for a bacterial protein, but it does not establish the particular symbiotic-interaction process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, D is supported by the matching protein annotation and its described role as a host-targeting bacterial effector. The evidence does not support another listed option.


### Important caveats

- The GO:0044403 annotation is IEA:InterPro, a computational annotation; it is not itself an experimental demonstration of that biological process.
- The functional note describes the E3 ligase activity as probable, while reporting a mouse infection phenotype associated with deletion of the gene.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not give a reliable, specific indication of the protein's role in host-pathogen interaction. The options make D broadly compatible with a bacterial virulence effector, but identifying this sequence as NleG1 is needed to establish that context.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific identification of this protein as a Citrobacter rodentium NleG1 effector and its host-interaction annotation or functional literature.",
    "reason": "Those identity and functional facts are absent from the prompt. General biological knowledge may make the eukaryotic-development options less plausible for a bacterial protein, but it does not establish the particular symbiotic-interaction process."
  },
  "case_id": "GO_biological_process_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a Citrobacter rodentium protein annotated as probable E3 ubiquitin-protein ligase NleG1. Its annotation links it to biological processes involved in symbiotic interaction, and the functional note describes a probable host-targeting effector; a bacterial deletion was also associated with less severe diarrhea in infected mice. The GO assignment itself is computational (IEA:InterPro), not direct experimental evidence for that GO term."
  },
  "important_caveats": [
    "The GO:0044403 annotation is IEA:InterPro, a computational annotation; it is not itself an experimental demonstration of that biological process.",
    "The functional note describes the E3 ligase activity as probable, while reporting a mouse infection phenotype associated with deletion of the gene."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is supported by the matching protein annotation and its described role as a host-targeting bacterial effector. The evidence does not support another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches a Citrobacter rodentium protein annotated as probable E3 ubiquitin-protein ligase NleG1. Its annotation links it to biological processes involved in symbiotic interaction, and the functional note describes a probable host-targeting effector; a bacterial deletion was also associated with less severe diarrhea in infected mice. The GO assignment itself is computational (IEA:InterPro), not direct experimental evidence for that GO term.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not give a reliable, specific indication of the protein's role in host-pathogen interaction. The options make D broadly compatible with a bacterial virulence effector, but identifying this sequence as NleG1 is needed to establish that context.",
    "missing_item_specific_fact": "The sequence-specific identification of this protein as a Citrobacter rodentium NleG1 effector and its host-interaction annotation or functional literature.",
    "reason": "Those identity and functional facts are absent from the prompt. General biological knowledge may make the eukaryotic-development options less plausible for a bacterial protein, but it does not establish the particular symbiotic-interaction process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, D is supported by the matching protein annotation and its described role as a host-targeting bacterial effector. The evidence does not support another listed option."
  },
  "important_caveats": [
    "The GO:0044403 annotation is IEA:InterPro, a computational annotation; it is not itself an experimental demonstration of that biological process.",
    "The functional note describes the E3 ligase activity as probable, while reporting a mouse infection phenotype associated with deletion of the gene."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is NleG1 from Citrobacter rodentium, a Type 3 Secreted Effector with probable E3 ubiquitin-protein ligase (U-box) activity that interferes with host ubiquitination pathways to promote bacterial survival in host tissues (C4, C5, H3). The GO annotation GO:0044403 'biological process involved in symbiotic interaction' is explicitly assigned (C6, H4), with evidence code IEA:InterPro. The GO term definition (GO4) includes 'host-pathogen interaction' and 'parasitism' as NARROW synonyms, making a bacterial effector that manipulates host cell physiology squarely within this category. The PubMed reference (36511702) provides experimental support: deletion of nleG1 reduces diarrhea severity in infected mice. The annotation is computational (IEA) but the functional role is experimentally supported.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a small (~194 aa) bacterial protein. Three of the four options (oligodendrocyte development, in utero embryonic development, response to mechanical stimulus) describe mammalian-specific developmental or sensory processes that are inapplicable to a bacterial protein. The sequence contains features consistent with a U-box E3 ubiquitin ligase domain. A bacterial protein with E3 ligase activity targeting host cell proteins is a hallmark of pathogen effectors that manipulate host physiology during infection. Host-pathogen interaction is explicitly a NARROW synonym of GO:0044403 'biological process involved in symbiotic interaction' (GO4). Thus, general knowledge of bacterial virulence mechanisms and GO ontology structure allows positive identification of D and elimination of A, B, C.


**Missing item-specific fact**

> Precise recognition of the U-box domain fold from raw sequence alone is non-trivial without database lookup, and the specific assignment to NleG1/Citrobacter rodentium T3SS effector requires item-specific knowledge. However, the elimination of the three mammalian/mechanosensory distractors and the positive inference that a bacterial E3 ligase targeting host proteins operates in host-pathogen (symbiotic) interaction provides a defensible reasoning path.


**Reason**

> The question can be addressed through general biological reasoning: (1) the protein is clearly bacterial (small size, sequence composition, no eukaryotic signal peptide), eliminating A and C as mammalian-specific processes; (2) no mechanosensory domain is present, eliminating B; (3) a bacterial protein with E3 ubiquitin ligase activity that targets host proteins is a pathogen effector, and host-pathogen interaction falls under 'symbiotic interaction' in GO. This constitutes a concrete biological argument distinguishing D from the alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (oligodendrocyte development), B (response to mechanical stimulus), and C (in utero embryonic development) are all mammalian-specific biological processes with no plausible connection to a 194-aa bacterial protein. Only D applies to a bacterial organism engaging in host interaction. The distractors are clearly eliminable.


### Important caveats

- The GO annotation evidence code is IEA:InterPro (automated/computational), not direct experimental annotation of the GO term itself, though the underlying function is experimentally supported by PubMed:36511702.
- The protein name includes 'Probable' (Probable E3 ubiquitin-protein ligase NleG1), indicating the enzymatic activity assignment is by similarity (ECO:0000250 to A0A482PDI9), not direct experimental validation of ligase activity for this specific protein.
- The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt entry A0A482PJF5, both historical and current).
- The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence with no organism or name information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a small (~194 aa) bacterial protein. Three of the four options (oligodendrocyte development, in utero embryonic development, response to mechanical stimulus) describe mammalian-specific developmental or sensory processes that are inapplicable to a bacterial protein. The sequence contains features consistent with a U-box E3 ubiquitin ligase domain. A bacterial protein with E3 ligase activity targeting host cell proteins is a hallmark of pathogen effectors that manipulate host physiology during infection. Host-pathogen interaction is explicitly a NARROW synonym of GO:0044403 'biological process involved in symbiotic interaction' (GO4). Thus, general knowledge of bacterial virulence mechanisms and GO ontology structure allows positive identification of D and elimination of A, B, C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise recognition of the U-box domain fold from raw sequence alone is non-trivial without database lookup, and the specific assignment to NleG1/Citrobacter rodentium T3SS effector requires item-specific knowledge. However, the elimination of the three mammalian/mechanosensory distractors and the positive inference that a bacterial E3 ligase targeting host proteins operates in host-pathogen (symbiotic) interaction provides a defensible reasoning path.",
    "reason": "The question can be addressed through general biological reasoning: (1) the protein is clearly bacterial (small size, sequence composition, no eukaryotic signal peptide), eliminating A and C as mammalian-specific processes; (2) no mechanosensory domain is present, eliminating B; (3) a bacterial protein with E3 ubiquitin ligase activity that targets host proteins is a pathogen effector, and host-pathogen interaction falls under 'symbiotic interaction' in GO. This constitutes a concrete biological argument distinguishing D from the alternatives."
  },
  "case_id": "GO_biological_process_0042",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The protein is NleG1 from Citrobacter rodentium, a Type 3 Secreted Effector with probable E3 ubiquitin-protein ligase (U-box) activity that interferes with host ubiquitination pathways to promote bacterial survival in host tissues (C4, C5, H3). The GO annotation GO:0044403 'biological process involved in symbiotic interaction' is explicitly assigned (C6, H4), with evidence code IEA:InterPro. The GO term definition (GO4) includes 'host-pathogen interaction' and 'parasitism' as NARROW synonyms, making a bacterial effector that manipulates host cell physiology squarely within this category. The PubMed reference (36511702) provides experimental support: deletion of nleG1 reduces diarrhea severity in infected mice. The annotation is computational (IEA) but the functional role is experimentally supported."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:InterPro (automated/computational), not direct experimental annotation of the GO term itself, though the underlying function is experimentally supported by PubMed:36511702.",
    "The protein name includes 'Probable' (Probable E3 ubiquitin-protein ligase NleG1), indicating the enzymatic activity assignment is by similarity (ECO:0000250 to A0A482PDI9), not direct experimental validation of ligase activity for this specific protein.",
    "The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt entry A0A482PJF5, both historical and current).",
    "The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence with no organism or name information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (oligodendrocyte development), B (response to mechanical stimulus), and C (in utero embryonic development) are all mammalian-specific biological processes with no plausible connection to a 194-aa bacterial protein. Only D applies to a bacterial organism engaging in host interaction. The distractors are clearly eliminable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0042",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is NleG1 from Citrobacter rodentium, a Type 3 Secreted Effector with probable E3 ubiquitin-protein ligase (U-box) activity that interferes with host ubiquitination pathways to promote bacterial survival in host tissues (C4, C5, H3). The GO annotation GO:0044403 'biological process involved in symbiotic interaction' is explicitly assigned (C6, H4), with evidence code IEA:InterPro. The GO term definition (GO4) includes 'host-pathogen interaction' and 'parasitism' as NARROW synonyms, making a bacterial effector that manipulates host cell physiology squarely within this category. The PubMed reference (36511702) provides experimental support: deletion of nleG1 reduces diarrhea severity in infected mice. The annotation is computational (IEA) but the functional role is experimentally supported.",
    "evidence_ids": ["C3", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a small (~194 aa) bacterial protein. Three of the four options (oligodendrocyte development, in utero embryonic development, response to mechanical stimulus) describe mammalian-specific developmental or sensory processes that are inapplicable to a bacterial protein. The sequence contains features consistent with a U-box E3 ubiquitin ligase domain. A bacterial protein with E3 ligase activity targeting host cell proteins is a hallmark of pathogen effectors that manipulate host physiology during infection. Host-pathogen interaction is explicitly a NARROW synonym of GO:0044403 'biological process involved in symbiotic interaction' (GO4). Thus, general knowledge of bacterial virulence mechanisms and GO ontology structure allows positive identification of D and elimination of A, B, C.",
    "missing_item_specific_fact": "Precise recognition of the U-box domain fold from raw sequence alone is non-trivial without database lookup, and the specific assignment to NleG1/Citrobacter rodentium T3SS effector requires item-specific knowledge. However, the elimination of the three mammalian/mechanosensory distractors and the positive inference that a bacterial E3 ligase targeting host proteins operates in host-pathogen (symbiotic) interaction provides a defensible reasoning path.",
    "reason": "The question can be addressed through general biological reasoning: (1) the protein is clearly bacterial (small size, sequence composition, no eukaryotic signal peptide), eliminating A and C as mammalian-specific processes; (2) no mechanosensory domain is present, eliminating B; (3) a bacterial protein with E3 ubiquitin ligase activity that targets host proteins is a pathogen effector, and host-pathogen interaction falls under 'symbiotic interaction' in GO. This constitutes a concrete biological argument distinguishing D from the alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (oligodendrocyte development), B (response to mechanical stimulus), and C (in utero embryonic development) are all mammalian-specific biological processes with no plausible connection to a 194-aa bacterial protein. Only D applies to a bacterial organism engaging in host interaction. The distractors are clearly eliminable."
  },
  "important_caveats": [
    "The GO annotation evidence code is IEA:InterPro (automated/computational), not direct experimental annotation of the GO term itself, though the underlying function is experimentally supported by PubMed:36511702.",
    "The protein name includes 'Probable' (Probable E3 ubiquitin-protein ligase NleG1), indicating the enzymatic activity assignment is by similarity (ECO:0000250 to A0A482PDI9), not direct experimental validation of ligase activity for this specific protein.",
    "The sequence-match is confirmed (SHA256 match between benchmark sequence and UniProt entry A0A482PJF5, both historical and current).",
    "The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence with no organism or name information."
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

**Accession:** `A0A482PJF5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 11. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
"A0A482PJF5"
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Gammaproteobacteria","Enterobacterales","Enterobacteriaceae","Citrobacter"],"scientificName":"Citrobacter rodentium","taxonId":67825}
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A482PDI9","source":"UniProtKB"}],"value":"2.3.2.27"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable E3 ubiquitin-protein ligase NleG1"}}}
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"36511702","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"36511702","source":"PubMed"}],"value":"Effector proteins function to alter host cell physiology and promote bacterial survival in host tissues. This protein is probably an E3 ubiquitin-protein ligase that interferes with the host's ubiquitination pathway and targets host proteins for proteasomal degradation (Probable) (PubMed:36511702). Mice infected with a strain of bacteria deleted for this gene have less severe diarrhea (PubMed:36511702)"}]}
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
{"database":"GO","id":"GO:0044403","properties":[{"key":"GoTerm","value":"P:biological process involved in symbiotic interaction"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJF5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:19.612966+00:00.  

```json
{"citation":{"authors":["Popov G.","Fiebig-Comyn A.","Syriste L.","Little D.J.","Skarina T.","Stogios P.J.","Birstonas S.","Coombes B.K.","Savchenko A."],"citationCrossReferences":[{"database":"PubMed","id":"36511702"},{"database":"DOI","id":"10.1128/iai.00505-22"}],"citationType":"journal article","firstPage":"e0050522","id":"36511702","journal":"Infect. Immun.","lastPage":"e0050522","publicationDate":"2023","title":"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.","volume":"91"},"referenceComments":[{"type":"STRAIN","value":"DBS100"}],"referenceNumber":2,"referencePositions":["SUBCELLULAR LOCATION","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `11427ada1e54afd66fb50a1b10f568002aca65107f966bc47e8d83be4ff7f60f`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:25:21.816588+00:00.  

```text
ID   NLEG1_CITRO             Reviewed;         194 AA.
AC   A0A482PJF5;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUN-2019, sequence version 1.
DT   28-JAN-2026, entry version 11.
DE   RecName: Full=Probable E3 ubiquitin-protein ligase NleG1 {ECO:0000305};
DE            EC=2.3.2.27 {ECO:0000250|UniProtKB:A0A482PDI9};
GN   Name=nleG1 {ECO:0000303|PubMed:36511702};
GN   ORFNames=E2R62_04780 {ECO:0000312|EMBL:QBY28229.1};
OS   Citrobacter rodentium.
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Citrobacter.
OX   NCBI_TaxID=67825;
```

Source SHA-256: `f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)  
**Locator:** `lines 21-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:25:21.816588+00:00.  

```text
RN   [2]
RP   SUBCELLULAR LOCATION, INDUCTION, AND DISRUPTION PHENOTYPE.
RC   STRAIN=DBS100;
RX   PubMed=36511702; DOI=10.1128/iai.00505-22;
RA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,
RA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;
RT   "Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for
RT   Different Roles during Citrobacter rodentium Infection in Mice.";
RL   Infect. Immun. 91:e0050522-e0050522(2023).
```

Source SHA-256: `f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)  
**Locator:** `lines 36-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:25:21.816588+00:00.  

```text
CC   -!- FUNCTION: Effector proteins function to alter host cell physiology and
CC       promote bacterial survival in host tissues. This protein is probably an
CC       E3 ubiquitin-protein ligase that interferes with the host's
CC       ubiquitination pathway and targets host proteins for proteasomal
CC       degradation (Probable) (PubMed:36511702). Mice infected with a strain
CC       of bacteria deleted for this gene have less severe diarrhea
CC       (PubMed:36511702). {ECO:0000269|PubMed:36511702,
CC       ECO:0000305|PubMed:36511702}.
```

Source SHA-256: `f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJF5?format=txt&versions=11)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 11 / 1.  
**Retrieved:** 2026-11-02T04:25:21.816588+00:00.  

```text
DR   GO; GO:0044403; P:biological process involved in symbiotic interaction; IEA:InterPro.
```

Source SHA-256: `f78a74f5532168e1330a7a346878f07175e0a25c83def5e4db7d3fb344aa7c0c`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 256806-256828`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044403
name: biological process involved in symbiotic interaction
namespace: biological_process
alt_id: GO:0043298
alt_id: GO:0044404
alt_id: GO:0072519
alt_id: GO:0085031
def: "A process carried out by gene products in an organism that enable the organism to engage in a symbiotic relationship, a more or less intimate association, with another organism. The various forms of symbiosis include parasitism, in which the association is disadvantageous or destructive to one of the organisms; mutualism, in which the association is advantageous, or often necessary to one or both and not harmful to either; and commensalism, in which one member of the association benefits while the other is not affected. However, mutualism, parasitism, and commensalism are often not discrete categories of interactions and should rather be perceived as a continuum of interaction ranging from parasitism to mutualism. In fact, the direction of a symbiotic interaction can change during the lifetime of the symbionts due to developmental changes as well as changes in the biotic/abiotic environment in which the interaction occurs. Microscopic symbionts are often referred to as endosymbionts." [GOC:cc, PMID:31257129]
subset: goslim_chembl
synonym: "commensalism" NARROW []
synonym: "host-pathogen interaction" NARROW []
synonym: "parasitism" NARROW []
synonym: "symbiosis" RELATED []
synonym: "symbiosis, encompassing mutualism through parasitism" RELATED []
synonym: "symbiotic interaction" RELATED []
synonym: "symbiotic interaction between host and organism" RELATED []
synonym: "symbiotic interaction between organisms" RELATED []
synonym: "symbiotic interaction between species" RELATED []
synonym: "symbiotic process" RELATED []
xref: Reactome:R-HSA-9839923 "Dengue Virus Infection"
is_a: GO:0044419 ! biological process involved in interspecies interaction between organisms

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 42. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
