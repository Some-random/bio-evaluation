# GO_cellular_component_0192

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSPRPQIKVGVLGATGTVGQRFIELLAAHPYFALHALGASSRSAGQQYARVVRWKLPSPIPDAVRHMVVHECRPDAPGFAECGVVFSGLDADVAGDIENAFRAADLVVYSNAKNYRRDPLCPLIVPLVNPSHLSIIPYQREQLGLKKGYIVTNANCSTTGIVVPLAALEKAFGPLDTVIVTTLQAISGAGYPGVSSLDIMDNVVPLISGEEDKIEWETNKILGGVTPDNKAFDLHAPKQINVSATCTRVPVIDGHTGCVSVKFARSPPPSVAEVENAFREYTCDAQHLGVPSAPAQAIVVHDAPDRPQPRLDKNLHNGACVSVGRIRECPVFDIKFVCLIDNVRLGAATSSIINAEIAVEKGLIQ

[Multiple Choices]
A. monoatomic ion channel complex
B. food vacuole
C. axon cytoplasm
D. cytosol
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

> The sequence-matched UniProt record annotates the protein to cytosol, supporting D. The annotation is transferred from a homolog, and the GO cytosol term is IEA rather than direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a compact soluble enzyme, without an obvious membrane-spanning region or secretion signal. That makes a cytosolic protein more plausible than an ion-channel complex or a food vacuole component; an axon-specific location is also not suggested.


**Missing item-specific fact**

> The exact protein-specific localization annotation is absent from the question, but is not necessary to distinguish the broad choices by this inference.


**Reason**

> The sequence and choices provide a defensible biological basis for choosing cytosol, although they do not establish localization with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Cytosol is the only listed option consistent with the sequence-based inference. The external annotation also lists nucleus, but that is not a choice and does not negate cytosolic localization.


### Important caveats

- The supplied annotation supports cytosolic localization but is transferred from a homolog; it is not direct experimental evidence for this protein.
- The annotation also includes nucleus, so cytosol should not be read as exclusive localization or as proof of the protein's primary location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble enzyme, without an obvious membrane-spanning region or secretion signal. That makes a cytosolic protein more plausible than an ion-channel complex or a food vacuole component; an axon-specific location is also not suggested.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein-specific localization annotation is absent from the question, but is not necessary to distinguish the broad choices by this inference.",
    "reason": "The sequence and choices provide a defensible biological basis for choosing cytosol, although they do not establish localization with certainty."
  },
  "case_id": "GO_cellular_component_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to cytosol, supporting D. The annotation is transferred from a homolog, and the GO cytosol term is IEA rather than direct experimental localization evidence."
  },
  "important_caveats": [
    "The supplied annotation supports cytosolic localization but is transferred from a homolog; it is not direct experimental evidence for this protein.",
    "The annotation also includes nucleus, so cytosol should not be read as exclusive localization or as proof of the protein's primary location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cytosol is the only listed option consistent with the sequence-based inference. The external annotation also lists nucleus, but that is not a choice and does not negate cytosolic localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to cytosol, supporting D. The annotation is transferred from a homolog, and the GO cytosol term is IEA rather than direct experimental localization evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble enzyme, without an obvious membrane-spanning region or secretion signal. That makes a cytosolic protein more plausible than an ion-channel complex or a food vacuole component; an axon-specific location is also not suggested.",
    "missing_item_specific_fact": "The exact protein-specific localization annotation is absent from the question, but is not necessary to distinguish the broad choices by this inference.",
    "reason": "The sequence and choices provide a defensible biological basis for choosing cytosol, although they do not establish localization with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Cytosol is the only listed option consistent with the sequence-based inference. The external annotation also lists nucleus, but that is not a choice and does not negate cytosolic localization."
  },
  "important_caveats": [
    "The supplied annotation supports cytosolic localization but is transferred from a homolog; it is not direct experimental evidence for this protein.",
    "The annotation also includes nucleus, so cytosol should not be read as exclusive localization or as proof of the protein's primary location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q5KPK7 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Cryptococcus deneoformans) annotates subcellular location as 'Cytoplasm, cytosol' (ECO:0000250, inferred by similarity from P13663, E. coli ASADHase). GO:0005829 (cytosol) is explicitly annotated with IEA:UniProtKB-SubCell. The enzyme catalyzes a step in the cytosolic aspartate biosynthesis pathway. The PDB structure (5CEF) confirms a soluble, non-membrane-associated enzyme. The expected answer 'cytosol' is consistent with both the annotation and the known biochemistry of ASADHase.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence lacks long hydrophobic stretches (>20 residues) characteristic of transmembrane helices, ruling out option A (monoatomic ion channel complex requires membrane-spanning segments). The sequence contains a Rossmann-fold NAD(P)-binding motif (VLGATGTVGQRFIELL, a GxGxxG variant), indicating a soluble dehydrogenase. No signal peptide, mitochondrial transit peptide, peroxisomal targeting signal, or vacuolar propeptide is present, making organelle-specific compartments (B: food vacuole) unlikely. Option C (axon cytoplasm) requires neuron-specific mRNA/protein targeting machinery absent from this generic enzyme sequence. By elimination of compartments requiring specific targeting signals, the default location for a soluble NAD(P)-dependent enzyme is the cytosol.


**Missing item-specific fact**

> The organism (Cryptococcus, a fungus lacking neurons) is not stated in the question, which would definitively exclude option C. However, the absence of any neuronal targeting features in the sequence still provides reasonable grounds to deprioritize axon cytoplasm.


**Reason**

> The sequence itself provides multiple discriminative features: absence of TM domains (eliminates A), presence of NAD-binding motifs indicating a soluble enzyme, and absence of any organelle-targeting signals (eliminates B and C as requiring specific targeting). The default 'soluble enzyme without targeting → cytosol' inference is standard cell biology reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, cytosol is uniquely defensible. The UniProt entry also lists 'Nucleus' as a secondary location, but nucleus is not among the choices. The distractors are clearly incompatible with the sequence features (no TM domains, no vacuolar targeting, no neuronal targeting).


### Important caveats

- The subcellular location annotation uses evidence code ECO:0000250 (similarity to P13663, E. coli ASADHase), not direct experimental localization of the fungal protein. However, the PDB structure (5CEF) and the known cytosolic pathway context support the annotation.
- The organism is not provided in the question input; reasoning about fungal biology (no neurons, no food vacuoles) requires inference from sequence context or general knowledge.
- The GO cytosol annotation is IEA (inferred from electronic annotation via UniProt-SubCell), a lower-confidence evidence type, though biologically well-supported for this enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks long hydrophobic stretches (>20 residues) characteristic of transmembrane helices, ruling out option A (monoatomic ion channel complex requires membrane-spanning segments). The sequence contains a Rossmann-fold NAD(P)-binding motif (VLGATGTVGQRFIELL, a GxGxxG variant), indicating a soluble dehydrogenase. No signal peptide, mitochondrial transit peptide, peroxisomal targeting signal, or vacuolar propeptide is present, making organelle-specific compartments (B: food vacuole) unlikely. Option C (axon cytoplasm) requires neuron-specific mRNA/protein targeting machinery absent from this generic enzyme sequence. By elimination of compartments requiring specific targeting signals, the default location for a soluble NAD(P)-dependent enzyme is the cytosol.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The organism (Cryptococcus, a fungus lacking neurons) is not stated in the question, which would definitively exclude option C. However, the absence of any neuronal targeting features in the sequence still provides reasonable grounds to deprioritize axon cytoplasm.",
    "reason": "The sequence itself provides multiple discriminative features: absence of TM domains (eliminates A), presence of NAD-binding motifs indicating a soluble enzyme, and absence of any organelle-targeting signals (eliminates B and C as requiring specific targeting). The default 'soluble enzyme without targeting → cytosol' inference is standard cell biology reasoning."
  },
  "case_id": "GO_cellular_component_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5",
      "C9",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Cryptococcus deneoformans) annotates subcellular location as 'Cytoplasm, cytosol' (ECO:0000250, inferred by similarity from P13663, E. coli ASADHase). GO:0005829 (cytosol) is explicitly annotated with IEA:UniProtKB-SubCell. The enzyme catalyzes a step in the cytosolic aspartate biosynthesis pathway. The PDB structure (5CEF) confirms a soluble, non-membrane-associated enzyme. The expected answer 'cytosol' is consistent with both the annotation and the known biochemistry of ASADHase."
  },
  "important_caveats": [
    "The subcellular location annotation uses evidence code ECO:0000250 (similarity to P13663, E. coli ASADHase), not direct experimental localization of the fungal protein. However, the PDB structure (5CEF) and the known cytosolic pathway context support the annotation.",
    "The organism is not provided in the question input; reasoning about fungal biology (no neurons, no food vacuoles) requires inference from sequence context or general knowledge.",
    "The GO cytosol annotation is IEA (inferred from electronic annotation via UniProt-SubCell), a lower-confidence evidence type, though biologically well-supported for this enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, cytosol is uniquely defensible. The UniProt entry also lists 'Nucleus' as a secondary location, but nucleus is not among the choices. The distractors are clearly incompatible with the sequence features (no TM domains, no vacuolar targeting, no neuronal targeting)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q5KPK7 (Aspartate-semialdehyde dehydrogenase, EC 1.2.1.11, from Cryptococcus deneoformans) annotates subcellular location as 'Cytoplasm, cytosol' (ECO:0000250, inferred by similarity from P13663, E. coli ASADHase). GO:0005829 (cytosol) is explicitly annotated with IEA:UniProtKB-SubCell. The enzyme catalyzes a step in the cytosolic aspartate biosynthesis pathway. The PDB structure (5CEF) confirms a soluble, non-membrane-associated enzyme. The expected answer 'cytosol' is consistent with both the annotation and the known biochemistry of ASADHase.",
    "evidence_ids": ["C5", "C6", "H4", "H5", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence lacks long hydrophobic stretches (>20 residues) characteristic of transmembrane helices, ruling out option A (monoatomic ion channel complex requires membrane-spanning segments). The sequence contains a Rossmann-fold NAD(P)-binding motif (VLGATGTVGQRFIELL, a GxGxxG variant), indicating a soluble dehydrogenase. No signal peptide, mitochondrial transit peptide, peroxisomal targeting signal, or vacuolar propeptide is present, making organelle-specific compartments (B: food vacuole) unlikely. Option C (axon cytoplasm) requires neuron-specific mRNA/protein targeting machinery absent from this generic enzyme sequence. By elimination of compartments requiring specific targeting signals, the default location for a soluble NAD(P)-dependent enzyme is the cytosol.",
    "missing_item_specific_fact": "The organism (Cryptococcus, a fungus lacking neurons) is not stated in the question, which would definitively exclude option C. However, the absence of any neuronal targeting features in the sequence still provides reasonable grounds to deprioritize axon cytoplasm.",
    "reason": "The sequence itself provides multiple discriminative features: absence of TM domains (eliminates A), presence of NAD-binding motifs indicating a soluble enzyme, and absence of any organelle-targeting signals (eliminates B and C as requiring specific targeting). The default 'soluble enzyme without targeting → cytosol' inference is standard cell biology reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, cytosol is uniquely defensible. The UniProt entry also lists 'Nucleus' as a secondary location, but nucleus is not among the choices. The distractors are clearly incompatible with the sequence features (no TM domains, no vacuolar targeting, no neuronal targeting)."
  },
  "important_caveats": [
    "The subcellular location annotation uses evidence code ECO:0000250 (similarity to P13663, E. coli ASADHase), not direct experimental localization of the fungal protein. However, the PDB structure (5CEF) and the known cytosolic pathway context support the annotation.",
    "The organism is not provided in the question input; reasoning about fungal biology (no neurons, no food vacuoles) requires inference from sequence context or general knowledge.",
    "The GO cytosol annotation is IEA (inferred from electronic annotation via UniProt-SubCell), a lower-confidence evidence type, though biologically well-supported for this enzyme class."
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

**Accession:** `Q5KPK7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
"Q5KPK7"
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/comments/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P13663","source":"UniProtKB"}],"id":"SL-0091","value":"Cytoplasm, cytosol"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P13663","source":"UniProtKB"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/uniProtKBCrossReferences/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5KPK7.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:24.745599+00:00.  

```json
{"citation":{"authors":["Dahal G.","Viola R.E."],"citationCrossReferences":[{"database":"PubMed","id":"26527262"},{"database":"DOI","id":"10.1107/s2053230x15017495"}],"citationType":"journal article","firstPage":"1365","id":"26527262","journal":"Acta Crystallogr. F Struct. Biol. Commun.","lastPage":"1371","publicationDate":"2015","title":"Structure of a fungal form of aspartate semialdehyde dehydrogenase from Cryptococcus neoformans.","volume":"71"},"evidences":[{"evidenceCode":"ECO:0007744","id":"5CEF","source":"PDB"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.60 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT"]}
```

Source SHA-256: `6e1b51beba0452942e5c6cb2774ea67654b44f73f1d91b259ec7240bea1d2e67`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 88-89`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm, cytosol
CC       {ECO:0000250|UniProtKB:P13663}. Nucleus {ECO:0000250|UniProtKB:P13663}.
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5KPK7?format=txt&versions=121)  
**Locator:** `lines 118-118`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:31:27.262588+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; IEA:UniProtKB-SubCell.
```

Source SHA-256: `117184b77b1c1a6b186665d7a7a3070affc905fd69df2a927a14fb0e3ceb88c4`.

### Evidence GO1

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
