# GO_cellular_component_0185

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDSNMMPQTAQQNAVFSKTNFAQQKLGQYQVVAPASPVCSRPGSSCSQPPTLFSNGPAVLTPTGSPPPIGFRPAVMLESEFGDSSYFPSTPPLSTSGSAVGSPKNYEVLQTPLNPMFSGLDGFVGVKSGYESTESSVLDWASCDSPPMTPVFIHSQPSRVPSLSSTTSDLSNISCPSLSPSPAPYARSVSSENDVDFCDPRNLTVPNTSNSSLAPEFTLDCLGEEEGSPSEQSALDTVLSQTAFDFSPAIASGLPAFEELSDFESEDDLSNLVKPGEGSRPRACTGSSIVSLGHGSFIADEDFSFDENDTFQFPSPSPPSSVEAVDDGHKDKRQKKTGTKDSQSAEPVMDTAAADNQTAEVEEQSEQASPVPSESHSSAEADTPSAPLPAPTNRRGRKQSLTEDPSKTFVCDLCNRRFRRQEHLKRHYRSLHTQEKPFECNECGKKFSRSDNLAQHARTHASGGAIVMNIIDNADPSAYEAGMVAPPPVDDYANYGKVLFQIAADVPGSASELSSEEASDNGKKKRKRSE

[Multiple Choices]
A. nuclear membrane
B. nucleus
C. cytosolic large ribosomal subunit
D. membrane attack complex
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

> The sequence-matched UniProt record identifies this protein as the MSN2 transcription factor and annotates it to the nucleus, although the localization evidence is transferred by similarity rather than presented as direct experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal C2H2-type zinc-finger motif and nearby basic residues are consistent with a nuclear DNA-binding transcription factor. The sequence also lacks an evident transmembrane segment, and it does not resemble a ribosomal protein or a component of the complement membrane attack complex.


**Missing item-specific fact**

> No protein-specific external fact is strictly necessary to distinguish nucleus from the listed alternatives, though the exact localization annotation is item-specific.


**Reason**

> Sequence motifs and protein-class reasoning meaningfully favor the nucleus over the distractors; this is not merely a case of recalling the exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also annotates cytoplasmic localization, but that is not among the choices. Of the listed choices, nucleus is the supported localization; nuclear membrane is a distinct, more specific location not established by the supplied sequence.


### Important caveats

- The sequence-matched UniProt annotation reports both nucleus and cytoplasm, so the protein may shuttle or have multiple localizations.
- The available localization annotation is transferred by similarity; it should not be represented as direct experimental validation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal C2H2-type zinc-finger motif and nearby basic residues are consistent with a nuclear DNA-binding transcription factor. The sequence also lacks an evident transmembrane segment, and it does not resemble a ribosomal protein or a component of the complement membrane attack complex.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external fact is strictly necessary to distinguish nucleus from the listed alternatives, though the exact localization annotation is item-specific.",
    "reason": "Sequence motifs and protein-class reasoning meaningfully favor the nucleus over the distractors; this is not merely a case of recalling the exact database entry."
  },
  "case_id": "GO_cellular_component_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as the MSN2 transcription factor and annotates it to the nucleus, although the localization evidence is transferred by similarity rather than presented as direct experimental evidence."
  },
  "important_caveats": [
    "The sequence-matched UniProt annotation reports both nucleus and cytoplasm, so the protein may shuttle or have multiple localizations.",
    "The available localization annotation is transferred by similarity; it should not be represented as direct experimental validation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytoplasmic localization, but that is not among the choices. Of the listed choices, nucleus is the supported localization; nuclear membrane is a distinct, more specific location not established by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record identifies this protein as the MSN2 transcription factor and annotates it to the nucleus, although the localization evidence is transferred by similarity rather than presented as direct experimental evidence.",
    "evidence_ids": ["C4", "C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal C2H2-type zinc-finger motif and nearby basic residues are consistent with a nuclear DNA-binding transcription factor. The sequence also lacks an evident transmembrane segment, and it does not resemble a ribosomal protein or a component of the complement membrane attack complex.",
    "missing_item_specific_fact": "No protein-specific external fact is strictly necessary to distinguish nucleus from the listed alternatives, though the exact localization annotation is item-specific.",
    "reason": "Sequence motifs and protein-class reasoning meaningfully favor the nucleus over the distractors; this is not merely a case of recalling the exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also annotates cytoplasmic localization, but that is not among the choices. Of the listed choices, nucleus is the supported localization; nuclear membrane is a distinct, more specific location not established by the supplied sequence."
  },
  "important_caveats": [
    "The sequence-matched UniProt annotation reports both nucleus and cytoplasm, so the protein may shuttle or have multiple localizations.",
    "The available localization annotation is transferred by similarity; it should not be represented as direct experimental validation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (E9F0C5) annotates this protein as a C2H2-type transcription factor MSN2 with GO:0005634 (nucleus) as a cellular component (ISS:UniProtKB evidence). The protein name and functional annotation as a transcription factor are consistent with nuclear localization. The annotation also lists cytoplasm, but the question asks for the primary compartment, and for a C2H2-type transcription factor the nucleus is the primary functional site. The evidence is computational (ISS/ECO:0000250 from sequence similarity to G4NBR8), not direct experimental localization, but it is the standard annotation supporting the key.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [C9](#evidence-c9), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable C2H2-type zinc finger motif ('ECNECGKKFSRSDNLAQHARTH' with the canonical C-x2-C-x12-H-x3-H pattern), identifying it as a DNA-binding transcription factor, which functions in the nucleus. Additionally, multiple basic-residue clusters (e.g., 'KKKRKRSE' at the C-terminus, 'NRRGRKQSL' internally) are consistent with nuclear localization signals. General biology dictates that transcription factors act on chromatin in the nucleus. The distractors are eliminable: the membrane attack complex is a mammalian complement pore-forming complex irrelevant to a fungal protein; a cytosolic ribosomal subunit would show ribosomal-protein fold features absent here; the nuclear membrane is a lipid bilayer compartment for transmembrane proteins, not soluble transcription factors.


**Missing item-specific fact**

> None critical. The C2H2 zinc finger and NLS-like basic clusters are visible in the sequence, and the inference that a transcription factor localizes to the nucleus is general biological knowledge.


**Reason**

> A model with general knowledge of zinc-finger transcription factors, NLS motifs, and cellular compartment biology can identify the C2H2 domain in the sequence, infer transcription-factor function, recognize basic clusters as NLS, and eliminate the three distractors without needing to recall the specific UniProt accession or its annotation. The reasoning chain (zinc finger → TF → nucleus; basic clusters → NLS → nucleus; eliminate MAC/ribosome/nuclear membrane) is grounded in the supplied sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although UniProt lists both nucleus and cytoplasm, cytoplasm is not among the four choices. Among A–D, only 'nucleus' (B) is consistent with a soluble C2H2 transcription factor. The other three options (nuclear membrane, ribosomal subunit, membrane attack complex) are clearly incompatible with the protein's identity and sequence features.


### Important caveats

- The UniProt nucleus annotation is ISS (inferred from sequence similarity to G4NBR8), not direct experimental localization; the primary paper (PMID:23466345) reports function and disruption phenotype but the subcellular-location evidence code is computational transfer.
- The annotation also lists cytoplasm as a secondary location, but this does not affect the 'primary' compartment answer among the given choices.
- The GO term 'cytosolic large ribosomal subunit' in option C maps to an obsolete term (GO:0000180, obsoleted; active term GO:0022625); this is a minor wording issue that does not change the answer.
- Sequence identity to the UniProt entry is confirmed (530 aa, SHA-256 match) across both current and historical (v50) snapshots.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable C2H2-type zinc finger motif ('ECNECGKKFSRSDNLAQHARTH' with the canonical C-x2-C-x12-H-x3-H pattern), identifying it as a DNA-binding transcription factor, which functions in the nucleus. Additionally, multiple basic-residue clusters (e.g., 'KKKRKRSE' at the C-terminus, 'NRRGRKQSL' internally) are consistent with nuclear localization signals. General biology dictates that transcription factors act on chromatin in the nucleus. The distractors are eliminable: the membrane attack complex is a mammalian complement pore-forming complex irrelevant to a fungal protein; a cytosolic ribosomal subunit would show ribosomal-protein fold features absent here; the nuclear membrane is a lipid bilayer compartment for transmembrane proteins, not soluble transcription factors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The C2H2 zinc finger and NLS-like basic clusters are visible in the sequence, and the inference that a transcription factor localizes to the nucleus is general biological knowledge.",
    "reason": "A model with general knowledge of zinc-finger transcription factors, NLS motifs, and cellular compartment biology can identify the C2H2 domain in the sequence, infer transcription-factor function, recognize basic clusters as NLS, and eliminate the three distractors without needing to recall the specific UniProt accession or its annotation. The reasoning chain (zinc finger → TF → nucleus; basic clusters → NLS → nucleus; eliminate MAC/ribosome/nuclear membrane) is grounded in the supplied sequence."
  },
  "case_id": "GO_cellular_component_0185",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "C9",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (E9F0C5) annotates this protein as a C2H2-type transcription factor MSN2 with GO:0005634 (nucleus) as a cellular component (ISS:UniProtKB evidence). The protein name and functional annotation as a transcription factor are consistent with nuclear localization. The annotation also lists cytoplasm, but the question asks for the primary compartment, and for a C2H2-type transcription factor the nucleus is the primary functional site. The evidence is computational (ISS/ECO:0000250 from sequence similarity to G4NBR8), not direct experimental localization, but it is the standard annotation supporting the key."
  },
  "important_caveats": [
    "The UniProt nucleus annotation is ISS (inferred from sequence similarity to G4NBR8), not direct experimental localization; the primary paper (PMID:23466345) reports function and disruption phenotype but the subcellular-location evidence code is computational transfer.",
    "The annotation also lists cytoplasm as a secondary location, but this does not affect the 'primary' compartment answer among the given choices.",
    "The GO term 'cytosolic large ribosomal subunit' in option C maps to an obsolete term (GO:0000180, obsoleted; active term GO:0022625); this is a minor wording issue that does not change the answer.",
    "Sequence identity to the UniProt entry is confirmed (530 aa, SHA-256 match) across both current and historical (v50) snapshots."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt lists both nucleus and cytoplasm, cytoplasm is not among the four choices. Among A–D, only 'nucleus' (B) is consistent with a soluble C2H2 transcription factor. The other three options (nuclear membrane, ribosomal subunit, membrane attack complex) are clearly incompatible with the protein's identity and sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0185",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (E9F0C5) annotates this protein as a C2H2-type transcription factor MSN2 with GO:0005634 (nucleus) as a cellular component (ISS:UniProtKB evidence). The protein name and functional annotation as a transcription factor are consistent with nuclear localization. The annotation also lists cytoplasm, but the question asks for the primary compartment, and for a C2H2-type transcription factor the nucleus is the primary functional site. The evidence is computational (ISS/ECO:0000250 from sequence similarity to G4NBR8), not direct experimental localization, but it is the standard annotation supporting the key.",
    "evidence_ids": ["C4", "C5", "C8", "C9", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable C2H2-type zinc finger motif ('ECNECGKKFSRSDNLAQHARTH' with the canonical C-x2-C-x12-H-x3-H pattern), identifying it as a DNA-binding transcription factor, which functions in the nucleus. Additionally, multiple basic-residue clusters (e.g., 'KKKRKRSE' at the C-terminus, 'NRRGRKQSL' internally) are consistent with nuclear localization signals. General biology dictates that transcription factors act on chromatin in the nucleus. The distractors are eliminable: the membrane attack complex is a mammalian complement pore-forming complex irrelevant to a fungal protein; a cytosolic ribosomal subunit would show ribosomal-protein fold features absent here; the nuclear membrane is a lipid bilayer compartment for transmembrane proteins, not soluble transcription factors.",
    "missing_item_specific_fact": "None critical. The C2H2 zinc finger and NLS-like basic clusters are visible in the sequence, and the inference that a transcription factor localizes to the nucleus is general biological knowledge.",
    "reason": "A model with general knowledge of zinc-finger transcription factors, NLS motifs, and cellular compartment biology can identify the C2H2 domain in the sequence, infer transcription-factor function, recognize basic clusters as NLS, and eliminate the three distractors without needing to recall the specific UniProt accession or its annotation. The reasoning chain (zinc finger → TF → nucleus; basic clusters → NLS → nucleus; eliminate MAC/ribosome/nuclear membrane) is grounded in the supplied sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although UniProt lists both nucleus and cytoplasm, cytoplasm is not among the four choices. Among A–D, only 'nucleus' (B) is consistent with a soluble C2H2 transcription factor. The other three options (nuclear membrane, ribosomal subunit, membrane attack complex) are clearly incompatible with the protein's identity and sequence features."
  },
  "important_caveats": [
    "The UniProt nucleus annotation is ISS (inferred from sequence similarity to G4NBR8), not direct experimental localization; the primary paper (PMID:23466345) reports function and disruption phenotype but the subcellular-location evidence code is computational transfer.",
    "The annotation also lists cytoplasm as a secondary location, but this does not affect the 'primary' compartment answer among the given choices.",
    "The GO term 'cytosolic large ribosomal subunit' in option C maps to an obsolete term (GO:0000180, obsoleted; active term GO:0022625); this is a minor wording issue that does not change the answer.",
    "Sequence identity to the UniProt entry is confirmed (530 aa, SHA-256 match) across both current and historical (v50) snapshots."
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

**Accession:** `E9F0C5` (recovered from dataset image-path metadata, not original question text).  
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9F0C5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:06.132793+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23466345","source":"PubMed"}],"value":"C2H2-type transcription factor MSN2"}}}
```

Source SHA-256: `6186b673962844efa14ca82f5ff96f5226868f3121fe7ec52e5ac93a49dfa9bf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9F0C5.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:06.132793+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"G4NBR8","source":"UniProtKB"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"G4NBR8","source":"UniProtKB"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `6186b673962844efa14ca82f5ff96f5226868f3121fe7ec52e5ac93a49dfa9bf`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9F0C5.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:06.132793+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `6186b673962844efa14ca82f5ff96f5226868f3121fe7ec52e5ac93a49dfa9bf`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9F0C5.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:06.132793+00:00.  

```json
{"citation":{"authors":["Liu Q.","Ying S.H.","Li J.G.","Tian C.G.","Feng M.G."],"citationCrossReferences":[{"database":"PubMed","id":"23466345"},{"database":"DOI","id":"10.1016/j.fgb.2013.02.008"}],"citationType":"journal article","firstPage":"42","id":"23466345","journal":"Fungal Genet. Biol.","lastPage":"51","publicationDate":"2013","title":"Insight into the transcriptional regulation of Msn2 required for conidiation, multi-stress responses and virulence of two entomopathogenic fungi.","volume":"54"},"referenceNumber":3,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `6186b673962844efa14ca82f5ff96f5226868f3121fe7ec52e5ac93a49dfa9bf`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9F0C5?format=txt&versions=50)  
**Locator:** `lines 48-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-02T04:28:10.306622+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000250|UniProtKB:G4NBR8}. Cytoplasm
CC       {ECO:0000250|UniProtKB:G4NBR8}.
```

Source SHA-256: `94c790046489e4075d1217fb237674f6a0ea5dcfa1ab143b1b687df7eab716e4`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9F0C5?format=txt&versions=50)  
**Locator:** `lines 74-74`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 50 / 1.  
**Retrieved:** 2026-11-02T04:28:10.306622+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IEA:UniProtKB-SubCell.
```

Source SHA-256: `94c790046489e4075d1217fb237674f6a0ea5dcfa1ab143b1b687df7eab716e4`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 185. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
