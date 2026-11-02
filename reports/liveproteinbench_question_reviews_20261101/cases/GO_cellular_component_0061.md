# GO_cellular_component_0061

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — host cell

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MESSSTPLAEYFWIAGVESVSYQDPNSQPAPAVPVESTIIEDGEPEDEWTNGGQPKTNARHSRQNSASRLSKMSLTERFSIQTLDDTDGNTKSNRSSATIRAVNPPDFSNGNDDSNGNSQNPAPSGTLGEGSMFMGDFDFDKALVKFAAEREVFLEDLTFSAGAKVQARAPMVNPRMERIRAEESDSGRLSPLRSIKGSIRRKMSFRDMNSVRKQPSNRISTSRAASIRTTRRLSNYNSVIPPPEPLNTDPDMHPLKRRFEPVLLDRYPPQEAGDEISRRGRFPDYVPMFAFPNDIQIVSSDDRPRSTWHGFTMTSDDNSKLYGITIIIWIALNADVAEDVEKKCEEWRQSHMSEEERELAASLGVRLAGERTHLSQLLAKLPTIPSGSPARERLEDEISTVEEKITLMTDMLRPLRHGAASKIEGLTAGESGLWAPRAYGILGRDAGNMSFWKEWLKAIVTPMTDGSVLRIPPSSPRVGRWQPLERYVVNLCTEAFNPLGSKTQVELGVRELRLYARKEADNEIPGSRTIDIYALFRCLSLENIVALFEYAMAESRIIFLSSHASMLHLACHALANLLYPLKWASIFIPILPARLLSALEAPCPYIVGIERRYDNIELPEDDYVLVDLDKDTIDATSQPVRLPRQARRKLMSLLQVAAPHKLRYGVATGPPPYAMESFPYDAFSTENGSLFRTSTPKSTLGKWVSQSSSGFGEADPPNEIQPPIFNAFASAHVENGKSDRPSTSKSGKTSPQSSVSPVSINFPPMPSTPVSRSDSGFALASTLREKRSGHFGEEKMRRSSSFGVDKHPPFQKPGMPFLNGHQANLSISAISVESQNSVIGGANGGYGGGYAPSTYAQSTLAASTIMPSMQIQPVRNTETTVWVEGHCFNYMPKDNTSMCTICNDLAEGDGVYRCTGCKIVSHGRCLGYCSLICPEAFHADRVRAAFVRCLASLLYTYRKYLGRPSKQQKSNGQLYAFDMDGFIKSLPHDQHDYAAMMRETQCFNEFIHDREMQPANDASIRLFDEIIMAKKARGRSGLATGLSRLSTLRASHGASTYGGFGPARGGSNSKIPAFLGDISDHIWRTASVPLPKGNFPGEYKTIVTRTPARLDRSLMREPRSIQGMPRVEPRGTRGLIRKQVPNMFGTTPPT

[Multiple Choices]
A. nuclear periphery
B. neuron projection
C. host cell
D. Golgi apparatus
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

> The sequence-matched UniProt record annotates the protein as located in the host cell and as secreted. The host-cell annotation is also present as a GO term, though that GO assignment is computationally inferred; the subcellular-location statement cites a publication.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices do not provide a biological context that identifies this protein as a pathogen effector or otherwise establishes host-cell localization. The sequence alone does not meaningfully distinguish host cell from these specific alternatives.


**Missing item-specific fact**

> The protein-specific localization annotation or evidence that this fungal protein is secreted and found in host cells.


**Reason**

> The key is supported by sequence-matched, protein-specific annotation, but that localization fact is absent from the model input. Inferring a precise host-cell location from the sequence and choices would require external knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports host cell among the listed choices. The record also says the protein is secreted, but that is not an offered choice.


### Important caveats

- The subcellular-location statement cites a 2025 publication, but the supplied evidence does not independently establish the experimental basis or methods.
- The GO host-cell assignment is IEA:UniProtKB-SubCell, a computationally inferred annotation; it should not be mistaken for direct experimental evidence.
- The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices do not provide a biological context that identifies this protein as a pathogen effector or otherwise establishes host-cell localization. The sequence alone does not meaningfully distinguish host cell from these specific alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or evidence that this fungal protein is secreted and found in host cells.",
    "reason": "The key is supported by sequence-matched, protein-specific annotation, but that localization fact is absent from the model input. Inferring a precise host-cell location from the sequence and choices would require external knowledge."
  },
  "case_id": "GO_cellular_component_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as located in the host cell and as secreted. The host-cell annotation is also present as a GO term, though that GO assignment is computationally inferred; the subcellular-location statement cites a publication."
  },
  "important_caveats": [
    "The subcellular-location statement cites a 2025 publication, but the supplied evidence does not independently establish the experimental basis or methods.",
    "The GO host-cell assignment is IEA:UniProtKB-SubCell, a computationally inferred annotation; it should not be mistaken for direct experimental evidence.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports host cell among the listed choices. The record also says the protein is secreted, but that is not an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein as located in the host cell and as secreted. The host-cell annotation is also present as a GO term, though that GO assignment is computationally inferred; the subcellular-location statement cites a publication.",
    "evidence_ids": ["C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices do not provide a biological context that identifies this protein as a pathogen effector or otherwise establishes host-cell localization. The sequence alone does not meaningfully distinguish host cell from these specific alternatives.",
    "missing_item_specific_fact": "The protein-specific localization annotation or evidence that this fungal protein is secreted and found in host cells.",
    "reason": "The key is supported by sequence-matched, protein-specific annotation, but that localization fact is absent from the model input. Inferring a precise host-cell location from the sequence and choices would require external knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports host cell among the listed choices. The record also says the protein is secreted, but that is not an offered choice."
  },
  "important_caveats": [
    "The subcellular-location statement cites a 2025 publication, but the supplied evidence does not independently establish the experimental basis or methods.",
    "The GO host-cell assignment is IEA:UniProtKB-SubCell, a computationally inferred annotation; it should not be mistaken for direct experimental evidence.",
    "The current and historical UniProt records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry I1RQE2 (EPD1_GIBZE, Elicitor of plant defense protein 1 from Gibberella zeae/Fusarium graminearum) explicitly annotates subcellular location as 'Secreted' and 'Host cell' with evidence code ECO:0000305 sourced from PubMed:39488762. The GO cross-reference GO:0043657 (host cell) is directly derived from this UniProt subcellular location annotation. The protein is a fungal pathogen effector that is secreted and enters the host plant cell, consistent with the 'host cell' GO term (GO:0043657: 'A cell within a host organism'). The sequence match is confirmed (SHA256 identical).

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6), [C4](#evidence-c4), [C9](#evidence-c9), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The distractors B (neuron projection) and A (nuclear periphery) can be partially eliminated by general biological reasoning: fungi lack neurons, and the sequence lacks a clear nuclear localization signal. The absence of an obvious N-terminal signal peptide or transmembrane domain weakens D (Golgi apparatus). However, none of these eliminations positively identify 'host cell' (GO:0043657), which is a pathogen-specific GO term describing a protein's location within a different organism (the host). Determining that this particular protein is a secreted fungal effector that translocates into the host plant cell requires knowing the organism is a pathogen and that this specific protein has been experimentally shown to enter the host — neither of which is derivable from the amino acid sequence alone.


**Missing item-specific fact**

> The identity of the organism as a fungal plant pathogen (Gibberella zeae/Fusarium graminearum), the protein's specific function as a secreted effector (EPD1), and the experimental evidence (PubMed:39488762) demonstrating its translocation into the host cell. Without organism context or prior knowledge of this specific protein, 'host cell' cannot be inferred from sequence features.


**Reason**

> The question provides only the raw amino acid sequence and four GO term options. 'Host cell' is not a standard intracellular compartment but a pathogen-specific location annotation. No sequence motif or general biological principle allows a model to conclude that this protein resides in a 'host cell' rather than being, e.g., extracellular or cytoplasmic within its own organism. The answer depends on recognizing the protein or knowing its experimentally characterized pathogenic lifestyle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the UniProt annotation, C (host cell) is the designated answer. Options A and B are clearly inapplicable (nuclear periphery requires NLS; neuron projection is irrelevant to fungi). D (Golgi apparatus) is somewhat plausible for a secreted protein but the UniProt annotation does not assign it there. No genuine ambiguity among the choices given the annotation, though without organism context the question is extremely difficult for a model to answer by reasoning.


### Important caveats

- The GO annotation GO:0043657 (host cell) carries evidence type IEA:UniProtKB-SubCell, meaning it is automatically propagated from the UniProt subcellular location comment, not independently curated in GO.
- The subcellular location annotation in UniProt uses ECO:0000305 (inferred from biological aspect of ancestor), sourced from PubMed:39488762 — this is not a direct experimental localization method like GFP fusion but rather an inference from the protein's characterized function as a secreted effector.
- The protein lacks an obvious canonical N-terminal signal peptide, raising questions about the secretion mechanism (possibly non-classical secretion), though UniProt annotates it as 'Secreted.'
- The question provides no organism context, making the 'host cell' concept (which requires a pathogen-host relationship) inaccessible without prior knowledge of the protein's identity.
- The UniProt entry was first publicly released 2025-04-09; the benchmark's exact source snapshot is unknown but the sequence matches across available versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The distractors B (neuron projection) and A (nuclear periphery) can be partially eliminated by general biological reasoning: fungi lack neurons, and the sequence lacks a clear nuclear localization signal. The absence of an obvious N-terminal signal peptide or transmembrane domain weakens D (Golgi apparatus). However, none of these eliminations positively identify 'host cell' (GO:0043657), which is a pathogen-specific GO term describing a protein's location within a different organism (the host). Determining that this particular protein is a secreted fungal effector that translocates into the host plant cell requires knowing the organism is a pathogen and that this specific protein has been experimentally shown to enter the host — neither of which is derivable from the amino acid sequence alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the organism as a fungal plant pathogen (Gibberella zeae/Fusarium graminearum), the protein's specific function as a secreted effector (EPD1), and the experimental evidence (PubMed:39488762) demonstrating its translocation into the host cell. Without organism context or prior knowledge of this specific protein, 'host cell' cannot be inferred from sequence features.",
    "reason": "The question provides only the raw amino acid sequence and four GO term options. 'Host cell' is not a standard intracellular compartment but a pathogen-specific location annotation. No sequence motif or general biological principle allows a model to conclude that this protein resides in a 'host cell' rather than being, e.g., extracellular or cytoplasmic within its own organism. The answer depends on recognizing the protein or knowing its experimentally characterized pathogenic lifestyle."
  },
  "case_id": "GO_cellular_component_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H3",
      "H6",
      "C4",
      "C9",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry I1RQE2 (EPD1_GIBZE, Elicitor of plant defense protein 1 from Gibberella zeae/Fusarium graminearum) explicitly annotates subcellular location as 'Secreted' and 'Host cell' with evidence code ECO:0000305 sourced from PubMed:39488762. The GO cross-reference GO:0043657 (host cell) is directly derived from this UniProt subcellular location annotation. The protein is a fungal pathogen effector that is secreted and enters the host plant cell, consistent with the 'host cell' GO term (GO:0043657: 'A cell within a host organism'). The sequence match is confirmed (SHA256 identical)."
  },
  "important_caveats": [
    "The GO annotation GO:0043657 (host cell) carries evidence type IEA:UniProtKB-SubCell, meaning it is automatically propagated from the UniProt subcellular location comment, not independently curated in GO.",
    "The subcellular location annotation in UniProt uses ECO:0000305 (inferred from biological aspect of ancestor), sourced from PubMed:39488762 — this is not a direct experimental localization method like GFP fusion but rather an inference from the protein's characterized function as a secreted effector.",
    "The protein lacks an obvious canonical N-terminal signal peptide, raising questions about the secretion mechanism (possibly non-classical secretion), though UniProt annotates it as 'Secreted.'",
    "The question provides no organism context, making the 'host cell' concept (which requires a pathogen-host relationship) inaccessible without prior knowledge of the protein's identity.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark's exact source snapshot is unknown but the sequence matches across available versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the UniProt annotation, C (host cell) is the designated answer. Options A and B are clearly inapplicable (nuclear periphery requires NLS; neuron projection is irrelevant to fungi). D (Golgi apparatus) is somewhat plausible for a secreted protein but the UniProt annotation does not assign it there. No genuine ambiguity among the choices given the annotation, though without organism context the question is extremely difficult for a model to answer by reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry I1RQE2 (EPD1_GIBZE, Elicitor of plant defense protein 1 from Gibberella zeae/Fusarium graminearum) explicitly annotates subcellular location as 'Secreted' and 'Host cell' with evidence code ECO:0000305 sourced from PubMed:39488762. The GO cross-reference GO:0043657 (host cell) is directly derived from this UniProt subcellular location annotation. The protein is a fungal pathogen effector that is secreted and enters the host plant cell, consistent with the 'host cell' GO term (GO:0043657: 'A cell within a host organism'). The sequence match is confirmed (SHA256 identical).",
    "evidence_ids": ["C5", "C8", "H3", "H6", "C4", "C9", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The distractors B (neuron projection) and A (nuclear periphery) can be partially eliminated by general biological reasoning: fungi lack neurons, and the sequence lacks a clear nuclear localization signal. The absence of an obvious N-terminal signal peptide or transmembrane domain weakens D (Golgi apparatus). However, none of these eliminations positively identify 'host cell' (GO:0043657), which is a pathogen-specific GO term describing a protein's location within a different organism (the host). Determining that this particular protein is a secreted fungal effector that translocates into the host plant cell requires knowing the organism is a pathogen and that this specific protein has been experimentally shown to enter the host — neither of which is derivable from the amino acid sequence alone.",
    "missing_item_specific_fact": "The identity of the organism as a fungal plant pathogen (Gibberella zeae/Fusarium graminearum), the protein's specific function as a secreted effector (EPD1), and the experimental evidence (PubMed:39488762) demonstrating its translocation into the host cell. Without organism context or prior knowledge of this specific protein, 'host cell' cannot be inferred from sequence features.",
    "reason": "The question provides only the raw amino acid sequence and four GO term options. 'Host cell' is not a standard intracellular compartment but a pathogen-specific location annotation. No sequence motif or general biological principle allows a model to conclude that this protein resides in a 'host cell' rather than being, e.g., extracellular or cytoplasmic within its own organism. The answer depends on recognizing the protein or knowing its experimentally characterized pathogenic lifestyle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the UniProt annotation, C (host cell) is the designated answer. Options A and B are clearly inapplicable (nuclear periphery requires NLS; neuron projection is irrelevant to fungi). D (Golgi apparatus) is somewhat plausible for a secreted protein but the UniProt annotation does not assign it there. No genuine ambiguity among the choices given the annotation, though without organism context the question is extremely difficult for a model to answer by reasoning."
  },
  "important_caveats": [
    "The GO annotation GO:0043657 (host cell) carries evidence type IEA:UniProtKB-SubCell, meaning it is automatically propagated from the UniProt subcellular location comment, not independently curated in GO.",
    "The subcellular location annotation in UniProt uses ECO:0000305 (inferred from biological aspect of ancestor), sourced from PubMed:39488762 — this is not a direct experimental localization method like GFP fusion but rather an inference from the protein's characterized function as a secreted effector.",
    "The protein lacks an obvious canonical N-terminal signal peptide, raising questions about the secretion mechanism (possibly non-classical secretion), though UniProt annotates it as 'Secreted.'",
    "The question provides no organism context, making the 'host cell' concept (which requires a pathogen-host relationship) inaccessible without prior knowledge of the protein's identity.",
    "The UniProt entry was first publicly released 2025-04-09; the benchmark's exact source snapshot is unknown but the sequence matches across available versions."
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

**Accession:** `I1RQE2` (recovered from dataset image-path metadata, not original question text).  
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

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1RQE2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.811755+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39488762","source":"PubMed"}],"value":"Elicitor of plant defense protein 1"}}}
```

Source SHA-256: `877074b62a2d1a09503f72eaadd42772a942efcd59c01e121dfc3ee4f83ef4ae`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1RQE2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.811755+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39488762","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39488762","source":"PubMed"}],"id":"SL-0427","value":"Host cell"}}]}
```

Source SHA-256: `877074b62a2d1a09503f72eaadd42772a942efcd59c01e121dfc3ee4f83ef4ae`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1RQE2.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.811755+00:00.  

```json
{"database":"GO","id":"GO:0043657","properties":[{"key":"GoTerm","value":"C:host cell"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `877074b62a2d1a09503f72eaadd42772a942efcd59c01e121dfc3ee4f83ef4ae`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I1RQE2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:09.811755+00:00.  

```json
{"citation":{"authors":["Sun L.","Li X.","Zhong J.","Wang Y.","Li B.","Ye Z.","Zhang J."],"citationCrossReferences":[{"database":"PubMed","id":"39488762"},{"database":"DOI","id":"10.1002/advs.202407787"}],"citationType":"journal article","firstPage":"e2407787","id":"39488762","journal":"Adv. Sci.","lastPage":"e2407787","publicationDate":"2025","title":"Recognition of a fungal effector potentiates pathogen-associated molecular pattern-triggered immunity in cotton.","volume":"12"},"referenceNumber":4,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `877074b62a2d1a09503f72eaadd42772a942efcd59c01e121dfc3ee4f83ef4ae`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1RQE2?format=txt&versions=69)  
**Locator:** `lines 57-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-01T06:28:09.550003+00:00.  

```text
RN   [4]
RP   FUNCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=39488762; DOI=10.1002/advs.202407787;
RA   Sun L., Li X., Zhong J., Wang Y., Li B., Ye Z., Zhang J.;
RT   "Recognition of a fungal effector potentiates pathogen-associated molecular
RT   pattern-triggered immunity in cotton.";
RL   Adv. Sci. 12:e2407787-e2407787(2025).
```

Source SHA-256: `1ad63d82f55f9433ece242667d0507d1fb27257aad7e905943f4bf5b5d6e3853`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1RQE2?format=txt&versions=69)  
**Locator:** `lines 66-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-01T06:28:09.550003+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:39488762}. Host cell
CC       {ECO:0000305|PubMed:39488762}.
```

Source SHA-256: `1ad63d82f55f9433ece242667d0507d1fb27257aad7e905943f4bf5b5d6e3853`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I1RQE2?format=txt&versions=69)  
**Locator:** `lines 88-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-01T06:28:09.550003+00:00.  

```text
DR   GO; GO:0043657; C:host cell; IEA:UniProtKB-SubCell.
```

Source SHA-256: `1ad63d82f55f9433ece242667d0507d1fb27257aad7e905943f4bf5b5d6e3853`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
