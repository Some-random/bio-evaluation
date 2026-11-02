# GO_cellular_component_0029

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNEALDDIDRILVRELAADGRATLSELATRAGLSVSAVQSRVRRLESRGVVQGYSARINPEAVGHLLSAFVAITPLDPSQPDDAPARLEHIEEVESCYSVAGEESYVLLVRVASARALEDLLQRIRTTANVRTRSTIILNTFYSDRQHIP

[Multiple Choices]
A. cytosol
B. chloroplast
C. cytoplasm
D. recycling endosome membrane
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

> The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IBA evidence, a computational, phylogenetically inferred annotation rather than direct experimental localization evidence. This supports the key as an annotation, without establishing that it was experimentally measured.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble protein and offers no obvious membrane-spanning or organelle-targeting signal, which can favor an intracellular soluble location over the membrane and chloroplast distractors. It does not, however, distinguish the specific GO label cytosol from the broader cytoplasm label.


**Missing item-specific fact**

> A protein-specific localization annotation or other evidence resolving which cellular-component term is intended; the input does not provide it.


**Reason**

> The sequence may support a general soluble intracellular prediction, but the decisive distinction between the nested cytosol and cytoplasm choices is not established by that inference. Selecting the keyed term depends on the protein-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Cytosol is part of the cytoplasm, so both labels can describe a soluble intracellular protein. The question gives no criterion for choosing the narrower term over the broader one.


### Important caveats

- The sequence match and UniProt annotation support the key, but the cited IBA evidence is computational, not direct experimental localization evidence.
- The reviewer-only source identity and annotation were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble protein and offers no obvious membrane-spanning or organelle-targeting signal, which can favor an intracellular soluble location over the membrane and chloroplast distractors. It does not, however, distinguish the specific GO label cytosol from the broader cytoplasm label.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A protein-specific localization annotation or other evidence resolving which cellular-component term is intended; the input does not provide it.",
    "reason": "The sequence may support a general soluble intracellular prediction, but the decisive distinction between the nested cytosol and cytoplasm choices is not established by that inference. Selecting the keyed term depends on the protein-specific annotation."
  },
  "case_id": "GO_cellular_component_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IBA evidence, a computational, phylogenetically inferred annotation rather than direct experimental localization evidence. This supports the key as an annotation, without establishing that it was experimentally measured."
  },
  "important_caveats": [
    "The sequence match and UniProt annotation support the key, but the cited IBA evidence is computational, not direct experimental localization evidence.",
    "The reviewer-only source identity and annotation were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Cytosol is part of the cytoplasm, so both labels can describe a soluble intracellular protein. The question gives no criterion for choosing the narrower term over the broader one."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated to cytosol (GO:0005829) with IBA evidence, a computational, phylogenetically inferred annotation rather than direct experimental localization evidence. This supports the key as an annotation, without establishing that it was experimentally measured.",
    "evidence_ids": ["C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble protein and offers no obvious membrane-spanning or organelle-targeting signal, which can favor an intracellular soluble location over the membrane and chloroplast distractors. It does not, however, distinguish the specific GO label cytosol from the broader cytoplasm label.",
    "missing_item_specific_fact": "A protein-specific localization annotation or other evidence resolving which cellular-component term is intended; the input does not provide it.",
    "reason": "The sequence may support a general soluble intracellular prediction, but the decisive distinction between the nested cytosol and cytoplasm choices is not established by that inference. Selecting the keyed term depends on the protein-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Cytosol is part of the cytoplasm, so both labels can describe a soluble intracellular protein. The question gives no criterion for choosing the narrower term over the broader one."
  },
  "important_caveats": [
    "The sequence match and UniProt annotation support the key, but the cited IBA evidence is computational, not direct experimental localization evidence.",
    "The reviewer-only source identity and annotation were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (I6YBQ3, LRPA_MYCTU) annotates GO:0005829 (cytosol) with evidence code IBA:GO_Central (C5, H5). The protein is an HTH-type transcriptional regulator (LrpA / feast-famine regulatory protein) from Mycobacterium tuberculosis, a bacterium. Crystal structures (2IVM, 2VBW–2VC1, 2QZ8) confirm it is a soluble DNA-binding protein with cofactor-binding domains, consistent with cytosolic localization. The IBA evidence code indicates computational inference rather than direct experimental measurement, but the biological context (soluble bacterial transcription factor functioning in the aqueous phase to bind genomic DNA) strongly supports the cytosol annotation. Options B (chloroplast) and D (recycling endosome membrane) are inapplicable to a bacterium.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C7](#evidence-c7), [H5](#evidence-h5), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a 150-residue HTH-type transcriptional regulator from a bacterium (M. tuberculosis). Bacteria lack chloroplasts and endosomes, immediately eliminating B and D. The sequence contains no transmembrane helices, signal peptides, or organelle-targeting motifs; it is a soluble DNA-binding protein confirmed by multiple crystal structures. In GO, cytosol (GO:0005829) is defined as the part of the cytoplasm excluding organelles and is the appropriate term for soluble proteins functioning in the aqueous phase. A soluble bacterial transcription factor that binds genomic DNA in the nucleoid region resides in the cytosol, not merely the broader 'cytoplasm' (GO:0005737), which includes membrane-bound structures. This reasoning distinguishes A from C without requiring the specific UniProt annotation.


**Missing item-specific fact**

> None critical. The IBA evidence code means the specific 'cytosol' label was propagated computationally rather than measured, but the biological argument (soluble, no targeting signals, DNA-binding transcription factor) independently supports cytosol over cytoplasm.


**Reason**

> Eliminating B and D requires only knowing the organism is a bacterium. Distinguishing A (cytosol) from C (cytoplasm) relies on the general GO convention that soluble proteins are annotated to cytosol (the organelle-free aqueous fraction) rather than the broader cytoplasm. This is a defensible biological/ontological reasoning step applicable to any soluble protein, not a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> In the GO ontology, cytosol is a child of cytoplasm (cytosol part_of cytoplasm). For a soluble bacterial protein, 'cytoplasm' (C) is not biologically incorrect—it is simply less specific than 'cytosol' (A). A model selecting C could argue it is the broader, equally valid compartment. However, the question asks for the 'primary' cellular component, and for a soluble protein with no association to organelles or membranes, 'cytosol' is the more precise and conventionally preferred GO annotation, making A the better answer. B and D are unambiguously wrong for a bacterium.


### Important caveats

- The GO annotation uses IBA:GO_Central (Inferred by Biological Aspect of Ancestor), a graph-based computational inference, not direct experimental localization data. No subcellular fractionation or microscopy experiment is cited for this protein's localization.
- The UniProt accession (I6YBQ3) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must reason from the sequence alone.
- The protein was integrated into Swiss-Prot only on 2025-02-05 (entry version 81 at review time; version 79 at historical cutoff). The author's source snapshot date is unknown, but the sequence and annotation are consistent across versions checked.
- The cytosol-vs-cytoplasm distinction, while resolvable by GO convention, is a fine-grained ontological point that some biologists treat as interchangeable in casual usage.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a 150-residue HTH-type transcriptional regulator from a bacterium (M. tuberculosis). Bacteria lack chloroplasts and endosomes, immediately eliminating B and D. The sequence contains no transmembrane helices, signal peptides, or organelle-targeting motifs; it is a soluble DNA-binding protein confirmed by multiple crystal structures. In GO, cytosol (GO:0005829) is defined as the part of the cytoplasm excluding organelles and is the appropriate term for soluble proteins functioning in the aqueous phase. A soluble bacterial transcription factor that binds genomic DNA in the nucleoid region resides in the cytosol, not merely the broader 'cytoplasm' (GO:0005737), which includes membrane-bound structures. This reasoning distinguishes A from C without requiring the specific UniProt annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The IBA evidence code means the specific 'cytosol' label was propagated computationally rather than measured, but the biological argument (soluble, no targeting signals, DNA-binding transcription factor) independently supports cytosol over cytoplasm.",
    "reason": "Eliminating B and D requires only knowing the organism is a bacterium. Distinguishing A (cytosol) from C (cytoplasm) relies on the general GO convention that soluble proteins are annotated to cytosol (the organelle-free aqueous fraction) rather than the broader cytoplasm. This is a defensible biological/ontological reasoning step applicable to any soluble protein, not a protein-specific lookup."
  },
  "case_id": "GO_cellular_component_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C7",
      "H5",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (I6YBQ3, LRPA_MYCTU) annotates GO:0005829 (cytosol) with evidence code IBA:GO_Central (C5, H5). The protein is an HTH-type transcriptional regulator (LrpA / feast-famine regulatory protein) from Mycobacterium tuberculosis, a bacterium. Crystal structures (2IVM, 2VBW–2VC1, 2QZ8) confirm it is a soluble DNA-binding protein with cofactor-binding domains, consistent with cytosolic localization. The IBA evidence code indicates computational inference rather than direct experimental measurement, but the biological context (soluble bacterial transcription factor functioning in the aqueous phase to bind genomic DNA) strongly supports the cytosol annotation. Options B (chloroplast) and D (recycling endosome membrane) are inapplicable to a bacterium."
  },
  "important_caveats": [
    "The GO annotation uses IBA:GO_Central (Inferred by Biological Aspect of Ancestor), a graph-based computational inference, not direct experimental localization data. No subcellular fractionation or microscopy experiment is cited for this protein's localization.",
    "The UniProt accession (I6YBQ3) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must reason from the sequence alone.",
    "The protein was integrated into Swiss-Prot only on 2025-02-05 (entry version 81 at review time; version 79 at historical cutoff). The author's source snapshot date is unknown, but the sequence and annotation are consistent across versions checked.",
    "The cytosol-vs-cytoplasm distinction, while resolvable by GO convention, is a fine-grained ontological point that some biologists treat as interchangeable in casual usage."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "In the GO ontology, cytosol is a child of cytoplasm (cytosol part_of cytoplasm). For a soluble bacterial protein, 'cytoplasm' (C) is not biologically incorrect—it is simply less specific than 'cytosol' (A). A model selecting C could argue it is the broader, equally valid compartment. However, the question asks for the 'primary' cellular component, and for a soluble protein with no association to organelles or membranes, 'cytosol' is the more precise and conventionally preferred GO annotation, making A the better answer. B and D are unambiguously wrong for a bacterium."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (I6YBQ3, LRPA_MYCTU) annotates GO:0005829 (cytosol) with evidence code IBA:GO_Central (C5, H5). The protein is an HTH-type transcriptional regulator (LrpA / feast-famine regulatory protein) from Mycobacterium tuberculosis, a bacterium. Crystal structures (2IVM, 2VBW–2VC1, 2QZ8) confirm it is a soluble DNA-binding protein with cofactor-binding domains, consistent with cytosolic localization. The IBA evidence code indicates computational inference rather than direct experimental measurement, but the biological context (soluble bacterial transcription factor functioning in the aqueous phase to bind genomic DNA) strongly supports the cytosol annotation. Options B (chloroplast) and D (recycling endosome membrane) are inapplicable to a bacterium.",
    "evidence_ids": ["C5", "C4", "C7", "H5", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a 150-residue HTH-type transcriptional regulator from a bacterium (M. tuberculosis). Bacteria lack chloroplasts and endosomes, immediately eliminating B and D. The sequence contains no transmembrane helices, signal peptides, or organelle-targeting motifs; it is a soluble DNA-binding protein confirmed by multiple crystal structures. In GO, cytosol (GO:0005829) is defined as the part of the cytoplasm excluding organelles and is the appropriate term for soluble proteins functioning in the aqueous phase. A soluble bacterial transcription factor that binds genomic DNA in the nucleoid region resides in the cytosol, not merely the broader 'cytoplasm' (GO:0005737), which includes membrane-bound structures. This reasoning distinguishes A from C without requiring the specific UniProt annotation.",
    "missing_item_specific_fact": "None critical. The IBA evidence code means the specific 'cytosol' label was propagated computationally rather than measured, but the biological argument (soluble, no targeting signals, DNA-binding transcription factor) independently supports cytosol over cytoplasm.",
    "reason": "Eliminating B and D requires only knowing the organism is a bacterium. Distinguishing A (cytosol) from C (cytoplasm) relies on the general GO convention that soluble proteins are annotated to cytosol (the organelle-free aqueous fraction) rather than the broader cytoplasm. This is a defensible biological/ontological reasoning step applicable to any soluble protein, not a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "In the GO ontology, cytosol is a child of cytoplasm (cytosol part_of cytoplasm). For a soluble bacterial protein, 'cytoplasm' (C) is not biologically incorrect—it is simply less specific than 'cytosol' (A). A model selecting C could argue it is the broader, equally valid compartment. However, the question asks for the 'primary' cellular component, and for a soluble protein with no association to organelles or membranes, 'cytosol' is the more precise and conventionally preferred GO annotation, making A the better answer. B and D are unambiguously wrong for a bacterium."
  },
  "important_caveats": [
    "The GO annotation uses IBA:GO_Central (Inferred by Biological Aspect of Ancestor), a graph-based computational inference, not direct experimental localization data. No subcellular fractionation or microscopy experiment is cited for this protein's localization.",
    "The UniProt accession (I6YBQ3) was inferred by the reviewer from dataset metadata; it was not provided to the evaluated model. The model must reason from the sequence alone.",
    "The protein was integrated into Swiss-Prot only on 2025-02-05 (entry version 81 at review time; version 79 at historical cutoff). The author's source snapshot date is unknown, but the sequence and annotation are consistent across versions checked.",
    "The cytosol-vs-cytoplasm distinction, while resolvable by GO convention, is a fine-grained ontological point that some biologists treat as interchangeable in casual usage."
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

**Accession:** `I6YBQ3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17962306","source":"PubMed"}],"value":"Feast/famine regulatory protein Rv3291c"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17962306","source":"PubMed"}],"value":"MtbLrp"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26789099","source":"PubMed"}],"value":"MtbLrpA"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional regulator LrpA"}}}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/uniProtKBCrossReferences/42`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I6YBQ3.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.289633+00:00.  

```json
{"citation":{"authors":["Shrivastava T.","Ramachandran R."],"citationCrossReferences":[{"database":"PubMed","id":"17962306"},{"database":"DOI","id":"10.1093/nar/gkm850"}],"citationType":"journal article","firstPage":"7324","id":"17962306","journal":"Nucleic Acids Res.","lastPage":"7335","publicationDate":"2007","title":"Mechanistic insights from the crystal structures of a feast/famine regulatory protein from Mycobacterium tuberculosis H37Rv.","volume":"35"},"evidences":[{"evidenceCode":"ECO:0007744","id":"2IVM","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VBZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VC0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"2VC1","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"H37Rv"}],"referenceNumber":7,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) OF APOPROTEIN AND IN COMPLEXES WITH HISTIDINE; LEUCINE; METHIONINE; PHENYLALANINE; TRYPTOPHAN AND TYROSINE","ACTIVITY REGULATION","SUBUNIT","DOMAIN"]}
```

Source SHA-256: `3978e04c41379d89d9a497b2d685cf726895877f193db390290b68c748badf35`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I6YBQ3?format=txt&versions=79)  
**Locator:** `lines 75-84`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:11.636802+00:00.  

```text
RN   [7] {ECO:0007744|PDB:2IVM, ECO:0007744|PDB:2VBW, ECO:0007744|PDB:2VBX, ECO:0007744|PDB:2VBY, ECO:0007744|PDB:2VBZ, ECO:0007744|PDB:2VC0, ECO:0007744|PDB:2VC1}
RP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) OF APOPROTEIN AND IN COMPLEXES WITH
RP   HISTIDINE; LEUCINE; METHIONINE; PHENYLALANINE; TRYPTOPHAN AND TYROSINE,
RP   ACTIVITY REGULATION, SUBUNIT, AND DOMAIN.
RC   STRAIN=H37Rv;
RX   PubMed=17962306; DOI=10.1093/nar/gkm850;
RA   Shrivastava T., Ramachandran R.;
RT   "Mechanistic insights from the crystal structures of a feast/famine
RT   regulatory protein from Mycobacterium tuberculosis H37Rv.";
RL   Nucleic Acids Res. 35:7324-7335(2007).
```

Source SHA-256: `0d8bb5d3f126c254cc07f1a917b843bb272ed6b3990eb34e792e13bcb3ee45b0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I6YBQ3?format=txt&versions=79)  
**Locator:** `lines 85-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:11.636802+00:00.  

```text
RN   [8] {ECO:0007744|PDB:2QZ8}
RP   X-RAY CRYSTALLOGRAPHY (2.16 ANGSTROMS) OF 5-150 OF MUTANT MET-108,
RP   FUNCTION, DNA-BINDING, ACTIVITY REGULATION, SUBUNIT, AND DOMAIN.
RC   STRAIN=H37Rv;
RX   PubMed=18042675; DOI=10.1110/ps.073192208;
RA   Reddy M.C., Gokulan K., Jacobs W.R., Ioerger T.R., Sacchettini J.C.;
RT   "Crystal structure of Mycobacterium tuberculosis LrpA, a leucine-responsive
RT   global regulator associated with starvation response.";
RL   Protein Sci. 17:159-170(2008).
```

Source SHA-256: `0d8bb5d3f126c254cc07f1a917b843bb272ed6b3990eb34e792e13bcb3ee45b0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I6YBQ3?format=txt&versions=79)  
**Locator:** `lines 193-193`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:11.636802+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IBA:GO_Central.
```

Source SHA-256: `0d8bb5d3f126c254cc07f1a917b843bb272ed6b3990eb34e792e13bcb3ee45b0`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59936-59953`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005829
name: cytosol
namespace: cellular_component
def: "The part of the cytoplasm that does not contain organelles but which does contain other particulate matter, such as protein complexes." [GOC:hjd, GOC:jl]
subset: goslim_agr
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_plant
xref: NIF_Subcellular:sao101633890
xref: Wikipedia:Cytosol
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
